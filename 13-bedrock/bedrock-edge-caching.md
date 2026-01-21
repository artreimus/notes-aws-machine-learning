# Caching for GenAI Workloads: CloudFront + API Gateway (Bedrock Context)

## Why This Matters for GenAI
- GenAI responses can be expensive and latency-sensitive.
- Traditional caching (exact-match) can still help for repeated prompts, shared static context, and non-personalized outputs.
- Caching is most effective when outputs are deterministic and reused frequently.

## CloudFront Caching (Edge)
### What It Does
- Caches HTTP responses at edge locations to reduce origin load and improve latency.
- Uses a **cache key** plus **TTL** settings to determine cache hits.

### Key Controls
- Cache policy
  - Defines what goes into the cache key (headers, cookies, query strings).
  - Controls TTLs (min, default, max).
- Origin request policy
  - Lets you forward headers/cookies/query strings to origin without including them in the cache key.

### GenAI-Specific Guidance
- Use CloudFront for:
  - Static UI assets for GenAI apps.
  - Reusable prompt templates or public, non-personalized content.
  - Canned responses or FAQ outputs where exact-match caching is safe.
- Avoid caching:
  - Personalized responses unless you include user-specific keys in the cache key.
  - Sensitive responses that should not be served cross-user.
- Keep cache keys minimal to maximize hit rate, but include any request fields that change the response.

## API Gateway Caching (REST APIs)
### What It Does
- API Gateway can cache responses at the **stage** for REST APIs.
- Cache entries are keyed by selected request parameters (headers, query strings, path params).

### Key Controls
- Stage-level cache
  - Enable caching and set TTL (default 300s, max 3600s; 0 disables cache).
- Cache key parameters
  - Define which request parameters differentiate cache entries.
- Invalidation
  - Flush stage cache or invalidate specific keys when needed.

### GenAI-Specific Guidance
- Use API Gateway caching for:
  - Frequently repeated prompts with identical inputs.
  - Non-personalized summaries or metadata responses.
  - Expensive deterministic calls where exact-match caching is acceptable.
- Avoid caching:
  - Highly personalized or user-specific responses unless the cache key includes user identifiers.
  - Streaming responses that are not compatible with simple response caching.
- Consider adding a dedicated semantic cache (outside API Gateway) if you need similarity-based caching.

## Practical Design Tips
- Treat caching as a cost/latency lever, not a quality lever.
- Use short TTLs for volatile data.
- Include user identity or tenant ID in cache keys for any personalized responses.
- Pair with guardrails and PII controls; cache only what is safe to reuse.

## Exam Tips
- CloudFront caching is edge-based and controlled by cache policies and TTLs.
- API Gateway caching is stage-based for REST APIs and uses cache key parameters.
- Both are exact-match caches; they do not provide semantic similarity caching.

## Sources
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-key-understand-cache-policy.html
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-the-cache-key.html
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html
- https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html
- https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html
