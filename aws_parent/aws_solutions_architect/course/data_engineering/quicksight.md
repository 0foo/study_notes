* serverless BI (business intelligence) service 
* BI means create dashboards

* cloud native (fast, scalable, etc)

* integrated with many many data sources in AWS, on-prem(JDBC), and 3rd party (JIRA, salesforce, etc)
* can import items directly into quicksight
    * use the SPICE engine 

* SPICE engine
    * in memory computation engine
    * only work's if you IMPORT the data into quicksite


* in enterprise level of quicksight
    * can setup column level security to restrict access 


#### Dashboard/Analuysis

* define users and groups IN QUICKSITE
    * not within IAM

* Dataset
  * Connect to data source (S3, Athena, RDS, etc.)
  * Prepare dataset (joins, filters, calculated fields)

* Analysis
  * Create analysis as a workspace
  * Add visualizations (charts, tables, KPIs)
  * Apply filters, parameters, interactions

* Dashboard
  * Publish analysis as a dashboard
  * Dashboard is read-only and interactive
  * Users can filter and explore, but not edit visuals
  * read only version of the analysis 



