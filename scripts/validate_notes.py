#!/usr/bin/env python3
"""Validate the AWS Machine Learning and AI notes vault without external dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FRONTMATTER_KEYS = (
    "title",
    "scope",
    "status",
    "domain",
    "service",
    "tags",
    "aliases",
    "last_verified",
    "source_type",
)

ALLOWED_STATUSES = {
    "reviewed",
    "draft",
    "stale",
    "legacy",
    "supplemental",
    "out-of-scope",
}

EXPECTED_SCOPE = "AWS Machine Learning and AI"

CANONICAL_SECTION_GROUPS = (
    ("## Knowledge Relevance", ("## Knowledge Relevance", "## Exam Relevance")),
    ("## When To Use", ("## When To Use",)),
    ("## Core Concepts", ("## Core Concepts",)),
    ("## AWS Services And Features", ("## AWS Services And Features",)),
    ("## Implementation Patterns", ("## Implementation Patterns",)),
    ("## Tradeoffs And Pitfalls", ("## Tradeoffs And Pitfalls",)),
    ("## Decision Triggers", ("## Decision Triggers", "## Exam Triggers")),
    ("## Related Notes", ("## Related Notes",)),
    ("## Sources", ("## Sources",)),
)

CONTENT_EXCLUDES = {
    "README.md",
    "PLAN_NOTES_IMPROVEMENT.md",
    "NOTE_TEMPLATE.md",
}

SOURCE_SECTION = re.compile(
    r"^(## )?(Sources|References|Additional Resources)\b",
    re.MULTILINE,
)

RISK_TERMS = re.compile(
    r"Elastic Inference|Training Compiler|Data Pipeline|Amazon Forecast|"
    r"AWS AppConfig|AWS IoT Greengrass|AWS Shield|Amazon DataZone|"
    r"Kinesis Data Analytics|Studio Classic|Edge Manager|CodeWhisperer|"
    r"Glue Elastic Views"
)

RISK_CAVEATS = re.compile(
    r"legacy|no longer|out[- ]of[- ]scope|full shutdown|sunset|caveat|"
    r"former|renamed|historical|do not|deprecated|discontinued|EOL|"
    r"not current|replacement|instead|prefer|avoid|maintenance|no new|"
    r"current name|Classic is|rather than",
    re.IGNORECASE,
)


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :]


def scalar_value(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*\"?([^\"\n]+)\"?\s*$", frontmatter, re.MULTILINE)
    return match.group(1).strip() if match else None


def list_values(frontmatter: str, key: str) -> list[str]:
    lines = frontmatter.splitlines()
    values: list[str] = []
    in_block = False
    for line in lines:
        if line == f"{key}:":
            in_block = True
            continue
        if in_block:
            if line.startswith("  - "):
                values.append(line.strip()[2:].strip().strip('"'))
                continue
            if line and not line.startswith(" "):
                break
    return values


def missing_canonical_sections(text: str) -> list[str]:
    missing: list[str] = []
    for preferred, accepted in CANONICAL_SECTION_GROUPS:
        if not any(section in text for section in accepted):
            missing.append(preferred)
    return missing


def validate_file(path: Path, strict_sections: bool) -> tuple[list[str], list[str], str | None]:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []
    frontmatter, body = split_frontmatter(text)

    if frontmatter is None:
        errors.append(f"{rel}: missing or unterminated frontmatter")
        return errors, warnings, None

    for key in REQUIRED_FRONTMATTER_KEYS:
        if not re.search(rf"^{re.escape(key)}:", frontmatter, re.MULTILINE):
            errors.append(f"{rel}: missing frontmatter key `{key}`")

    if re.search(r"^exam:", frontmatter, re.MULTILINE):
        errors.append(f"{rel}: legacy frontmatter key `exam`; use `scope` and optional `certifications`")

    scope = scalar_value(frontmatter, "scope")
    if scope and scope != EXPECTED_SCOPE:
        errors.append(f"{rel}: invalid scope `{scope}`")

    status = scalar_value(frontmatter, "status")
    if status not in ALLOWED_STATUSES:
        errors.append(f"{rel}: invalid status `{status}`")

    tags = list_values(frontmatter, "tags")
    duplicates = sorted({tag for tag in tags if tags.count(tag) > 1})
    if duplicates:
        errors.append(f"{rel}: duplicate tags {duplicates}")

    if not body.lstrip("\n").startswith("# "):
        errors.append(f"{rel}: first body line after frontmatter must be an H1")

    if not SOURCE_SECTION.search(text):
        errors.append(f"{rel}: missing Sources, References, or Additional Resources section")

    if rel.name not in {"README.md", "PLAN_NOTES_IMPROVEMENT.md"} and (
        "needs-verification" in text or re.search(r"\b(TODO|FIXME|TBD)\b", text)
    ):
        errors.append(f"{rel}: unresolved verification or todo marker")

    if rel.name not in {"README.md", "PLAN_NOTES_IMPROVEMENT.md"} and status not in {
        "legacy",
        "out-of-scope",
        "supplemental",
    }:
        for number, line in enumerate(text.splitlines(), 1):
            if RISK_TERMS.search(line) and not RISK_CAVEATS.search(line):
                errors.append(f"{rel}:{number}: uncaveated stale/lifecycle term: {line}")

    if rel.name not in CONTENT_EXCLUDES:
        missing_sections = missing_canonical_sections(text)
        if missing_sections:
            message = f"{rel}: missing canonical sections: {', '.join(missing_sections)}"
            if strict_sections:
                errors.append(message)
            else:
                warnings.append(message)

    return errors, warnings, status


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AWS ML/AI note structure and lifecycle caveats.")
    parser.add_argument(
        "--strict-sections",
        action="store_true",
        help="Fail when content notes do not use every canonical NOTE_TEMPLATE section group.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    status_counts: Counter[str] = Counter()

    files = markdown_files()
    for path in files:
        file_errors, file_warnings, status = validate_file(path, args.strict_sections)
        errors.extend(file_errors)
        warnings.extend(file_warnings)
        if status:
            status_counts[status] += 1

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        if warnings and not args.strict_sections:
            print(f"\nWarnings: {len(warnings)} canonical section gaps remain.", file=sys.stderr)
        return 1

    print(f"Validated {len(files)} markdown files.")
    print("Status counts:")
    for status, count in sorted(status_counts.items()):
        print(f"- {status}: {count}")

    if warnings:
        print(f"Canonical section warnings: {len(warnings)} files are not fully migrated.")
        print("Run with --strict-sections to make these warnings fail validation.")
    else:
        print("Canonical section coverage: complete.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
