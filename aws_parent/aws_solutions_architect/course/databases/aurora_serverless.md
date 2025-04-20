* automated database instantiation and auto-scaling based on actual usage
* good for unpredictable workloads
* no capacity planning needed
* pay per second, can be more cost effective

####  aurora serverless - Data API
* access with a simple API endpoint, no JDBC needed
* HTTPS endpoint that allows you run SQL statements
* no persistent database connection management
* users must be granted permissions to Data API and Secrets Manager(where permissions are checked)

* the Data Api layer requests credentials from secrets manager which are used to make calls to database
    * The user/role that calls aurora api passes their creds in the http header as a signature
    * Checks the role then processes the request which checks the secrets ARN that stores the DB creds
    * the DB creds are then pulled from secrets manager which are then used for authenticationauthorization inside the database

#### RDS proxy for aurora
* can use an RDS proxy to manage DB connections with aurora just like with RDS
* lambdas can scale and use this proxy
* can create additiona RDS proxy for aurora to create an endpoint for read only replicas


#### Global aurora
* define a primary region which takes reads/writes
* up to 5 secondary read only regions
* replication lag over to these regions is less than 1 seconds
* up to 16 read replicas per secondary region
* having global read only regions helps alot with reducing latency (i.e. ghetto edge)
* promoting another region for disaster recovery has RTO of < 1 minute
* ability to manager the RPO in aurora for postgres, can set backup times
* write forwarding
    * enables secondary DB clusters that are read only to forward writes to primary cluster
* note: even with write forwarding the data has to go to primary cluster first, then replicated to the secondarys
    * primary database is the only one with always up to date data


#### Convert RDS to Aurora
* take a snapshot of RDS, store to s3, then simply go into RDS snapshot restore and select 'restore to aurora'
    * aurora will handle the conversion for you
    * requires taking the RDS DB down or missing some data
* can also create a read replica of an RDS DB in Aurora
    * when replication lag is 

