* EXAM TIP: anytime need to analyze data in s3 using serverless SQL use Athena

* serverless query service to analyze data stored in S3
* uses standard SQL language to query the files (build on Presto)



* supports CSV, JSON, ORC, Avro, Parquet

*  pricing: 5$ per TB of data scanned


* typically used with QuickSight to create dashbaords/reporting

* use cases: business intelligence(analytics, reporting), analyze/query logs (VPC flow, ELB, cloudtrails, etc)



#### Performance improvements

* use a columnar datatype, only scan the columns you need
    * two data formats that do this are Apache Parquet and ORC
    * huge performance improvment
    * use Glue to convert data as an ETL jobe between CSV and Parquet

* compress data for smaller retrieval

* partition datasets in S3 for easier querying on virtual columns
    * divide up into folders inside of S3 as a single partition
    * that way when you do a query on Athena you can pass in the folder that the dataset is in 
    * will not have to search through entire dataset


* user larger files to minimize the overhead better than many smaller files
    * larger files easier to scan/retrieve



#### Federated query
* can query not only S3 but many other sources!!!
* can query relational, non-relational, object and custom datasources (aws or on-prem)
* use a data source connection that is a LAMBDA function to run federated queries
    * cloudwatch logs, dynamo, RDS, document_db, elasticache, redshift, Aurora,  SQL server, EMR etc.
* one lambda function per data source connector
* CAN DO SQL QUERIES ACROSS NUMEROUS DATA SOURCES
    * i.e. can run a join between mongo and RDS