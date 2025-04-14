* Redshift based on PostGresQL but not used for OLTP
* Redshift is OLAP
* analytics and data warehousing
* 10x better performance than other data warehouses
* scale to petabytes
* data stored as a column NOT a row
    * essentially means the "array" is the column
    * so to get a row would need the index of each item
    * chatGPT it to explain better
* massively parrallel query execution
    * makes it very fast
* is a managed service so get: 
    * backup/restore for redshift
    * Security: VPC, IAM, KMS
    * Monitoring

 
#### 2 modes
* provisioned cluster
    * on demand servers you provision yourself
* serverless cluster
    * if dont want to manage servers


* SQL interface for queries
* can connect Tableau or Quicksight to build dashboards
    * redshift is very fast so dashboard is very responsive



#### how to load data
    * load from S3, Kinesis Firehose, dynamo, DMS


#### Capacity
* up to 100+ nodes
* each node has 16 TB per node
* single AZ for most redshift clusters vut for some can do mult region for failover


#### node types
* leader node - query planning, results aggregatioan
* compute node: performs the computation and send results to leader

#### Use cases
* if queries are sporadic use Athena instad, much more cost efficient
* Only worth it if you sustained usage

#### DR and Restore
* Snapshots are point in time and stored in s3

* Must restore a snapshot into a new cluster

* automated snapshots
    * set a retention policy 30 days is default
    * Snapshots are incremental diffs
    * can automate snapshots
        * every 8 hours or 5 gigs of data is default
        * can change this
* manual snapshots
    * retained until manually deleted

* can configure redshift to copy snapshot of a cluster to another region
    * good for disaster recovery 
    * restore into another region
    * Important note:  
        * each region has separate KMS key
        * will need to create a 'snapshot copy grant' in the destination region to allow redshift to use other KSM key



#### Redshift spectrum
* Redshift Spectrum spins up new nodes to process S3 data in parallel
* It scales compute separately from your Redshift cluster
* This makes it efficient for querying large external datasets

* Redshift Spectrum is designed to query S3 data (e.g., Parquet, CSV) using SQL
* It uses a **separate fleet of EC2-based compute nodes** (called Spectrum nodes)
* When you run a query:
  * Redshift dispatches part of the query to Spectrum
  * Spectrum spins up as many nodes as needed based on:
    * Query complexity
    * Data size
    * Concurrency

* These Spectrum nodes:
  * Scan and filter S3 data
  * Return the results to your Redshift cluster for final joins/aggregation (if needed)

* This design allows:
  * Querying massive S3 datasets without overloading your Redshift cluster
  * Elastic scaling of compute — you only pay per query and data scanned


#### Redshift Workload Management
* 
* separates queries into a set of priority queues
* can put high priority jobs in one queue medium priority in another low in another
* good for things like sysadmin high priority jobs and short running jobs not being held up by long running
* automatic WLM
    * queues managed by AWS
* managed WLM
    * queues managed by user


#### Concurrency scaling
* enables you to provide consistently fast performance with irtually unlimited concurrent users and queries
* redshift adds additional cluster capacity on the fly (concurrency scaling  to process an increase in requests
* charged per second!!