#### compare warehousing technologys


* EMR - big data tools such as apache hive or spark and migrate to AWS
    * long running cluster with many jobs with auto-scaling
    * one cluster per job - size each job/cluster independantly
    * purchasing options - on demand, reserved, spot
    * can access data in:
        * dynamo 
        * S3
    * can save data:
        * scrach data in EBS(HDFS)
        * long term data in S3 (EMRFS)


* Athena
    * simple queries and aggregations
    * data must live in S3
    * serverless simple SQL queries 
    * out of the box queries for many services
    * audit all queries through cloudtrail

* Redshift
    * advanced SQL queries
    * must provision servers
    * Redshift spectrum for serverless queries on S3
    * 