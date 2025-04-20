* know the engines it offers

* postgres SQL
* MySQL
* Maria DB
* IBM DB2
* Oracle
* SQL server


* managed database (see concepts.md for what that means)

* launched in a VPC in private subnet
* use security groups to manage access

* any resource that wants to access must be in the subnet or able to reach the subnet
    * important with lambda as that lambda will need to be spun up inside of the subnet

* backed by EBS so it will expand out to any size needed

* RDS publishes events
    * get notified by SNS for events(operations, outages, when backups starting, etc.)

* multi AZ 

* standby instance
    * standby instance for failover in case of outage
    * these replicas can be on one or more AZ'a
    * one DNS name to access the database 
        * in event of failover RDS will update the IP associated to DNS to the standby instance
    * During the failover process, connections to the database are temporarily disrupted. 
    * failover usually takes 1 to 2 minutes
    * note: the standby instance is purely for backup, application never uses it for performance increases

* read replicas
    * used for performance increases
    * can manually promote a read replica to the master if needed
    * can be cross region
    * async replication---eventual consistency


* distribute (read) load to read replicas
    * route 53 can create a weighted record set
    * set the weight of each ip that will be used as a percentage 
    * i.e. return 4 values with 25% weight each and each will get 25% of the load
    * enable health checks in route 53 and if an instance has issues will be excluded from the DNS record

#### Security
* KMS encryption for database and snapshots
* transparent data encryption for Oracle and SQL server
* SSL encryption for over the wire 
* authorization still happens within RDS database not IAM

* IAM auth 
    * works with: postgres, mysql, mariaDB
    * get auth token from IAM 
    * token has 15 minute lifetime
    * allows centralized user management with IAM
    * can use IAM Roles and EC2 instance profiles to access database
    * in the configuration of the IAM role add a database user
    * this database user is what's used inside of RDS database to manage authorization

#### Monitoring
* cloudtrail cannot track queries made withing RDS)


#### RDS for Oracle
* two ways of backups
    1. RDS backups - 
        * can backup to RDS or Oracle and 
        * can only be restored to an RDS database instance
    2. Oracle RMAN - (recovery manager) 
        * backup and restore to non-RDS
        * backups to s3 where it can only be restored to external Oracle DB
* RAC-real application clusters
    * it's an Oracle feature
    * RDS does NOT support this
    * only works on EC2 instances you have control over

* TDE (transparent data encryption)
    * encrypt data before it's written to storage and as its called from storage
    * Applications do not need to be modified to use TDE, as encryption and decryption occur automatically at the database level.
    * When data is written to disk, it is encrypted automatically
    * When data is read from disk, it is decrypted automatically and provided in plaintext to authorized users.
* DMS works on Oracle RDS



#### RDS for mysql
* can use the `mysqldump` tool to migrate a MYSQL RDS DB to non-RDS
* the external MySQL database can run outside of RDS
    * on prem, ec2, etc.
* `mysqldump` does both the export and the import



#### RDS proxy for AWS Lambda
* when use Lambda with RDS it will open and maintain a database connection
* if many concurrent functions may encounter a 'tooManyConnections' error
* if use RDS proxy no longer need code that handles:
    * cleaning up idle connections 
    * managing connection pools

* RDS proxy support IAM auth, or DB auth
* auto scaling

* must ensure lambda can reach the proxy
    * i.e. public proxy + public lambda
    * private proxy + lambda in same VPC

