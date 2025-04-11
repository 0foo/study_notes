### Application Discovery Services
* gather info about on prem for migration planning
* server utilization data and dependency mapping are important for migrations
* two kinds of discovery
    1. agentless discovery  
        * OVA vmware package to be deployed on prem
        * does inventory on all the virtual machines, performance, config
        * OS agnostic
    2. agent based discovery
        * gather system config, performance,process, and details of network connections between systems
        * install an agent on the OS
* can track the migration 
    * data can be viewed in AWS migration hub, Athena/QuickSight, CSV
    * data is automatically stored in S3 at regular intervales


### AWS Application Migration Service (MGN)
* The AWS evolution of: CloudEndure Migration combined with AWS Server Migration Service (SMS)
* Lift and Shift to simplify migrating app's to AWS
* convert physical, virtual, and cloud based servers to run natively on AWS 
* agent based
    * essneitally install an agent on your on prem host that will stream at a BLOCK LEVEL to EBS and replicate all of your systems
    * this is done live on production hosts
    * this is CONTINUOUS STREAMING on production hosts
    * drivers may be injected and other host specific modifications may happen
    * this replicated environment is built in a lightweight staging environment in AWS for testing and validation
    * cutover: when you're ready you can launch a fully replicated prod instance based on this validated instance



### Elastic Disaster Recovery (DRS)
    * used to be called cloudendure disaster recovery
    * similar to MGN in that there's continuous block level replication for on prem hosts into the cloud EBS
    * same technology agent as MGN
    * can do a failover to cloud if needed while restoring/fixing on prem environment


### DMS database migration service

* quickly migrate databases to AWS

* source DB remains avail during migration!

* cdc - change data capture
    * CDC replication tracks and replicates ongoing changes in the source database.
    * Inserts, updates, and deletes are captured after the initial load.
    * Used when you want to:
    * Keep source and target in sync during migration.
    * Minimize downtime by cutting over after CDC catches up.
    * AWS DMS supports CDC via transaction logs (e.g., MySQL binlog, Oracle redo logs, SQL Server transaction logs).
    * Can run CDC only, or in combo:
    * Full load + CDC = full dump first, then sync live changes.

* supports:
    * homogenous migration: same database engine to same database engine(mysql to mysql)
    * heterogenous migration: different databases(mysql to oracle)

* can do continuous replication using CDC 
    * will need an EC2 instance created to perform the replication task
    * source DB -> EC2 instance with DMS -> destination DB

* redshift, kinesis, opensearch service are DESTINATION ONLY for DMS cannot use them as source DBS
    * cannot be a source for DMS DATA!! 

* source db examples: any relational, s3, mongo, oracle, SAP, and many more
    * CDC replication tracks and replicates ongoing changes in the source database.
    * Inserts, updates, and deletes are captured after the initial load.
    * Used when you want to:
    * Keep source and target in sync during migration.
    * Minimize downtime by cutting over after CDC catches up.
    * AWS DMS supports CDC via transaction logs (e.g., MySQL binlog, Oracle redo logs, SQL Server transaction logs).
    * Can run CDC only, or in combo:
    * Full load + CDC = full dump first, then sync live changes.

* SCT: Schema conversion tool
    * convert one schema to another
    * EXample: 
        * OLTP: between two sql databases
        * OLAP: from some SQL database to redshift
    * dont need SCT if using the same database engine


* Can integrate snowball and DMS
    * large data migrations may have TB to PB of data
    * Steps:
        1. use AWS SCT to extract data locally and move to an snowball edge device
        2. ship back to AWS
        3. AWS will load data into s3 
        4. DMS kicks in, takes the files from S3 and moves them to target data store
    * if use CDC (change data capture) any updates happening in on prem data source will be replicated over to the destination data store

