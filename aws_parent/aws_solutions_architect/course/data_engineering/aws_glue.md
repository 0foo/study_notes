* managede ETL service 
* prepare/transform data for data analytics 
* fully serverless


* datasource like s3 or RDS or something -> GLUE (extract/transform -> load it into some other data source like redshift or something



#### Glue catalog
* Centralized Metadata Storage
  * Stores table definitions, schema, and data location info (e.g., S3)
* Data Discovery
  * Crawlers can scan data sources and automatically populate metadata
* Query Engine Integration
  * Used by Athena, Redshift Spectrum, EMR, and Glue jobs for querying data
* Schema Versioning
  * Tracks and manages changes to data schema over time
* Access Control
  * Works with Lake Formation and IAM for managing access to metadata and data

