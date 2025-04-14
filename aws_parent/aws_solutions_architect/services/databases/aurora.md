* AWS implementation of postgres/mysql with cloud native additions
* Postgres or MySql

* automatically grows in size when needed up to 128 TB: storage is managed
* 6 copys of data made by default across 3 AZ's
* multi AZ by default
* up to 15 read replicas 
* get a reader endpoint that you can use that will handle distribution of load to read replicas
* cross region Read Replica
    * entire database is copied
* easy ability to export/import data from/to s3
    * no client application needed, is built in, no network costs
* backups,snapshots and restore, same as RDS
* replication + self healing + autoexpanding


#### Replicas
* up to 15 read replicas
* can specify what size when you create them



#### Multi AZ clustedr
* 6 copys of data made by default across 3 AZ's
* 4 of the 6 are needed for writes
* 3 out of the 6 are needed for reads
* self healing with peer to peer replication
* storage is striped across 100's of volumes
* failover for master happens in less than 30 seconds
* master is only node that can write to storage
* master + up to 15 read replicas to serve the reads(15 total across all AZ's)
* If you are using an Aurora Global Database, writes to the primary cluster (master) in one region are replicated to other regions. This setup allows near real-time replication with minimal latency.
* If the primary region experiences an outage, one of the secondary regions can be promoted as the primary to maintain availability.

#### 
* client -> write endpoint -> master database on autoexpanding storage
* read replicas -> read endpoint -> read from master db

#### endpoint
* endpoint = ip + port
* cluster endpoing = writer endpoint 
    * leads to primary instance in cluster
    * used for write ops
* reader endpoint = read endpoing
    * load balancing for all read only connections to all auroroa replicas in the cluster
* custom endpoints
    * sets of DB instance you choose in the cluster
    * connect to different subsets with different capacities and configurations
* instance endpoint
    * connect to a specific instance in the cluster


#### Aurora logs/monitoroing
* error log
* slow query log
* general log
* audit log

* downloaded from aurora
* published to cloudwatch logs

* cloudwatch metrics
* enhanced metrics


#### Troubleshooting
* use performance insights tool in Aurora
    * find issues by waits, sql statements, hosts and users
* cloudwatch logs
* cloudwatch monitoring
* slow query log

