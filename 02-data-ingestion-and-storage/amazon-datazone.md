# Amazon DataZone

- Managed data governance and sharing service that creates a business data portal for publishing, discovering, and subscribing to governed data assets.
- Core building blocks:
  - **Domains**: administrative boundaries with their own administrators, glossary, and approval policies.
  - **Projects**: workspaces for producer or consumer teams; used to publish assets to the catalog or request subscriptions.
  - **Catalog**: indexed metadata with search, business glossary terms, and tags to aid discovery.
  - **Data products/assets**: registered sources such as S3/Lake Formation tables, Redshift databases/tables, and other cataloged resources.
- Access management and governance:
  - Producers register data assets into a domain and define subscription terms; consumers submit subscription requests that follow domain-defined approval workflows.
  - Enforces fine-grained access via Lake Formation (for S3/Glue catalogs) or Redshift permissions after a request is approved.
  - Integrates with IAM Identity Center for SSO to the data portal and with centralized policies/glossary terms to enforce consistent governance.
- Typical uses: enable self-service discovery of curated datasets across accounts, provide auditable approval flows for data access, and maintain a consistent business glossary and metadata for analytics and ML teams.
