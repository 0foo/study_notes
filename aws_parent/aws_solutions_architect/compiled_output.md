
# service_communication

## MQ.md
* SQS, SNS are "cloud native", propietary AWS services
* if have an on prem solution may be using an open protocol 
* if migrating from on prem to cloud may want to keep using your open protocol
* MQ is a managed message broker service for two open protocols
    * rabbit MQ
    * active MQ
* doesn't scale as much as SQS/SNS
* has to run on managed service, run in Multi AZ with failover in case of issues for High Avail
* Amazon MQ has both a queue feature and a topic feature
    * Queues: For point-to-point communication (P2P).
    * Topics: For publish/subscribe (pub/sub) communication
    * see below

* migration
    * there are systems in place to migrate from one MQ broker protocol to Amazon MQ
    * example: IBM MQ, TIBCO, Rabbit MQ, Apache ActiveMQ, etc.







* REFERENCE: 
    * Queue
        * Producers send messages to a queue.
        * A single consumer receives and processes each message.
        * Messages are removed from the queue once delivered and acknowledged.
    * Topics
        * Producers send messages to a topic.
        * All subscribers to the topic receive a copy of the message.
        * Subscribers can filter messages based on conditions or routing keys (depending on the protocol).
    * NOTE:
        * amazon SQS is queue
        * amazon SNS is topic
# service_communication

## SNS.md
* send one message and have many different recievers
* pub/sub
* SQS is queue wheras SNS is topic

* TOPIC: a service publish a message to a SNS topic which has many subscribers that all get that topic

* The event producer only sends messages to one topic
* The event listeners all subscribe to the topic
* The listeners get ALL events pushed to the topic(unless using a specific feature)


* not tested on limits for SNS just an idea
    * 12 million plus subscriptions per topic
    * soft limit of 100,000 topics


#### Subscriber potential
* have subscriber functionality built in to send to:
    * email
    * SMS
    * HTTP endpoints
* integrations with AWS services
    * SQS queue
    * lambda to do something with
    * kinesis firehose -> s3 or redshift


#### Publisher potential
* recieves data from a lot of AWS services(don't have to remember these)
    * cloudwatch alarm
    * AWS budgets
    * ASG notifications
    * etc.

#### How to publish
* Topic Publish
    * create a topic 
    * subscribers subscribe
    * publish to topic and all subscribers will get

* Direct Publish (mobile app SDK)
    * create platform application
    * create platform endpoint
    * publish to platform endpoint
    * can push to many platforms (google GCM, Apple APNS, etc) 
    * totally for mobile

#### Security
* in flight encryption by default
* at rest with KMS keys
* Access: IAM policies regulate access to SNS Api with SNS access policies



#### SNS plus SQS fan out pattern
* want a message to be sent to multiple sqs queues
* can send message once to SNS topic
    * SQS queues will be subscribed to this topic 
    * will all get a copy of the message in their queues
* make sure SQS queue access policy allows SNS to write
* works cross region

* examples
    * S3 events to multiple queues
        * can only have a single event per event type 
        * so send that event to SNS which can fan out to multiple SQS queues
        * i.e. to have different types of processing on the item, create thumbnail, store metadata to a dynamo table, etc.
    * SNS to S3 through Kinesis data firehose(kdf)
        * SNS can send message to Kinesis 
        * KDF can then get the data to S3 or anyother KDF supported location
        * give a lot of options for how to persist that message


* FIFO topics/queues
    * if want fanout but with ordering, and deduplication use FIFO topics and FIFO queues
    * ordering given to messages in the topic
    * limited throughput (same as SQS fifo)


* message filtering in SNS
    * if subscription has no filtering policy the subscriber will recieve every message
    * JSON policy used to filter incoming messages
    * compares data in the message with the filtering policy and only accepts the message if meets critera



#### Message delivery retries and DLQ
* if SNS delivers to an destination and it fails there's a preset delivery retry policy/complicated logic for backoff/retry
* retries a number of times over a period of time to continue to deliver message
* only HTTP endpoints can be custom retry policies
    * can specify a number of factors for retrying
        * i.e. number of retries, delay between retry, backoff function,  etc. etc.

* If delivery policy fails message is discarded unless set a DLQ
    * SQS queue attached to a subscription NOT a topic
    * you setup a DLQ per subscription
# service_communication

## SQS.md
* serverless managed queue, no need to provision anything
* extreme scale

* used to decouple services
* max message size 256KB
* if need larger size, upload the larger file to s3, then add a pointer in the SQS message that consumer can read

#### Consumer
* EC2 with autoscale
* Lambda
* use as write buffer to dynamo db
    * may have write provisioned to a certain amount in dynamo
    * so can buffer in SQS and only feed to dynamo at certain speed
    * avoids dynamo throttle 


#### Type
* FIFO - 
    * processed in order recieved
    * Limited Scale: 300 message/s with no batching, 3000 messages/s with batching
* 


#### Deadletter Queue
* if consumer fails to process a message
    * message goes back into the queue
    * maintains a fail count
    * when hits a certain number of fails(threshold), will send to Dead Letter Queue
* DLQ: useful for debugging
* DLQ of a FIFO queue must also be a FIFO queue
* DLQ of standard queue must also be a standard queue
* DLQ has retention time, so can set a time to retain DLQ messages at which point they are lost
    * good to set this to longer times

* redrive to source
    * after inspecting a DLQ message and figuring out and fixing what's wrong
    * can redrive the DLQ message back to it's original source (native feature in SQS no additional code needed)

#### Idempotency
* messages can be processed twice by consumers
* need to make sure that consumers won't duplicate the effect if process additional time
* the responsibility of ensuring messages aren't duplicated falls on CONSUMER as SQS may duplicate messages
* consumers can do a hash of a part of the data and upsert into db with hash as key
    * that way will update the data if it's a duplicate


#### Event source mapping
* Event Source Mapping in the context of Amazon SQS refers to the process by which AWS services, such as AWS Lambda, automatically poll and consume messages from an SQS queue without requiring you to write or manage the polling logic yourself.
* Messages from the SQS queue are batched and sent to the configured Lambda function for processing.
* Lambda scales automatically with the rate of incoming messages in the queue.
* The number of concurrent Lambda invocations adjusts based on the batch size and the processing rate of the function.
    * define a batch size and lambda will pull that many from the queue
    * if theres more than that batch size in the queue more lambdas will be created to handle them
* queue visibility timeout should be 6x the timeout of your lambda function(reccomended via aws docs)
    * maybe explain this more with GPT
* DLQ is possible


#### Architecture ideas
* can separate clien and server by a request queue and a response queue
    * completely decouples, fault tolerance, load balancing
# service_communication

## step_functions.md
* workflow orchestration
* have deep integration with numerous other services
* represent flow as json state machine
* integrate with TONS of aws services

#### Trigger 
* management console
* AWS SDK
* cli
* AWS lambda (startExecution API call via SDK)
* API gateway
* Event Bridge
* Code Pipeline
* other stepfunctions



#### Tasks
* lambda task: invoke lambda function
* activity task
    * set up an http activity worker
    * activity worker will poll the step function service and see if there's something for it to do
    * After receiving a task, the worker processes it and sends the result back using the SendTaskSuccess, SendTaskFailure, or SendTaskHeartbeat APIs.
* service tasks
    * connect to a supported AWS service
    * i.e. lambda, ECS, Fargate, Dynamo, etc.
* wait task
    * wait for a duration

* very common exam question: DOES NOT INTEGRATE WITH MECHANICAL TURK
    * have to use ASWF instead of step functions


#### Workflows
* two types: standar and express

* Express: fast, high throughput workloads, cheaper, with short duration
* Standard: longer, slower, more reliable/durable, with longer potential duration

* Two types of Express workflow
    1. Syncronous
        * client wait until workflow completes then return result
        * i.e. api gateway calling a sync workflow, waiting, returning response to client
    2. Asyncronous
        * client don't wait for workflow for comlete, just send and forget
        * i.e. promises
        * used if client doesn't need immediate response/result
        * i.e. api gateway kicks off a workflow and doesn't wait for completion

* Don't have to know the following, just here for reference
    * Execution Duration:
    * Standard: Up to 1 year.
    * Express: Up to 5 minutes.

    * Execution Volume:
    * Standard: Designed for low to moderate execution volumes (e.g., workflows with critical state tracking and retries).
    * Express: Designed for high-volume workloads (e.g., millions of executions per second, like event-driven applications).

    * Pricing Model:
    * Standard: Charges per state transition.
    * Express: Price on number of executions,  duration of executions, and memory consumption (is cheaper)

    * Performance and Scalability:
    * Standard: Scales for moderate concurrency with exact-once execution.
    * Express: Scales for extremely high concurrency with at-least-once execution (potential for duplicate processing).

    * State Durability:
    * Standard: Each state is durably persisted, making it more suitable for workflows requiring high reliability.
    * Express: Optimized for speed, so state is not durably persisted between steps.

#### Error handling
* enable error handling, retries, and add alerting to Step Function State Machine
* best practice: setup eventbridge to alert via email if statemachine function fails

* can add retry blocks
# data_engineering

## timestream.md
#### managed cloud tier
* time series database
    * data with time included
    * faster/cheaper the relational DB for data with time values
* fully managed, highly available, auto scaling up/down, replicated across three AZ
* store/analyze trillions of events per day



# data_engineering

## document_db.md
* essentially an AWS implementation of mongdb with cloud native add ons
* mongo is used to store, query, and index, JSON data 
* very similar in every way to auroroa but for mongo
* scales to workloads of millions of RPS


#### Pricing
* pay for what you use/ no upfront costs
* on demand database instances which house the application: i.e. primary, replica
    * pay for these by the second
* pay for database I/O between application tier and storage tier per million I/O
* pay for database storage tier in GB/month
* pay for backup storage in GB/month

#### managed/cloud native
* fully managed, highly available, auto scaling, replicated across three AZ
* grows in increments of 10GB 


# data_engineering

## aws_batch.md
* run batch jobs as docker images
* two ways:
    1. run on fargate, serverless
    2. dynamic provisioning of the instance in your VPC

* optimal quantity and type based on volume and requirements
* no need to manage clusters/ fully serverless
* batch processes of images running thousands of concurrent jobs
* Schedule batch jobs using Amazon Eventbridge
* orchestrate using AWS Step functions


* Architecture
1. s3 trigger event bridge  
2. event bridge trigger AWS batch
3. batch job invoked (fargate/docker, ec2, spot instance)
4. fargate/docker will pull image from ECR and instantiate containers
5. batch jobs may need to retrieve data from s3 for the job 
6. can send the final product to s3 and maybe insert metadata into dynamo



#### Batch vs Lambda
* Lambda
    * time limit
    * space limit
    * limit on what runtimes can use

* batch
    * no time limit
    * any runtime as long as packaged in a docker image
    * rely on EBS/instance store for disk space
    * relies on EC2 or AWS Fargate

#### Managed batch environment
* AWS manages capacity and instance types
* can choose on demand or spot
* set max price for spot
* all the instances launced within own VPC
    * needs access to ECS
    * will need a NAT gateway or NAT instance  or using VPC endpoint for ECS
* set min/max vCPU
    * note this will launch all different types of spot instances as they're available
    * all that matters is the vCPU
* can setup autoscaling to expand/contract spot instance count in response to increase/decrease in jobs


#### Batch job queue 
* how batch jobs distribute jobs to instances
* send job to job queue in a number of ways
    * SDK
    * Lambda
    * Clouwatch events
    * Step function
    * etc.


#### Multinode mode
* Most important:
    * does not work with spot instances
    * works better if EC2 launch mode is in a placement group "cluster" to get the enhanced networkgin
        * means everything is on same rack within same AZ
* Other:
    * good for HPC
    * leverage multiple EC2/ECS instances at the same time to run your job
    * you specify how many
    * good for when you have tightly coupled workloads
    * 1 main node and many child nodes
    * main node will launch and then launch/manage other nodes
    * all nodes run the job, then shutdown


#### Unmanaged batch environment
* you control and manage instance config, provisioning, and scaling

# data_engineering

## kinesis_streams.md
#### Major rundown
* key words: REALTIME DATA 
* real time streaming
    * lots of user sending clicks in from website
    * logs
    * IoT devices
* data processing time is under 200ms
* data stays in system from 1 to 365 days 
* data is STORED there until it expires
* data is immutable once in the stream
* Requires you to write and deploy producers/consumers to move data to storage or analytics systems.
* kinesis takes data up to a max of 1MB 
    * SQS data size max is around 256 KB
    * alot of small data
* data is sent with a partition KEY which tells which shard to send the data to
    * this data is ORDERED per shard
* streams divided up into shards 
    * Streams can scale by adding or removing shards.

* security: at rest(KMS), in flight(HTTPS)

* You write data to a stream endpoint, amd specify the data and a partition key in the payload.
    * Kinesis uses the partition key to determine which shard in the stream that the data will be routed to.

#### Producer
* just the device/application that generates the data and sends it into Kinesis
* producers:
    * AWS SDK: simple producer
    * Kinesis PRODUCER Library(KPL)
        * batch, compression, retries, C++, Java
        * library for C++/java
        * for your own application
    * Kinesis agent (built with KPL)
        * installed on hosts and run to monitor log files and send to Kinesis directly
        * can write to either KDStreams or KDFirehose

#### Consumer
* the applications utilizing the data in real time
* custom application, lambda function, firehose, storage, analytics, etc.
* Multiple consumers can consume the data(different from SQS which one consumer removes post from queue)
* consumers:
    * AWS SDK: simple consumer
    * Lambda (through even source mapping)
    * Kinesis CLIENT Library(KCL)
        * read in parallel from kinesis stream
        * checkpointing, co-ordinated reads across multiple ec2 instances
        * can spin up multiple EC2 instances which all claim part of the work in each shard by setting up checkpoint claims in dynamo
    * Kinesis Firehose
    
* When you access data from an Amazon Kinesis Data Stream, you pull data from a shard, not directly from the stream as a whole. The stream is composed of multiple shards, and each shard contains a subset of the data based on the partition key that determined its placement.
* When consuming data, your application reads from each shard in the stream separately.
* The consumer must poll all shards in the stream to retrieve all the data.*

#### Sharding / Throughupt
* Data streams are divided into shards, which determine the stream's throughput.
* A shard is a unit of capacity within a stream.
* Each shard can:
    * Ingest up to 1 MB/sec or 1,000 records/sec. (producer)
    * Output up to 2 MB/sec. (consumer)
* producers
    * can send 1MB or 1000 messages per second per shard or get throughput message
    * if want to scale write throughput will need to increase shards
* consumers
    * Consumer classic:
        * read 2MB/s at read per shard across ALL consumers
        * 5 API calls per second per shard across all consumers
    * Consumer Enhance Fan Out
        * read 2MB/s at read PER SHARD, PER ENHANCED CONSUMER
        * No API calls needed(is push model)

* retention 24 hours by default, can be extended by 365 days.
* if need more read/write throughput need to add more shards
* multiple applications can consume from the same stream
    * SQS can't do that as a consumer takes the message from the queue
    * pub/sub architecture for streaming data 
* once data inserted into Kinesis it can't be deleted, is immutable
* can autoscale
* when you create the FIRST SHARD in the stream it encompasses the entire 128 bit hash space
* any new shards must be created by splitting an existing shard
* any shards to be deleted are deleted by merging shards
* Additional shards: created via SplitShard or MergeShards, and you define how the hash space is divided.
* all data written to a kinesis stream is ordered on a shard basis

#### Partition key
* The partition key is hashed(128 bit) using a MD5 hash function, and the resulting hash determines the shard.
* ensure you have a random partition key such that data is distributed equally amongst the shards
* Each shard in the stream has a hash range.


#### Capacity planning
* pay by provisioned capacity!!

* two modes: 
    1. on demand: scales automatically
        * determines size to scale based on the throughput peak during the last 30 days
        * pay pershard provisioned per hour
    2. provisioned: you managed number of shards over time (this was first original mode of streams)
        * pay per STREAM per hour and data in/out of stream


#### Integration with Recognition
* producers
    * one video stream per streaming device 
        * security cam, body cam, work cam, smartphone
    * video stream is called a producer
    * kinesis video stream producer library
    * data is stored in S3 but CANNOT access it, will have to build own dump to S3
* consumers
    * consumed by EC2 instances for real time analysis or batch
    * can leverage Kinesis video stream parser library
    * integrate with Recognition for facial detection

 producer -> kinesis vid stream -> consumers like recognition or EC2 -> can send metadata to kinesis data stream and store faces in Recognition ->
# data_engineering

## architecture.md
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
# data_engineering

## redshift.md
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
# data_engineering

## athena.md
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
# data_engineering

## aws_glue.md
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


# data_engineering

## running_jobs_on_aws.md
1. provision EC2 and use cron
2.  * not highly available, scalable
    * never use

* amazon event bridge and lambda
    * serverless
    * periodic lambda
    * has lamabda limitations

* have reactive workflow to invoke actions when something happens
    * event bridge, s3, api gateway, sqs, etc, etc

* use aws batch
    * none of the limitations of lambda
    * doens't have built in periodicity
    * can integrate with event bridge to trigger a batch job
    * event bridge has time based events


* use fargate
    * more barebones than batch


* use EMR 
    * better for long running or big data workloads
# data_engineering

## amazon_msk.md
* amazon fully managed Kafka cluster
* alternative to Kinesis
* MSK creates and manages Zookeeper nodes and Kafka broker nodes for you
* deploy cluster in multi AZ VPC (up to 3 for HA)
* data stored on EBS for as long as you want as long as you pay for it!


* MSK serverless
    * rurn Kafka on AWS without any servers to manage
    * AWS handles it all on the backend



* Kafka allows streaming


#### How does it work
* kafka has topics which are equivelent to one data stream
* topic spread out over brokers which are essentially replicas of the data
* a producer writes to a topic and it gets spread out over the brokers
* a consumer reads from a topic and will pull from one or more broker



#### Kinesis streams vs MSK

* message size
    * Kinesis: 1MB max message size
    * MSK: 1MB default size, can expand the size to higher sizes

* capacity units
    * data streams with shards
    * kafka topics with partitions

* throughput scaling
    * kinesis stream: shard splitting/merging
    * MSK: add partitions not remove

* data retention
    * MSK: can keep data for as long as you want (as long as you pay for the EBS )
    * kinesis stream: 365 days max lifetime


#### Consumers
* Flink
* Glue
* Lambda
* write own custom consumer, ECS, EC2
# data_engineering

## kinesis_analytics_flink.md
* framework used for processing data streams in real time
* Plug kinesis streams or amazon MSK (managed kafka) -> kinesis analytics
* AWS will:
    * provision the infrastructure for you
    * manage the backups(checkpoints, snapshots)
    * use any Apache Flink features to transform the data


* FLINK CANNOT READ FROM FIREHOSE!!!!

* FIREHOSE CAN READ FROM FLINK!!!
# data_engineering

## quicksight.md
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




# data_engineering

## amazon_emr.md
* Elastic MapReduce
* helps create Hadoop clusters to analyze and process vast amounts of data
* move on prem hadoop cluster jobs to AWS
* clusters can be made of hundreds of ec2 to process jobs then shutdown once job is completed
 * auto scale with cloudwatch
 * use case: data proc, machine learning, web indexing, big data
    * anything to process at scale

* EMR launched within VPC in single AZ
    * will get better network performance
    * more volative to be in a single AZ
* EC2 instances are using HDFS for the file system
    * hadoop distributed file system
    * temporary storage
* for long term storage need to use EMRFS
    * has native integration into S3
    * more durable, multi AZ

* apache hive
    * can run this in EMR to integrate/read from Dynamo


* can have long running clusters
* can have transient clusters


#### Cost optimization in EMR
    * master node - orchestrates all the other nodes and is long running
    * core node - run tasks and store data long running
    * task node - just to run tasks, usually spot instances
    * purchasing options
        * on demand - reliable, predictable, won't be terminated
        * reserved - minimum on one year, way cheaper, EMR will automatically use if available
            * good for master node and core nodes
        * spot - less reliable but way cheaper, good for task nodes

#### Instance configuration
* Uniform instance groups: select single instance type and purchasing option(on demand, spot) for each node (has autoscaling)
* Instance fleet: 
    * can specify a mix of instances and on demand and spot 
# data_engineering

## kinesis.md
* managed "data streaming" service
* ingest a lot of data at scale in real time
* great for:
    * app logs
    * metrics
    * IoT
    * clickstreams

* great for "real time" big data
* great for streamin processing framework
* data is automatically replicated synchronously to 3 AZ
    * highly avail, fault tolerant

* Kinesis is 3 services
    1. Kinesis streams - low latency streaming ingest at scale
    2. Kinesis analytics - real time analytics on streams using SQL
    3. Kinesis data firehose(KDF) - to load streams into s3, redshift, elasticsearch, splunk

* obtain data via streams
* can send to KDF for storage
* can send to KA for analytics
* can send to KA then to KDF 
* etc
# data_engineering

## Kinesis_firehose.md
* Designed for data delivery to storage or analytics destinations (S3, Redshift, etc.).


#### Main benefits
* you upload data to firehose and get these benefits
    * automatic scaling!!!
    * buffering(i.e. for saving money on writes to s3)
    * can add custom transformation logic with lambda
    * data compression/encryption(can configure Firehose to compress data (e.g., GZIP, Snappy) and encrypt it )
    * error handling/retry mechanisms (Firehose retries failed data deliveries and supports logging errors for troubleshooting.)
    * encrypted at rest and in transit

#### Flow of KDF
1. Sources:
    * Kinesis data streams - MOST COMMON
    * Amazon cloudwatch
    * AWS IoT
    * clients directly
    * other AWS services

2. transform data optional
    * has some automatic transformations
    * can use lambda to do custom transforms to the data
    * there's several blueprint lambda templates
        * example: json to csv or compress of data
    * Firehose supports data compression (e.g., GZIP, Snappy) to save storage costs
    * firehose supports many data formats, conversions, transformation,compression
    * Lambda is invoked for every batch of data sent by Firehose to the function for transformation.
    * Invocation cost: $0.20 per million invocations.
    * Frequent invocations (due to small Firehose buffer sizes) can increase costs.
    * want a large buffer to use one lambda
    * Note this can get expensive

    * if have high throughput, the size buffer will be reached

3. data is buffered if enabled
    * has size and time buffers that can be specified
    * can disable buffering
    * can allow buffer to autoscale as well
    * Firehose buffers incoming data before delivering it, reducing the number of writes to the destination and improving efficiency.
    * adjustable buffer interval from 0 to 900 seconds 
    * also has a few second constant delivery time interval
    * useful for example with s3: this reduces the number of PUT requests to S3, lowering S3 costs.
    * time and size
        * when buffer size is reached, it's flushed and sent to deis
        * If after set time even if buffer is not full, it will flush
            * minium time: is 1 minute
    * firehose can automatically scale the buffer size if have high throughput
    * if have low throughput the buffer time limit will reached


4. destinations
    * can send to multiple destinations
    * 3 types of destination:
        * AWS destination  REMEMBER THESE VERY IMPORTANT FOR TEST
            * S3
            * redshift(copies to s3 first! very important! then KDF issues a copy command to copy from s3 to redshift)
            * opensearch
            * splunk
            * lambda (as transformation NOT final endpoint)
            * API Gateway via POST calls, which then call a lambda
                * Set Firehose’s destination to HTTP endpoint.
                * Create an API Gateway + Lambda combo to accept incoming POSTs from Firehose.
                * In your Lambda, write data to Timestream or any other custom destination.

        * 3rd party (splunk, datadog, mongo etc)
        * custom HTTP api 
    * can deliver to one or more destination 
    * NOTE: Sparc and KCL CANNOT read from FIREHOSE, ONLY kinesis data stream
    


5. post processing
    * after data sent to destinations can also output the source records to s3 as a backup
    * can have a sort of DLQ by sending data that was failed to write to a s3 bucket

#### Capacity planning
* NONE! 
* automatic scaling


#### Price
* pay only for data going through firehose

 


#### When to use streams vs firehose
* streams
    * Designed for real-time DATA STREAMING.
    * More suitable for applications that need real-time, event-driven processing.
    * Provides more flexibility for complex or real-time transformations.
    * data processed in real time (under 200ms)!!!
    * Requires you to write and deploy producers/consumers to move data to storage or analytics systems.
    * data stays in system from 1 to 365 days and is immutable
    * Multiple consumers can consume the data(different from SQS which one consumer removes post from queue)
    * manage scaling yourself: shard splitting merging(autoscale exsist now)
    * pay by provisioned capacity!!
    * support replay capability


* firehose
    * Designed for DATA DELIVERY to storage or analytics destinations (S3, Redshift, etc.).
    * Ideal for low-maintenance, near-real-time data pipelines.
    * load streaming data into (S3/Redshift/Opensearch)/3rd Party/custom HTTP
    * near real time!!
    * fully managed
    * automated scaling!
    * pay by usage!!!
    * no data storage
    * can send to multiple destinations
    * buffering(i.e. for saving money on writes to s3) 
    * can add custom transformation logic with lambda
    * automatic scaling
    * data compression/encryption(can configure Firehose to compress data (e.g., GZIP, Snappy) and encrypt it )
    * error handling/retry mechanisms (Firehose retries failed data deliveries and supports logging errors for troubleshooting.)


#### Why?
* Firehose automatically delivers streaming data to the specified destination without requiring you to manage and scale the infrastructure for data ingestion.
* Supports destinations like Amazon S3, Amazon Redshift, Amazon OpenSearch Service (formerly Elasticsearch), and third-party services like Splunk.
* Without Firehose, you would need to write, deploy, and maintain custom ingestion and delivery code. Firehose abstracts this for you.
* Firehose scales automatically to handle incoming data volume, eliminating the need to manually provision resources.
* It can handle gigabytes per second of input data, making it suitable for high-throughput use cases.
* Firehose can invoke an AWS Lambda function to transform or enrich data before delivering it to the destination.
    * Example: Format raw JSON logs into a structured CSV format for storage in Amazon S3 or Redshift.


# DNS

## global_accellerator.md
* Anycast IP
    * essentially an IP that multiple servers share
    * Multiple servers in different geographic locations are configured to use the same IP address.
    * Routing to the Nearest Server:
        * The Border Gateway Protocol (BGP) or other routing protocols ensure that traffic is directed to the closest (or most optimal) server based on metrics like latency, hop count, or path cost.
    * Dynamic Failover:
        * If a server goes offline, the traffic is automatically rerouted to another server sharing the same anycast IP, ensuring high availability.
* 2 anycast IP are created for your applications
* Anycast IP will route traffic to closest edge location
* The AWS  will then route the traffic to your resources in whatever region they're in over the high speed internal AWS backbone

#### how it works

* Global Entry Points:
    * When you set up Global Accelerator, AWS assigns you two static IP addresses from different network zones for redundancy.
    * Users connect to these static IPs to access your application.

* Traffic Optimization:
    * The user’s request is routed to the AWS global edge location nearest to them.
    * From the edge location, traffic travels over the AWS global network to the endpoint closest to the user or the best-performing one.

* Endpoint Management:
    * You can add various AWS resources as endpoints:
        * Elastic Load Balancers (ALB, NLB)
        * EC2 instances
        * Elastic IP addresses
    * Endpoints can be in different AWS Regions, allowing for global application deployment.

* Health Monitoring:
    * Global Accelerator does health checks of your application
    * Global Accelerator continuously monitors the health of your application endpoints and reroutes traffic to healthy endpoints as needed.

* DDoS protection
    * AWS Shield


#### Cloudfront vs Global Accelerator
* Cloudfront
    * improves performance for cacheable content: images, videos, API returns, HTML, etc. 
    * content is served and cached at the edge

* GA
    * It's essentially an edge proxy that will send your traffic over high speed AWS network to your application in any region
    * works for non HTTP use cases also: gaming, IoT, VOIP
    * good for HTTP needing failover 
    * good for HTTP needing static IP's
# DNS

## route_53.md
#### Hosted Zone
* a Hosted Zone is essentially just a domain with all the records attached to it
* can associate a traffic policy with a hosted zone
* public zone - for internet resolving
* private -     resolvable only within AWS

#### DNS record types
* A/AAA
    * A: maps hostname to ipv4
    * AAA: maps hostname to ipv6
    * Can point multiple domains/subdomains to the same  IP with multiple A/AAA

* CNAME: maps hostname to another hostname
    * target must have an A record
    * cannot create a CNAME for a TLD
        * can only create a CNAME for a subdomain
        * would have to be a www.somesite.com, not somesite.com
* NS: record of the nameserver/s that hold which authoritative name servers are responsible for handling queries for a particular domain or subdomain
    * If a DNS server doesn't know how to resolve a domain, it responds with NS records for the next level of the DNS hierarchy.
    * This process continues until:
        * The record is found, or
        * An NXDOMAIN response is returned if the domain does not exist. (failure mode)

* ALIAS record: An ALIAS record in Route 53 is a special type of DNS record specific to AWS. It allows you to point a domain name (or subdomain) to an AWS resource instead of an IP address.
    * ALIAS records are AWS-specific, designed to simplify integration with AWS resources and handle dynamic IP changes automatically.
    * NOTE: ALIAS are completely transparent to the client which views them essentially as an A record
    * Here’s what happens:
        * The dig query requests the A record for example.com.
        * Route 53 resolves the ALIAS target (my-cloudfront-distribution.cloudfront.net) into its corresponding IP addresses.
        * The client receives the resolved IP addresses as if they were direct A records.
    * When a resolver queries an ALIAS record, Route 53 dynamically resolves the ALIAS target (e.g., the IP addresses for the CloudFront distribution or ELB) and responds with the resolved A or AAAA records.
    * The TTL value returned for an ALIAS record is inherited from the target resource's TTL (not explicitly set on the ALIAS record itself).
    * in many cases won't be able to do a CNAME but can do an ALIAS
    * can't set ALIAS for an EC2 domain name

* DNS TTL
    * caching of the DNS response for the TTL 
    * will use the cached DNS response instead of reaching out to DNS server
    * note: when change record, will have to await for the TTL to expire so the client will check with DNS server again
    * tradeoff between less load on DNS server and how easily to change records
    * Except for ALIAS, TTL is mandatory
        * this is interesting as you can repoint your alias records to new locations without a TTL

#### Routing policies
* can specify multiple values in a DNS record 
    * respond with multiple value in the DNS record
    * a random one is chosen by the client

* all but simple policy can be associated with health checks

* simple
    * route traffic to a single resource
    * not associated with a health check
    * can specify multiple values
* weighted
    * in rt53 can specify weights of resources 
    * Based on the weights assigned, Route 53 randomly selects one record with a probability proportional to its weight.
    * rt53 will return that to the client
    * all handled in rt53 client only sees one record 
    * can be associated with health checks which means rt53 will not return the record if the health checks fail
* latency based records
    * redirect to the source that has the least latency to us
    * latency defined by the traffic between the users and AWS regions
    * can associate with health checks as well
    * How Latency-Based Routing Works
        * Client Query:
            * A client (e.g., a web browser or application) makes a DNS query for a domain (e.g., example.com).
            * This query is handled by the client's recursive DNS resolver (provided by an ISP or corporate network).
        * Resolver Location:
            * Route 53 sees the IP address of the resolver, not the client’s IP.
            * It uses the resolver’s IP address to estimate the client’s geographic location.
        * Latency Evaluation:
            * Route 53 uses pre-computed latency measurements to determine which AWS region provides the lowest latency for that resolver.
            * These measurements are periodically updated by AWS to reflect real-world conditions, including changes in network topology or congestion.
        * Record Selection:
            * Route 53 selects the DNS record for the endpoint (e.g., IP address, ELB, CloudFront distribution) associated with the region that has the lowest latency for the resolver.
            * It returns only one record in response to the query.
* failover policy
    * have primary/secondary resources
    * simple health checks and if the primary fails will route to secondary

* geolocation  policy
        * route 53 uses the ISP or whoever is the clients originating DNS resolver to identify location
        * will respond with a record matching the closest location of the resource
        * have a default fallback if no gelocation match exists

* geoproximity policy
    * similar to geolocation
    * Geoproximity routing is part of Route 53’s traffic flow feature, and you must use a traffic flow policy to configure it.
    * Like geolocation routing, Route 53 uses the resolver's location, which may not always align with the client’s actual location.
    * adds a bias
        * Route traffic to the nearest resource while biasing certain regions for load balancing.
        * a greater bias will send a larger area of traffic to a resource
        * essentially expands the region with a larger bias
        * can send more traffic to the region with bias from 1 to 99
        * can sen less traffic to the region with bias from -1 to -99
* multi-value poicy
    * returns multiple values/resources
    * associated with health check so only valid/healthy responses are returned
    * returns up to 8 values
    * can load balance via DNS but not a substitute for a true LB

* IP based routing
    * similar to geoproximity or geolocation but instead of looking at client and resolvers location it looks at the IP
    * routes based on the CIDR of the client and its resolver
    * allows routing based on specific IP locations, i.e. sending all traffic from a particular ISP to a certain resourcre

#### Traffic flow
* visual editor 
* allows complex decisions trees in routing flows 
* allows bias so that certain regions will have much larger area sending traffic to a resource
* configurations can be saved as a 'Traffic Flow Policy'
    * a single policy can be applid to dfifferent domain names(Hosted Zones)
* supports versioning

#### health checks
    * can add health checks on rt53 
    * note: theres a bunch of health checkers located all around the world
        * health checkers outside of VPC's so can't health check private/on prem

    * create a cloudwatch alarm to monitor a private/internal/on prem resource
        * the health checker can monitor that cloudwatch alarm, i.e. check the alarm itself
    * can specify conditions for pass/fail
        * pass: 200/300 status code
        * pass/fail: based on text in first 5120 bytes of the response 

    * 3 types of hc
        * monitor an endpoint
        * calculated health check, monitor other health checks, 
            * combine a bunch of health checks into one
            * can have up to 256 children into one
            * specify how many of child need to pass to make parent pass
        * cloudwatch alarm health check i.e. can make any thing a health check
            * i.e. database overload, etc.

#### hybrid DNS 
* have both on prem DNS servers AND rt53 dns servers 
    * both will have different domains i.e. aws.org and myonprem.com
    * both of those will not know each other's full listing of DNS zones
    * both can have a generic forwarding domain and will forward those requests to the handling DNS server
    * essentially functions like normal DNS as it forwards request to the resovler to handle it.
    * note: will need to have a 'Resolver Endpoint', which are ENI's on the subnets hosting the servers that are essentially attached to route 53 and allow external requests to be recieved by route 53 or internal requests from route53 to leave the subnet to go to the on prem resolvers
    * VERY IMPORTANT TO KNOW ABOUT INBOUND AND OUTBOUND ENPOINTS and hybrid DNS for exam

* split horizon
    * internal DNS resolution vs External public DNS resolution for the same resource
    * DNS will return different responses based on if the request if from internal networks or external public

#### Resolver rules
    * rules that are set to require forward requests for specific domains to another resolver
        * the rule is the resolvers IP
    * can customize in detail for example send a subdomain to a different resolver than it's parent domain
    * there's a ton of preconfigured rules already for internal AWS stuff
    * if multiple rules match route 53 will choose the most specific match
    * can share these rules across account if you're using AWS Resource Access Manager(RAM)
        * but then manage centrally in one account


#### OTher

* DNSEC- dns security
    * good for protecting from man in the middle attacks
    *  SEcure domain names
    * only works with public zones
* can buy domain from 3rd party and point at rt53 



#### Architecture

* have two replica RDS instances-one active, one as backup, both in internal VPC
    * have either an 
        * API endpoint via lambda/ec2 to do a health check
        * cloudwatch alarm set on RDS
    * can set the rt53 Health check to check these since they're not internal private and can be checked
    * can then trigger a cloud watch alarm on this check which will trigger a lambda to 
        * change the backup to primary
        * change rt53 dns  to point to back up
# identity_federation

## IAM.md
* IAM Role:
    * An IAM role is an identity within AWS that provides permissions for accessing AWS services.
    * It contains a set of permissions defined by policies (e.g., S3 access, DynamoDB access).
    * When an EC2 instance profile is used, the IAM role is assumed by the instance.

* EC2 instance profile
    * An instance profile is essentially a container for the IAM role.
    * You create an instance profile and attach the IAM role to it.
    * The profile is then associated with an EC2 instance, enabling applications running on the instance to use the role's permissions.
# cost_control

## RI_notes.md
* all accounts in an OU share the RI and Savings planv

* the managmeent account is only way to turn off any RI discount for any account in OU
* this is done in billing dash board of management account


### Renewal of reserved instances
* can queue ahead of time purchase of reserved instances
* so to renew just queue a reserve instnace purchase on the exact date the other expiers
# cost_control

## trusted_advisor.md
* build in service
* analyze account and provide reccomendations
    * cost optimize - KNOW
    * security
    * fault tolerance
    * performance
    * service limits - KNOW 
    * operational excellence - KNOW


* basic advisor: get 7 core checks and reccomendations
    * all customer have access

* full advisor only available to business and enterprise support plans

* cloudwatch alarms, email notifications, access via API


support plans
basic - all customers, is free, get 7 score checks via Trus.Adv
developer - pay, more support, but still only get access to the core checks
business/enterprise
    * access to full set of Trus. Adv. checks
    * can get programattic access to trusted advisor via API


### What can it check
* can check if a bucket is public 
    * CANNOT check if anything is public inside the bucket(see below)
* service limits    
    * only monitored NOT changed in trusted advisor
    * have to either open a case or use service quotas service



### increase service limits


### Check public items inside of buckets
How to check for public objects instead:

* Amazon EventBridge / S3 Events
    * Set up event notifications for changes in object ACLs or bucket policies. When an object becomes public, an event can trigger a Lambda function or another alerting mechanism.

* AWS Config Rules
    * Use AWS Config to continuously monitor AWS resource configurations. Specifically:
    * Use the managed rule: s3-bucket-public-read-prohibited
    * Use custom Config rules with Lambda to dive deeper into object-level access.

* in summary, To detect public S3 objects, not just buckets:
    * Use AWS Config Rules for ongoing compliance.
    * Use EventBridge or S3 Event Notifications to react to access control changes in real-time.
# cost_control

## aws_budget.md
* create a budget and set alarms when cost exceeds budget
* 4 types of budgets
    1. cost
    2. usage
    3. reservation
    4. savings plans

* for reserved instances (RI)
    * track utilization
    * supports EC2, elasticache, RDS, Redshift

* define up to 5 notifications per budget

* budgets are very granular
* can define a budget by: service, linked account tag, purchase option, instance type, region, availability zone, api operation

* same otions as COST EXPLORER!

* budget action
    * run an action when the budget exceed threshhold
    1. Apply IAM policy to a user,group, or IAM role to restrict from doing anything
    2. Apply service control policy to an organizational unit to restrict what an account can do
    3. Stop EC2 or RDS instances
    * can happen automatically or require a workflow approval to ensure some human says yes

* Example:  If have a root OU with a dev OU inside of it that needs resources in the root OU. 
    * if the budget alarm threshold is triggered, can apply an SCP to the dev OU to restrict their access to the root OU resource


* centralized budget management
    * see architecture section
* decentralized budget managemetn
    * see architecture section


# cost_control

## aws_compute_optimizer.md
* reccomend optimal AWS resources for your workloads
* analyze ec2 instances/ASG and tell you which are over/under provisioned
* uses machine learning to analyze your usage metrics and gives reccomendations
* reccomendataion can be save to s3
* can lower costs
* looks at cloudwatch
    * need to install cloudwatch agent to get memory metrics to cloudwatch otherwsie not needed for cpu, network, disk
# cost_control

## s3_cost_savings.md
* standard GP
* standard IA
* one zone IA


* Intelligent tiering
    * will move objects between tiers to maximize cost savings
    * have to pay for each object being monitored(but ends up cheaper still)
* glacier instant retrieval
    * allows to retrieve glacier files quickly

* glacier flexible retrieval
* glacier deep archive
    * most savings but a long time to restore the file

* can define s3 lifecycle configuration
    * automatically transition objects between tiers

* compress objects before sending to s3!!


* s3 requestor pays
    * the person requesting the object will pay and not the owner
    * in general bucket owners pay for s3 storage/transfer costs
    * with this requestor pays for cost of transfer (not storage)
    * good for sharing large dataset with thousands of accounts
    * users have to be authenticated with IAM before able to download data
    * be careful of ROLES   
        * if you give cross account access to a role and that's used to query the bucket then you pay!!

# cost_control

## ec2_launch_types.md
### Two types

1. spot instances
    * short workloads
    * transient-can loose them 
    * not reliable

2. on demand instances
    * predictable pricing, reliable, stable


3. reserved
    * minimum 1 year to commit
    * for long workload

4. convertible reserved
    * long workloads with flexible instances


5. dedicated instances
    * no other customers even share your hardware

6. dedicated host
    * book entire physical server
    * control instance placement

7. Savings plan
    * discounts based on long term usage
    * commit to a type of usage: i.e. 10$ per hour for up to 1 to 3 years
    * any usage beyond this is billed at on demand price
    * EC2 savings plan
        * gives like 72% savings (same as standard reserved instance)
        * more flexible, rather than locked into a specific instance on RI you choose an instance family on a region
            * locked to instance family
            * locked to region
            * can be any size
            * any OS
            * dedicated or default tenancy
    * Compute savings plan
        * up to 66%, same as convertible RI
        * not locked to instance family
        * not locked to region
        * can also use in ECS or Fargate
        * OS and tenancy
    * sage maker savings plan
        * up to 64% off
        * only on sagemaker workloads
        
* bare metal instance will allow access to core and sockets
* can define host affinity so instance reboots are kept on same host
# cost_control

## cost_allocation_tags.md
### Types of tags

* custom allocation tags just appear in the billing console
* takes about 24 hours for tags to appear in billing reports

* AWS generated tags
    * starts with prefix aws:
    * not applied to resources created before the activation of these tags so no retroactive tagging
    * extends cost tracking functionality by adding tags to track additional things
        * aws:servicecatalog:provisioningProduct
        * cloudformation stack name
        * createdBy
        * and more



* user defined tags
    * custom tags user create   
    * define with prefix user:
    * can define custom tags like application, team, environment, etc.


### Tag editor
* Find resources to tag
* has a search function where you can target groups of resources
* bulk tag add/update/remove to these resources
* search tag/untagged resources in all aws regions
* 
# cost_control

## cost_explorer.md
* visualize,understand, and manage AWS cost/usage over time
* create custom reports that will anylyze cost and usage data
* analyze data at a high level: total costs and usage across all accounts
* or monthly, hourly, resource level granularity
* choose an optimal savings plan(to lower prices on your bill)
* can forecast usage up to 12 months based on previous usage

# cost_control

## service_quota.md
* Service that notifies you when you're close to reaching a service quota value threshhold


* the service quota's console is just a link to create a cloudwatch alarm with a threshold




# security

## Shield.md

# security

## network-firewall.md
* protects from layer 3 to 7

* inspect any traffic in any direction
    * cross VPC
    * internet inbound/outbound
    * direct connect/VPN inbound/outbound
# security

## WAF.md
* protect against DDOS
# security

## Firewall-Manager.md

# lambda

## basic.md
* main integration
    * API gateway
    * Kenesis
    * DunamoDB 
    * S3 
    * IoR
    * Event Bridge
    * Cloudwatch logs
    * SNS
    * Cognito
    * SQS

* Serverless thumbnail creation
    1. New image in S3
    2. Trigger Lambda
         * create a thumbnail
         * push the new thumbnail to s3
         * push the metadata to DynamoDB
    
* Serverless Cron job
    1. Event bridge to create a time based trigger
    2. Triggers AWS lambda

* Languages(don't need to know)
    * node
    * pythong
    * java
    * C#
    * ruby
    * custom runtime API(rust/golang)


* Use container image on lambda
    * max image size is 10GB
    * container image must implement lambda runtime API
    * prefer to use ECS or Fargate instead of Lambda for containers

* Resources
    * 128Megs to 10Gigs of RAM
    * CPU is linked to RAM (cant be set)
        * example: 2vcpus allocated at 1,769 MB of RAM
        * 6vcpu's allocated @ 10Gig
* Timeout 
    * max amount of time lambda can run before AWS stops its execution
    * can run up to 15 minutes

* /tmp storage 
    * 10,248 MB

* Deployment package limits
    * 50 MB zipped
    * 250MB unzipped

* concurrency
    * up to 1000 concurrent executions by ALL SERVICES(soft limit can be increase by AWS team)
    * anything trying to use Lambda past this will be throttled
    * A workaround is to send requests to SQS and let lambda process them if tolerant to async
    * Reserved Concurrency: can set a reserved concurrency for a specific lambda
        * allocate a specific number of concurrent execution slots exclusively for a particular Lambda function. 
        * If a function exceeds its reserved concurrency, additional requests are throttled, returning a ThrottlingException.
        * A function has its slots available to it but CANT EXCEED THEM even if slots are available

    * Provisioned Concurrency: Keeps a specified number of execution environments initialized and ready to serve requests with low latency.

* Lambda async/sync
    * Synchronous Lambda
        * Immediate response from the Lambda
        * API gateway for example
        * larger payload sizes because the client manages the full lifecycle of the request and response.
        * Errors handled client side(retrys, backoff, etc)

    * Async Lambda
        * AWS handles the queuing internally
        * Used for event driven architecture
        * no immediate reponse
        * Smaller payload sizes
        * can define dead letter queue for if the async event fails and then fails the set number of retrys also
        * uses: event driven events, any sort of job: s3 thumbnail creation, SNS event, etc.


* Invokation/Output Payload max size
    * 6MB when synchronous
    * 256KB when asynchronous
    * Workarounds for Large Payloads
        * If you need to process payloads larger than these limits:
        1. Use Amazon S3
            * Store the large payload in an S3 bucket and pass the S3 object key or a pre-signed URL to the Lambda function.
            * This approach works for both synchronous and asynchronous invocations.
        2. Use Amazon SQS
            * For asynchronous workflows, split the payload into smaller chunks (if possible) and send each chunk as a separate SQS message.
        3. Use API Gateway or Step Functions
            * Combine Lambda with API Gateway or AWS Step Functions for orchestrating large workflows where payloads can be handled in multiple steps.

* Lambda and Code Deploy
    * integrated with the SAM framework
    * can help automate traffic shift for Lambda aliases 
        * gradually shift traffic from a v1 endpoint to a v2 by a percentage amounts
    *  Strategies:
        * Linear: linear increase by X amount in Y minutes
        * Canary: X amount over Y time frame then all in
        * AllAtOnce
    * Can run pre/post traffic hooks to check the health of a Lambda function so wont move traffic if Lambda unhealthy

* Logging/Monitoring/Tracing
    * AWS execution logs/metrics are in Cloudwatch
    * ensure AWS Lambda role has IAM policy to allow write to Cloudwatch

* X-Ray
    * Its possible to trace Lambda with X-Ray
    * Enable it in the Lambda configuration(will run the X Ray daemon for you)
    * If need XRay instrumentation in CODE: Use AWS SDK 
    * Ensure Lamda has IAM access to XRay
    * Note: Xray can trace all kinds of stuff including a request flow through AWS, database performance, etc.


* Cold start
    * Lambda's have cold starts
    * cold start happens the first time a lambda is invoked
    * cold start can take up to 1 second to get the lambda working (programming language runtime can reduce this drastically)
    * after the first invokation the container stays 'warm' and handles requests instantly
    * AWS Lambda containers typically stay warm for 5 to 15 minutes after the last invocation. However, the exact duration is not guaranteed and depends on AWS's internal optimizations and resource allocation policies.
    * if autoscaling will have delays during the cold starts as new lambdas are spun up to handle load(small delays of 1 seoncd or so)
        * note: this happens once as it expands and the new lambdas stay warm for many minutes
    * still way faster than any other method of autoscaling




#### Lambda in a VPC
* by default Lambda not deployed in a VPC, deployed to the AWS cloud at large
* Can't connect to internal VPC stuff
* Note: by default lambda in a VPC will not have internet access
* If deploy lambda in a private VPC, can connect InternetGW/NAT gateway in public subnet to reach/be accessible by internet
    * this will also allow access to some out of VPC AWS public services
* Could also create VPC endpoint for Lambda to reach out of VPC AWS services 
* If lambda deployed in public cloud, will get a random public AWS IP
* If deployed in private VPC NAT will take care of this with its Public IP



#### architectures

* Whats the difference:
    * s3 -> SNS -> lambda
    * s3 -> SNS -> SQS -> lambda
# deployment_instance_management

## code_deploy.md
* applications deploy to many EC2 instances
* go from one version to another version
* (not managed by elastic beanstalk)
* can deploy to EC2, ASG, ECS, Lambda

* half at a time deployment
    * take half of existing instances down(or some proportion)
    * upgrade them
    * bring them back up 
    * bring the other half down
    * upgrade
    * bring back up
    * IN PLACE UPDATES


* blue/green or canary: 
    * essentially create new environment, test it, then switch traffic to it
    * if traffic switched all at once is blue/green, if trickle is a canary



### EC2
* define how to deploy with an file named: appspec.yml + deployment strategy(i.e. cnary? blue/green, how fast/gradual? etc)
* appspec.yaml
* does in place updates i.e. doesn't create new instances
* can define hooks to verify the deployment is working great after each deployment phase
* can use half at a timeIt  theanswers question:




### code deploy to ASG
* one of two ways:
    * in place updates: 
        * updates current existing EC2 instances in ASG (see half at time deployment)
    * blue/green:
        * new autoscaling group created, settings copied, and instances copied from one instance to another
        * new ASG created via launch template
        * can choose how long to keep the old instances
        * ASG will be serving to both version while transitioning
        * At some point will remove the old versions if everything is working well


### Lambda
* creates a new lambda and then 
* essentially blue/green with a lambda alias that will allow traffic shifting to the v2 lambda 
* allowed to run a pre and post deploy lambda(will need to define these)
* can monitor deploy with cloudwatch metric and setup an alarm to trigger a rollback
* can roll back with cloudwatch alarms, set it up to monitor some metrics to test to see if working if not rollbacks
* if both the pre/post hook lambda pass the deploy is successful
* easy and automated rollbacks with cloudwatch alarm
* SAM framework natively does code deployment


### ECS / Fargate
* write a new task i.e. next version of the task
* the tasks are sent traffic by the ALB
* traffic shifting will happen from old task to new in either blue/green or canary fashion
* once new task is validated the old task will be deleted

* can code deploy to ECS with blue/green deploys or canary deploys
* setup is done withing ECS service NOT code deploy
* new task set is created and traffic routed there
* if everything stable for some pre-defined minutes then the old task set is terminated
* architecture: ALB -> ECS service which uses ECS task to launch ECS tasks



### Deployment strategies
* half at a time (will take half down, upgrade, then go live, then do other half)

# deployment_instance_management

## systems_manager.md
* get operational insights about the state of your infrastructure
* helps manage EC2 and on-prem instances
* Easily detect problems
* patch automation at scale
* integrated with cloudwatch metric/dashboard
* integrated with AWS config
* totally FREE

* need to install the SSM agent on the systems we control
    * by default installed on AWS made and some Ubuntu AMI's
    * need to make sure the SSM agent has proper IAM permissions to register with system 
    * if on prem - make sure the access keys are correct for the agent to connect to systems manager


### Functionality

* run a command across multiple instances
    * define resource groups to group instances
    * rate control / error control to define how fast to run this command across instances and what to do with any that error
    * fully integrated with cloudtrail and IAM
    * no need for SSH, the agent takes care of it
    * results are shown in the SSM console

* session manager
    * can get a console on a host
    * different than SSH, does not need any SSH configurations or keys
    * access via aws cli, SDK, aws console
    * can send the session info to logs
    * can configure a hook to send startSession events to cloudtrail to tell when someone has started an SSM session


* patch manager
    * define a patch baseline, patch groups(i.e. dev, test, etc)
    * maintenance windows
    * monitor patch compliance using SSM inventory
    * define rate control ( errors  and concurrency ) 

* OpsCenter
    * differs' from SSM ops center in that Health dashboard gives you all the issues that AWS is experiencing
        * whereas AWS SSM ops center gives you all the issues happning in your environment
    * logs, alarms, config info, stack info
    * By default — OpsCenter won’t show anything unless something creates an OpsItem.
    * It’s not automatic for all issues. You need to configure sources or rules that send issues to OpsCenter. 
    * ex: cloudwatch alarm for high cpu -> eventbridge -> eventbridge rule will send to opscenter
    * can define a runbook for fixing those issues
        * runbook is a series of automations that run to possibly fix an issue
    
# deployment_instance_management

## elastic_beanstalk.md
* idea: a developer centric view of deploying an application on AWS cloud
* wrapper around all native AWS components(EC2, RDS, ASG, etc)
* one view that's easy to make sense of

* free to use beanstalk, but pay for underlying resources

* Beanstalk supports numerous runtime languages: java, golang, php, node, etc.

* can also use docker with beanstalk 
* if you can dockerize your application, then you can migrate it to elastic beanstalk

* great to replatform your appliation from on prem to cloud


* managed service: instance configuration/ OS config handled by Beanstalk
* deployment strategy is configurable but handled by beanstalk, so can have different rollout strategies
* develoer is just responsible for the application code 

### three architecture models
    * Devlopment: single instance w/ elastic IP
    * High Avilability: LB + ASG + Multi-AZ (standard stuff)
        * web tier: ALB, ASG, EC2
    * Worker envi: data -> web tier -> SQS -> Auto Scaling Group( can adapt to SQS size)
        * useful for long running tasks and/or resource intensive that can take a while to complete
        * anytime hear 'decoupling' think SQS
        * ex: processing video, generating zip file, etc.
        * can configure them to be periodic as well


* blue/green deployment
    * create a new stage environment and deploy the new version there
    * route 53 to use weighted routing to slowing increase traffic
    * can use the "swap URL" which will just swap all traffic from one to another
    * from blue to green
    * can either do gradual(canary) or full

# deployment_instance_management

## SAM.md
* framework for developing serverless applications
* all the code in yaml
* can create all kinds of resources for developing an application
* can also help you run all of these resources
* SAM uses code deploy internally to deploy lambda functions with traffic shifting - VERY IMPORTANT TO KNOW
* uses cloudformation in the backend

* SEE CICD SAM architecture diagram in the architectures folder

* codepipeline + codecommit + code build -> cloudformation + deployable lambda zip file with depdencies etc.

* code build
    * It builds the Lambda code.
    * It generates a deployable CloudFormation template via the SAM packaging process.

* SAM + Cloudformation is then run to deploy this and create resources

* code deploy then traffic shifts from v1 to v2 of the lambda


# deployment_instance_management

## cloud_map.md
### cloud map 

* can register all the components in cloud map
* can do code free upgrades to new versions of services
* integration with health checking - stop sending traffic to unhealthy endpoints
* apps can query cloud map via SDK, API or DNS
# deployment_instance_management

## AWS_CDK.md
* define cloud structure using familiar programming language
* the code is compiled into cloudformation templates
* can define infrastructure and run time code at same time together
    * great for lambda fucntions, docker containers

* you use the CDK cli to transform into CF templates which can then be deployed

# deployment_instance_management

## cloudformation.md
* Infrastructure as code
* other services rely on it, for example: beanstalk, SAM, etc.


* Note: these are some facts about it to know.



* Data retention: retain data when CF stack is deleted 
    * by default everything is deleted in CF
    * can define a DeletionPolicy to control what happnes when CF template deleted
        * in CF under the resource itself you add DeletionPolicy attribute
            * DeletionPolicy=retain
                * just simply don't delete it
            * DeletionPolicy=snapshot(can delete,  but take snapshot first)
                * works on anything that can be snapshotted for example: ebs, rds, elasticache, redshift
            * DeletionPolicy=delete
                * default policy, delete the resource
                * if using RDS, the default policy is to snapshot
                * S3 bucket can't be deleted unless empty

* Custom resources: can define cloudformation custom resources
    * backed by a lambda function that can do anything you want (via API calls)
    * anytime CF is run, will invoke that custom resource which will invoke the lambda
    * for things like
        * brand new resources with no CF support, can use lambda to manipulate them
        * an on-prem resource
        * emptying an s3 bucket before deletion
        * fetch an AMI id
        * anything else!!!

     
            

* Stack sets: update all accounts and regions associated with the stack set
    * manage stacks across multiple accounts/regions
    * allows you to deploy the same infrastructure across regions/accounts
    * really useful for security or shared services
    * can enable an auto rollout feature for when an account is added to an organization


* cloudformation drift
    * things become changed outside of cloudformation i.e. manually
    * this is drift
    * how to know: use the service called: cloudformation drift
    * can detect drift at the stack layer or lower

* integration of secrets manager and Cloudformation
    * can create a secret in the cloudformation template with a function call GenerateSecretString
    * that secret is stored in secrets manager
    * that secret is then set in a reference that can be used throughout cloudformation without having to hardcode the secret in the CF template file
    
* import existing resources 
    * can import existing manually created resources into a cloudformation template
    * will need to create a CF template that mirrors currently existing maually created resources
    * use unique identifiers for resources
    * when you add/run that via cloudformation it will not delete the resources first it will simply add them as part of the stack



# deployment_instance_management

## CICD.md

Code -> Build -> Test -> Deploy -> Provision

* code: VCS like github, gitlab, ECR for docker etc.
* Build/Test: code build, jenkins, code build can build/package a new docker image!!
* Deploy/Provision: beanstalk, code deploy/EC2 fleet via cloudformation, ECS
* code pipline orchestrates all of these steps


#### General process
1. Developers push code to a repository
2. Trigger webhook
3. Build server: pulls the code and Builds the code and runs tests on it (code build, jenkins CI)
4. Gives feedback via various channels on if tests pass/fail
5. Deployment server: Once build has passed, Code is deployed (jenkins CD, code deploy, spinnaker)
* NOTE: build server and deploy server can be same or separate hosts


#### Continuous Integration
* code is tested continuously
* allows to deploy more often
* build server can run tests (which can take a long time) instead of dev's having to run on their machines



#### Continuous Delivery
* deploy often and deployments are quick
* instead of one large release every month to 5 small releases per day
* keeps each release safer with smaller surface area for bugs 
* you catch bugs a lot quicker



#### Info
* code pipeline orchestrates ALL of this
* can trigger a lambda when pushing to code commit 
    * lambda can run code 
    * example: scan code for AWS credentials and then trigger IAM to disable that credential
* code pipeline allwos a manual approval stage before deploying
* docker can be used 
    * code build will build/package the docker image then push into Amazon ECR
* Can do cloudformation deploys in cloud pipeline


#### Code pipeline/Github integration
* Code pipeline polls github
* github sends webhook
* Github has code star source connection application which does integrations and will update code pipeline
# deployment_instance_management

## service_catalog.md
* cloudformation used to create a 'product'
* this product is assembled into a collection called a portfolio
* this portfolio of products then has permissions set by IAM
* theres a console that the users can visit that will show the product list they are authorized for
* can provision products from there

* helps with governance, compliance, consistency
* service catalog can integrate with other applications such as service now
# deployment_instance_management

## code_guru.md
* ML powered service for automated code reviews and performance reccomendations
* code guru reviewer
    * automated reviews for static code analysis
    * bugs, memory leaks, security leaks, input validation, best practices,  etc.
    * uses machine learning and AI after analyzying millions of code reviews for data set
    * supports java and python
    * integrates with code  commit and 3rd party apps like github
* code guru profiler
    * visibilty/reccomendations for application performance during runtime in production
    * detect/optimize the expensive lines of code pre-production on a stage or test server
    * run time behavior of application
    * identify code inefficencies
    * example: if application consuming excessive CPU performance in some function
    * provide heap summaries: identify which objects using up the most memory
    * anomoly detection
    * support AWS or on prem application
 

#  monitoring_and_alerting

## cloudtrail.md
AWS CloudTrail is a logging and auditing service that records every API call made in your AWS account. 
* “Who did what, when, and from where in my AWS account?”
#  monitoring_and_alerting

## personal_health_dash.md
* bell icon in the nav bar at the top
* will tell you all of the AWS internal issues going on as well as others you define
* Global service
* Show how outages happen in AWS
* Show impact on resources
* List issues/actions you can do to remediate them
* differs' from SSM ops center in that Health dashboard gives you all the issues that AWS is experiencing
    * whereas AWS SSM ops center gives you all the issues happning in your environment

* will show you all the maintenance events from AWS
    * keyword to look for in the exam

* can access all this info programatically via AWS Health API

* if have enabled AWS organizations -> can aggregate all these health events in one place


### Health Event Notifications
* can use event bridge or cloudwatch to react to changes for AWS health events in your AWS account
* AWS personal health will trigger an event which will be sent to even bridge or cloudwatch which will invoke some other service( SNS, lambda, kinesis, etc) 
* Use cases: notification, logging, trigger corrective actions
* can't be used to return public events from the even dashboard(??? look more into) 
* Example: Want to recieve email notification when EC2 instances are scheduled for updates


### GUI
* in website AWS console will have a list of all infrastructure related events both by you and AWS itself
* 
#  monitoring_and_alerting

## x-ray.md
* Anytime see distributed tracing and troubleshooting at the request level thing X-Ray
    * All you need to know for exam


### Extra info
* can get high level analysis and tracing capability of your application
* trace
    * how network calls are moving across infrastructure
    * trace requests across your microservices

* integrate with EC2, ECS, Beanstalk, Lambda, API Gateway, 
* X-ray agent can be installed on instances as well

* Be sure to enable X-Ray permissions for the X-Ray agent

#  monitoring_and_alerting

## eventbridge.md
### Eventbridge

* What is EventBridge?
  * A fully managed event bus service
  * Allows you to build event-driven applications using events from AWS services, SaaS apps, or custom sources

* Key Concepts:
  * Event Bus:
    * Default, Partner, or Custom
    * Receives and routes events
  * Rules:
    * Match incoming events using patterns
    * Route matched events to targets
  * Event Pattern:
    * JSON structure that defines what events to match (by service, type, resource, etc.)
  * Target:
    * AWS services like Lambda, Step Functions, SQS, SNS, Kinesis, etc.

* Sources of Events:
  * AWS services (e.g., EC2, CodePipeline, S3, DynamoDB)
  * SaaS partners (e.g., Zendesk, Datadog, PagerDuty)
  * Custom applications (via PutEvents API)

* Use Cases:
  * Orchestrate microservices
  * Trigger workflows (e.g., Lambda or Step Functions)
  * Audit and compliance tracking
  * Real-time data processing
  * Integrate SaaS tools with AWS services

* Features:
  * Schema registry (for event validation/discovery)
  * Archive and replay events
  * Event transformation (with input transformers)
  * Fine-grained access control with IAM


* how it works example:
    * S3 emits events (e.g., object created, deleted, restored)
    * If EventBridge is enabled for the bucket, those events are automatically sent to the EventBridge default event bus
        * no need for SNS or lambda intermediary
    * You write a rule in EventBridge to match those events and send them to a target (Lambda, SQS, etc.)








* formerly known as cloudwatch events


* periodic: schedule cron jobs in the cloud
    * trigger a lambda function at some period

* reactive: can set rules that react to a service doing something
    * i.e. a root user logs in
    * will send an email


* a lot of services can send to Event Bridge


* cloudtrails can intercept ANY API call made in your AWS accounts and the send to Event Bridge for further processing/notifying/alert/etc/

* Event bridge output is a json document that represents the details about your event

* This JSON document can be sent to a lot of services and used to trigger a lot of things(ECS, Lambda, SQS, Kinesis, etc.)

* can archive the events- indefintite or set time, 

* can replay these archived events-troubleshooting, debugging

### Event Bus

* event brige is default internal event bus
* also have a partner event bus

* Partner Event bus
    * AWS has integrated with third party partners and they send their events into your partner event bus
    * can react to changes happening outside of AWS

* Custom event bus-can define


### Schema Registry
* Event bridge recieves events from a lot of places
    * what do these events look like?
    * JSON
    * store in schema registry
    * event bridge anaylye events in bus, then infer the schema
    * Schema registry allows you to generate code for your application that can output events properly formatted to an specific schema
    * Schema can be versioned as well

###  resource based policy for EvBr
    * manage specific policies for a specific event bus
    * a speicific event bus can allow/deny from other region or other accounts

* Can have a central Event Bus for all your AWS accounts
    * these events will be aggregated

#  monitoring_and_alerting

## cloudwatch.md
* Cloudwatch Default Metrics
    * provided by many AWS services
    * by default for EC2 standard monitoring is 5 minutes
        * can enable detailed which gives you metrics every 1 minute
    * CPU, Network, 
    * RAM is NOT build in metric with standard 
    * to get memory will need to create a custom metric and use the Cloudwatch Unified agent

* Custom metric
    * Default Resolution is one minute
    * can enable high resolution mode and get that down to 1 second


* Cloudwatch Alarm integrations
    * can trigger these things (know this)
        * EC2 action (reboot, stop, terminate,recover)
        * autoscaling
        * SNS 
            * notifications (emails, chats, etc)
            * from SNS can also send to:
                * SQS
                * Lambda function
                    * can use this to trigger Route 53 to shift traffic away from instance with problems
        * can send alarm to EventBridge
            * Kinesis
            * Step Function
            * Lambda function
            * etc


* Cloudwatch Dashboards
    * Display metrics and Alarms
    * Show metrics of multiple regions

* Cloudwatch Synthetics Canary
    * configurable script that monitors your API's, URL's, Websites, etc.
    * Run some sort of health check inside your canary
    * Regularly run a check to reproduce customer behavior with a script to find issues before the customers does
    * Check availability and latency of endpoints
    * Can store the latency data and screenshots of UI
    * trigger a cloudwatch Alarm if there's issues
    * scripts written in node/python, with a headless Chrome browser included
    * Blueprints
        * heartbeat monitor
        * API canary(basic read write functions of APIs)
        * Broken Link Checker(pass in a URL and will ensure that all links are not 404)
        * Visual Monitoring(compare periodic screenshot with a baseline screenshot)
        * Canary Recorder   
            * used with Cloudwatch synthetics recorder
            * lets your record your actions on a website and generate a script to replay
        * GUI workflow builder
            * create, customize, and manage canary scripts visually and programmatically to monitor your applications and APIs.


### Cloudwatch Logs
* Sources: How to push data into CW logs 
    1. SDK
    2. Logs agent
        * Can be installed on EC2 or on prem hosts
    3. Unified Agent
    4. Integration with a service - some services have direct integrations with CS logs
        * ECS
        * Beanstalk*
        * Lambda
        * VPC flow logs
        * API gateway
        * Cloudtrail
        * Route53 - log DNS queries
* Log groups
    * give it any name you want that usually represents an application
* Log stream
    * inside a log group
    * Subdivide a log group up, different log files for example
* Can define log expiration policies(never expire, 30 days, etc.)
* can encrypt CW logs with KMS
* Can further send logs to other destination:
    * S3
    * Kinesis data stream, firehose
    * Lambda
    * Elastic Search via Lambda


* metric filters
    * can monitor the logs and when a condition occurs will increment the metric filter
    * essentially creates another metric datapoint
    * for example
        * find how many times a specific IP has occured
        * count the count of the occurence of the word ERROR 
    * can be used to trigger CW alarms

* Cloudwatch logs insight
    * can query logs in real time
    * can add queries to a CW dashboard


# VPC

## VPC-peering.md
* VPC Peering in AWS allows you to establish a direct network connection between two Virtual Private Clouds (VPCs). This connection enables instances in one VPC to communicate with instances in another as if they were in the same network. It works over AWS's private network infrastructure, providing secure and scalable connectivity.

* can be cross region

* send peering connection and both accepts
* then both VPC's need to configure routes/DNS to the respective peering connection


* VPC is non-edge allowed: cont' connect one VPC to resources that are on the edge THROUGH another VPC via peering
    * VPN
    * Direct Connect
    * Internet GW
    * NAT GW
    * Gateway VPC endpoint (s3 and dynamo)

* VPC is non-transitive
    * can't connect to another VPC VIA another VPC

* No overlapping CIDR in VPC's if trying to peer them
    * even just one, AWS will not allow!!!

* Data transfer charges apply for traffic sent across VPC peering connections, especially for cross-region traffic.


# VPC

## IGW.md
* Attachement scope: attached to VPC (not subnet)
* common configurations: can be attached to a VPC router or a NAT gateway

*  An Internet Gateway (IGW) in AWS only allows traffic originating from resources inside the VPC to which it is attached. This is a critical design principle for security and routing in AWS.

* The Internet Gateway (IGW) only allows outbound traffic from:
    * Instances in public subnets with public IPs.
    * Private subnets via a NAT Gateway for traffic originating within the VPC.

* Traffic coming from a VPN connection via a VGW is treated as "non-VPC-originating traffic" and is not allowed to flow through the IGW.


* workarounds:
    * NAT Instance
        * route traffic into an instance on the network which will then use the instances IP to send traffic via internet
        * this seems to be sort of a hack?
        * Note: NAT Gateway WILL NOT WORK
    * Transit Gateway
        * hub and spoke and can set routing table rules to route VPN traffic to an egress VPC with an IGW
# VPC

## local_zones.md
* place compute, storage, database close to end users to run latency sensitve applications
* extend your VPC to more locations
* EC2, RDS, ECS, EBS, ElastiCache, DirectConnect
* extend a normal region(us-east-1)
    * define a local zone in Boston for example
    * extend the VPC into this region and 
* 
# VPC

## VPN.md
### Site to Site VPN
* consists of a customer gate way(CGW) and virtual private gateway(VPG)
    * virtual private gateway also used for direct connect

* customer network - vpn appliance - customer gateway(aws) - virtual private gateway - vpc
* can either use static routing in the routing tables 
* or can use BGP
    * BGP propogates routes between networks
    * have to give each side of the connection an autonomouse 


* customer site <-> CGW <->VPN <-> VGW on VPC <-> NAT <-> IGW <-> internet
    * customer site  can't access internet, see IGW, doesn't allow off VPC traffic


* the reverse direction DOES work though
    * can access internet from VPC via the customer site
    * Internet <- customer site <-> CGW <-> VPN <-> VGW <-> VPC 


* VPN cloud hub
    * can connect a bunch of CGW to a single VPG
    * useful for if an company has a bunch of offices that all need VPN
    * useful for reduncany also



#### AWS client VPN
* it's a simple way to connect to your VPC via OpenVPN
* it will put an ENI for your local machine on one or more subnets of the VPC
* Essentially your machine is treated as an instance on the VPN
* can combine this with a Site to Site VPN inside the VPC to access on prem infrastructure in a corporate data center or some such from yor local laptop or client machine
* very important concept: it acts like your machine is ON the VPC
    * can access edge resources and peered resources
    * this means you can acceas resources on a peered VPC,  access internet via IGW, access corporate on prem, etc.



####  On Premise redundant connection
1. Site to Site Active connection
    * have two office locations connected to AWS via their own VPN/Direct Connect line
    * the two offices are connected with each other also separately from anything AWS related
    * if one of the offices lose VPN/Direct connection, can route the traffic through other office connection and then VPN/Direct connection to access AWS

2. Can also have varous flavors of VPN connectivity/Direct Connect via one or more offices all connected to each other for redundancy
# VPC

## VPC-general.md
* VPC segmentation
    * VPC created in region 
    * Anything with the word zone requires a subnet(local zone, wavelength zone, availability zone)
    

* Main types of connections into VPC
    * internet (via IGW and/or IGW)
    * VPC peering
    * direct connect
    * VPN


* Security types in VPC
    * NACL's are stateless
        * must declare both inbound and outbound rules
    * Security groups are stateful
        * if inbound allowed, outbound allowed

* Rules can filter by ip,port,dns,inbound/outbound, regex, etc
* allow, block, alert


* active flow inspection: dynamically inspect traffic live 
    * can get detailed like inspecting handshakes 
    * detect unusual traffic patterns
    * port scans

* can also send logs to s3, cloudwatch, kinesis for analysis

* Rules can be centrally managed cross account to apply to many VPC's


# VPC

## PrivateLink.md
* a private link
    * Puts a network interface (ENI) on the consumer's VPC 
    * ENI is associated to a private link endpoing on producer VPC
    * private link endpoint associated with NLB on the producers VPC
    * NLB is associated with the instance(s) providing the service


some uses:
    * can connect on prem service to a VPC with direct connect -> private link, that service now has an ip on the VPC
    * can create a VPC endpoint for your own custom service in another VPC



* service <-> NLB <-> private link endpoint in producer side <producer-consumer> ENI on consumer side <-> consumer 



* if want to share a single instance/service with another VPC (i.e. offering a customer a product)

* VPC peering would allow ALL instances in one VPC to talk to ALL instances in my VPC 
* NAT/internet GW...public internet has a bunch of problems

# VPC

## VPC-endpoints.md
#### AWS managed interface
* An AWS Managed Interface refers to an Elastic Network Interface (ENI) that is created and managed automatically by AWS to facilitate communication between AWS-managed services and resources within your Amazon Virtual Private Cloud (VPC). These interfaces provide seamless private connectivity for various AWS services.

* functions as a normal interface with security groups, flow logs, etc.

* Types:
    1. VPC Endpoint (Interface Endpoint)
    2. AWS Client VPN
    3. Elastic Load Balancer (ALB/NLB)
    4. AWS PrivateLink
    5. Network Firewall or Transit Gateway:

* Costs:
    * There are charges associated with the use of managed interfaces, such as data transfer costs and hourly charges for services like Interface Endpoints.





### Endpoints general
* connect a vpc to an AWS service 
* services normally have to access AWS resources via the public internet
* this opens up way to access aws resources on private aws network
* when add them DNS is automatically updated with the url to PRIVATE IP instead of public IP, overrides
* route table is also automatically updated
* very important: GW endpoints only work for things INSIDE A VPC. NOT TRANSITIVE


### gateway endpoint
* endpoint gateway is specifically for s3 and dynamo
* doesn't use interface
* in the routing table the target is the public ip's of the service and the destination is a vpce (vpc endpoint)

### VPC endpoint interface
* Is essentially an ENI in a subnet with an IP/security group that the whole subnet can send data to
* need to "enable DNS hostnames" and "enable DNS support"
* sharable so can be accessed from Direct Connect or Site to site VPN

#### Differences
Gateway Endpoint:
    Works at the route table level. i.e. acts like the service 
    Traffic is routed automatically to the Gateway Endpoint when the route table is updated.
    Access can be controlled using VPC policies and bucket/table policies.
    Does not support security groups.
    Is free


Interface Endpoint:
    Works at the application level.
    Applications or services must explicitly connect to the endpoint by using the endpoint's private IP address or domain name (resolved via private DNS).
    not free
    can have security groups


#### Gateway - Endpoint policies
* similar to a security group in purpose
* speicifc policies different than IAM or service specific policies
* note: sometimes it's good to add a full deny on the aws resource to anything not coming from the vpc endpoint
* this requires a condition statement
    * aws:sourceVpce: <some vpce id>
    * aws:sourceVpce: only works for vpc endpoint

* example: add a s3 bucket policy to the s3 bucket to deny any access with a condition not equals aws:sourceVpce

### Troubleshooting
* outbound security group on the instance are open , ie attached to the instance
* check route tables
* check DNS 
* check security groups if it's an non-gateway interface endpoint
* check VPC endpoint policy if it's a gateway
* check the actual AWS resource policy i.e. the policy attached to s3
* check IAM roles








# VPC

## direct-connect.md
* DEDICATED LINE between your Data Center and AWS
* traffic does not travel over public internet
* traffic does not go through ISP, so no payment to an ISP
* NOT redundant so will need setup to a second connection or VPN
* Connect to a single region!!!

* typicallly uses BGP and advertises the network of subset of network to the VPC

#### Physical Layter
* architecture
    * customer site -> direct connect hub -> virtual private gateway attached to the direct connect hub->vpc

* direct connect hub is structure located somewhere.

#### VIF
* virtual interface
* The VIF is the logical interface that AWS provides to route traffic
* A VIF (Virtual Interface) is on the AWS side of the Direct Connect connection. It is created and managed within AWS to define how traffic is routed between your on-premises network and AWS resources over the Direct Connect link.
* Your on-premises router communicates with the VIF using BGP for traffic routing.

* types:
    1. public VIF 
        * connect to public facing AWS endpoints like s3, EC2, many more
    2. private VIF - connect to private resources inside of VPC
        * EC2
        * VPC interface endpoints 
        * can then use an Interface VPC endpoint to connect to other servicea
            * this is a more private alternative to public VIF
        * associates with a VPG when it needs to connect to a VPC
            * VPG uses BGP and recieves BGP
    3. transit VIF - when using a Transit Gateway 


* When you create a Virtual Interface (VIF) in AWS Direct Connect, it will attach to your Direct Connect connection but not directly to a VPC. Instead, the VIF connects to a gateway (like a Virtual Private Gateway, or Direct Connect Gateway) that links the VIF to the VPC.

* a single Virtual Interface (VIF) cannot connect to multiple Virtual Private Gateways (VPGs) directly. A Private VIF is limited to a one-to-one connection with either:
    * A Virtual Private Gateway (VPG) (for a single VPC).
    * A Direct Connect Gateway (DX Gateway), which can provide access to multiple VPGs or VPCs via a Transit Gateway or directly to multiple VPG's.


#### Gateways
* transit gateway
    * transit VIF - when using a Transit Gateway 
    * A VIF cannot directly connect to a Transit Gateway. 
    * requires a Direct Connect Gateway to connect to a transit gateway
    * so the architecture is:
        * on prem -- direct connect -- direct connect gateway -- transit gateway -- numerous other things

* Direct Connect Gateway
    * associate a VIF with a DCGW
    * then must connect DCGW to a VPG or a Transit GW which then connect to VPC
    * has BGP for routing
    * There is a limit to the number of Virtual Private Gateways (VGWs) that a Direct Connect Gateway (DX Gateway) can connect to. Currently, a DX Gateway can connect to a maximum of 10 VGWs by default.

    * DCGW can connect to up to 10 VGW

* VPG
    * can connect a private VIF to a VPC directly via a VPG
    * limited to a single VPC connectivity
    * If you are connecting a Private VIF to a single VPC in the same region as the Direct Connect location, you can connect the Private VIF directly to the VPG.


#### Architectures
* on prem - direct connect - VIF - VPG - VPC
    * simple, connect a private VIF to a single VPG to a single VPC
* on prem - direct connect - VIF - DCGW - VPG(up to 10) - VPC  
    * connect up to 10 VPG which also means 10 separate VPC's
* on prem - direct connect - VIF - DCGW - Transit Gateway where anything goes

#### connection types
1. 
* A Dedicated Connection is a physical connection between your on-premises network and an AWS Direct Connect location.
* It is provisioned directly by AWS.
* Ownership: You own and manage the physical connection.
* dedicated non-scalable bandwidth requires upgrade for more


2. 
* A Hosted Connection is provisioned by an AWS Partner who owns the physical Direct Connect infrastructure.
* The partner provides logical connectivity to your organization.
* The AWS Partner provisions the connection, making it simpler to set up.
* You do not need to deal with physical cabling or colocations.
* The physical connection is shared between multiple customers, with each getting a logically isolated portion.
* can scale the bandwidth because the aws partner can logically allocate you more


* takes at least a month for a direct connect link


#### encryption
* direct connect is not encrypted
* however, it IS private on a private line
* to encrypt would have to use VPN as well

* would use the direct connect as the physical infrastructure and the VPN would work on top of that


#### Link Aggregation Group (LAG)
* can create a LAG by having multiple direct connect hard lines and summing them up into one logical one
* this increase speed and failover
* can aggregate up to 4 connections
* must have same bandwidth and terminate at same direct connect location
* can set minimum number of connections for lag to function


#### Connection via VPG
* can connect a private VIF to a VPG in a VPC
* single connection to a single VPC
* for multiple VPC connection would need a VPG in each VPC




#### Other
* can use transit gateway with direct connect but that will only link things in the same region
* can use a direct connect gateway to link single direct connect vif to multiple transit gateways in multiple regions


####  direct connect-sitelink

* if two offices each with their own direct connect link to AWS
* each of these offices is connected to a direct connect location in a different region
* can use DCG-sitelink so they can speak with each other and bypass going thru AWS
* the direct connections will go to AWS then hit the DCG and then sent back out to the other location, avoiding 
# VPC

## TGW.md

* Transit Gateway solves these problems 
    * allows edge connectivity for VPC's
    * allows transitivity of VPC's
    * hub and spoke
    * connect a bunch of VPC's, VPN'x, Direct Connects, NAT, Gateways, etc. to centralized Transit Gateway
    * have to define routing tables



* Locations
    * Transit gateway is REGIONAL
    * Can share single TGW cross account using RAM(resource access manager) but only to resources in same region!!
        * Cross-region sharing: TGWs are regional, so sharing is limited to accounts within the same region.

    * For cross region:
        * Can create multiple TGWS in multiple regions and PEER them (non-transitive, requires TGW in ea. region, uses AWS backbone)


* TGW supports IP multicast


* TGW allows transitivity of:
    * NAT GW
    * NLB
    * PrivateLink
    * EFS
    * VPN
    * Direct Connect
    * Internet GW
    * NAT GW
    * Gateway VPC endpoint (s3 and dynamo)
    * more?



Example Scenario:
-------
    Account A has VPCs in us-east-1 and us-west-2.
    Account B also has VPCs in us-east-1 and us-west-2.

For each region:

    Within us-east-1:
        Create a TGW in us-east-1 and share it between the accounts using RAM.
        Attach all us-east-1 VPCs to this TGW.

    Within us-west-2:
        Create another TGW in us-west-2 and share it similarly.

To enable communication between VPCs across us-east-1 and us-west-2, set up TGW Peering between the TGWs in the two regions.




----
* Further info
AWS Transit Gateway supports inter-region peering, enabling seamless connectivity between VPCs and on-premises networks across AWS regions. Here’s an explanation of how Transit Gateway works across regions:
Key Features of Inter-Region Transit Gateway Peering:

    Peering Connections:
        Transit Gateways in different regions can be connected via a peering connection.
        Traffic is routed through the AWS global network backbone, ensuring low latency and high performance.

    High Availability:
        Transit Gateways are regionally redundant and fault-tolerant.
        The inter-region peering connection is also highly available and scales automatically.

    Non-Transitive Routing:
        Like VPC peering, inter-region Transit Gateway peering is non-transitive.
        If you connect Transit Gateway A to Transit Gateway B, and Transit Gateway B to Transit Gateway C, traffic cannot flow from A to C.

    Encrypted Communication:
        All traffic over inter-region peering connections is encrypted using AWS backbone infrastructure.
        No need to configure additional encryption mechanisms.

    No Bandwidth Charges for Peering:
        You pay for data transfer costs (based on inter-region data transfer rates) but there are no separate charges for peering connections.
# VPC

## VPC-logging.md
### VPC flow logs
* capture traffic info

* can monitor:
    * vpc 
    * subnet 
    * ENI 
    * anything that can be an AWS managed interface(ENI)
        * ELB, RDS, NATGW, etc. etc.

* traffic can go into S3, cloudwatch, kinesis
* can query with Athena on S3 or cloudwatch insights

* examples of monitoring:
    * success or rejection of traffic by a security group or NAC
    * analytics of usage behavior, malicious behavior, port scanning etc


* can send flow logs to cloudwatch log service
    * output flow logs to cloudwatch and analyze with:
        * cloudwatch contributor insights: 
            * can do data analysis i.e. top 10 interfaces pulling the most network
            
        * cloudwatch metric filter that will go off when logs hit some mettic
            * then send to CW alarm -> SNS
            * i.e. if too much ssh or somethingg
    * output flow logs to S3 bucket then analyze with Amazon Athena 
# VPC

## NATGW.md
#### NAT gateway
* Attached to SUBNET (not entire VPC)
* Always attached via managed ENI(therefore: can monitor via via flow logs)
* will see inbound traffic on the NAT public IP (if SG and NACL allows) but that's the demarcation and it's dropped there

#### Traffic restriction

Outbound Traffic to the Internet:
A NAT Gateway is designed to allow instances in a private subnet to initiate outbound connections to the internet or other AWS services. This is its primary use case.

Inbound Traffic Restrictions:

    NAT Gateways block inbound traffic initiated from the internet.
    Even if there is a public IP address associated with the NAT Gateway, it will not accept unsolicited inbound connections.

NAT Gateways are stateful. This means they will allow return traffic for connections that were initiated by instances in the private subnet.

#### NATGW is 1:N NAT model

AWS NAT Gateway aligns with the 1:N NAT model:

    One Elastic IP Address (EIP):
    The NAT Gateway uses a single public IP (or more in High Availability setups) to handle outbound traffic from multiple private IP addresses in a private subnet.

    Port Translation:
    NAT Gateway dynamically maps each outbound connection from a private IP to a unique combination of the public IP and a port number.

    Return Traffic:
    The NAT Gateway tracks the state of outbound connections and allows return traffic based on these mappings.



#### NAT Theory
Yes, you're describing the two main types of NAT (Network Address Translation) configurations: 1:1 NAT and 1:N (or many-to-one) NAT. These are common in networking scenarios and are relevant to how NAT is implemented in various environments, including AWS.
1:1 NAT (Static NAT or One-to-One Mapping)

    How It Works:
    Each private IP address is mapped to a unique public IP address. This is a direct, one-to-one relationship between internal and external IPs.
    Use Case:
        Scenarios where a consistent public IP is needed for a specific internal resource (e.g., hosting a service that requires the same IP for client access or whitelisting).
        Typically used in setups where there are enough public IPs available for each internal device requiring external access.
    Example in AWS:
    Not directly supported by AWS NAT Gateway, but it can be achieved with an Elastic IP (EIP) and routing rules for specific instances.

1:N NAT (Dynamic NAT or Many-to-One Mapping)

    How It Works:
    A single public IP address is shared among multiple private IP addresses. The NAT device differentiates traffic by dynamically assigning a unique port number to each connection.
    Use Case:
        Most common for internet access in private networks (e.g., home routers, enterprise networks, AWS NAT Gateway).
        Optimizes the use of public IPs by allowing many private devices to access the internet using one or a few public IPs.
    Example in AWS:
    The AWS NAT Gateway operates in a 1:N model, using a single Elastic IP address to manage traffic for multiple private subnet resources.



# VPC

## VPG.md
* A Virtual Private Gateway (VPG), often abbreviated as VGW, is an AWS-managed network gateway that enables connectivity between your Amazon Virtual Private Cloud (VPC) and external networks. 

It is primarily used for:
* setting up Site-to-Site VPN connections
* integrating with AWS Direct Connect.
    * it's what the VIF associates with to connect to the VPC

Supports both:

    Dynamic routing: Uses BGP (Border Gateway Protocol) for route propagation.
    Static routing: Manually defined routes.
# VPC

## wavelength.md
* AWS Wavelength is a service designed to bring AWS compute and storage resources closer to end-users by running AWS infrastructure at the edge of mobile carrier networks.

* Wavelength Zones are AWS infrastructure deployed directly in the data centers of telecommunication providers (like Verizon, Vodafone, and SK Telecom).

* It's a zone inside of a parent region(AZ)

* These zones are physically closer to mobile devices, reducing the round-trip time for data sent from devices to the application backend.

* By minimizing the distance between users and compute resources, applications can achieve single-digit millisecond latencies.

* Note: It's just a subset of AWS services in these zones that are getting the extremely low latency.
    * AWS Wavelength is designed for low-latency edge use cases, so it only includes the most critical compute, storage, and networking services needed for processing data and handling latency-sensitive workloads.
    * compute: EC2, ECS, EKS
    * storage: EBS
    * networking: VPC, ELB
    * No direct support for RDS, DynamoDB, or Aurora in Wavelength Zones. These can be accessed via the parent AWS region.
    * Services like AWS Lambda, Step Functions, or SageMaker are not available directly in Wavelength Zones.
    * No direct support for Amazon S3 or Glacier in Wavelength Zones, but you can connect to these in the parent region.
    * Services like Amazon Athena, EMR, or Redshift are not natively supported in Wavelength.
    * Applications in Wavelength Zones can connect back to the full suite of AWS services in the parent region, such as databases, analytics, and machine learning services.

* essentially having an AWS zone with AWS service access on the edge of a 5G network
* really low latency for people accessing AWS resources from a 5G network
* traffic never leaves the netw


* because it's 5G use cases are numerous
    * smart cities, connected vehicles, live streams, AR/VR, real time gaming, etc
# VPC

## outposts.md
#### Hybrid cloud
* business that have on-prem infra alongside a cloud infra
* will have two ways of dealing with IT systems, skillsets, API,etc.
* AWS created outposts


#### outpost
* AWS will come setup and manage "Outpost racks" at your local business
    * will have on-prem infra with AWS services setup
    * same AWS infra tools/services but on prem

* can use same skills/knowledge base and still have on-prem benefits

* Tradeoff: 
    * you are responsible for physical security because that rack is on your local system
    * Only a subset of AWS services work on outpost local on-prem

* Benefits: 
    * speed
    * migrations
    * security of data because it's local
    * low latency


* to connect to your aws services from dash 
    * can either use an outposts link
    * or do a sync to the cloud



# migration

## elastic_disaster_recovery.md
* AWS Elastic Disaster Recovery (AWS DRS)

  * What It Is:
    * Lets you quickly recover on-premises or cloud-based servers to AWS during a disaster

  * Key Features:
    * Continuous replication using lightweight agents
    * Low RTO (minutes) and RPO (seconds)
    * Non-disruptive testing of recovery plans
    * Automated orchestration to launch EC2 recovery instances
    * Supports Windows and Linux

  * Use Cases:
    * Disaster recovery for:
      * On-premises servers
      * EC2 instances across regions/accounts
      * VMware, Hyper-V, physical servers

  * Workflow Overview:
    * Install agent on source machines
    * Data continuously replicates to AWS
    * Failover event triggers recovery in minutes
    * Option to fail back to original site

# migration

## AWS_backup.md
* AWS managed service
* centrally manage and automate AWS backups across AWS services
* no need to create custom scripts and manual processes
* want a central view of your backup strategy
* supported services: all database related services, all file system services, and more


* supports cross region backups
    * can have your backup pushed to another region (disaster recovery)
* supports cross account backups


* supports point in time recovery (PITR) for supported services
* on demand and scheduled backups
* tag based backup policies
* you can create backup policies known as backup plans 
    * i.e. define frequency
    * backup window
    * transition to cold storage?
    * retention period of backups

### AWS backup vault lock
* option to enable
* enforce a WORM (write once read many) state for all the backups you store in your backup vault
* can't delete or modify backups
* even root user can't delete/modify backups when enabled

# migration

## fault_injector.md
### Fault injector simulator service

* based on chaos engineering
* randomly generate faults to ensure our architecture is solid
* help find hidden bugs/bottlenecks
* some services supported
    * EC2
    * ECS
    * EKS
    * RDS


* will create a template inside Fault Injector Simulator service
* start the experiment
* monitor with cloudwatch or event bridge
* then stop the experiment
* FIS will output a report 
    * performance
    * observibibily
    * resiliency
    * etc.
# migration

## cart.md
### Cloud adoption readiness tool

* helps organizations develop efficient and effective plans for cloud adoption and migrations
* get a score chart
* transform idea of moving to cloud into a detailed plan that follows AWS best practices


* answer a set of questions across six different perspectives(business, people, process, platform, operations, security)
* gives you a chart and custom report to give you your level of readienss
* give some reccomendations for following AWS best practices for migration



# migration

## migration_evaluator.md
* helps build a  data driven business case for migration to AWS
* provide clear baseline of what your organization is running today
* install agentless collector to conduct broadbased discovery of all on prem infrastructure
* or can import data from 3rd party
* take snapshot of on premise footprint, server dependencies
* analyze current state of on prem, define target state in AWS, develop migration plan
* all this imported data will give you QuickInsights reports for customized cost insights

# migration

## migration_services.md
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


# migration

## storage_gateway.md

* USE CASE: provide NFS/SMB interface for on-prem or VPC hosts
* Also can cache locally either hot cache or entire s3 backend


* File Gateway: each file is a separate S3 object.
  * File path = S3 object key.
  * Metadata stored as object metadata.

* Volume Gateway: block storage backed by S3.
  * Data written as iSCSI block volumes.
  * Snapshots stored in S3 as EBS snapshots.
  * can't recover individual files without restoring entire volume

* Tape Gateway: virtual tapes stored in S3/Glacier.
  * Emulates tape libraries for backup apps.
  * Tapes are stored as virtual tape objects in S3.
  * can't recover individual files without restoring entire volume



### S3 File gateway
* USE CASE: mount S3 as file systems on prem
* can use with any storage class but glacier
* NFS or SMB integration
* can define IAM roles 
* can still define life cycle policy and intelligent tiering like any s3 bucket 
    * since still backed by an s3 bucket
* SMB protocol will allow use of AD for user auth and access control


### FSx File gateway
* discontinued 
* FSx for windows is already mountable natively
* the only advantage is a local cache in on-prem environment to give you low latency access


### Volume gateway
* USE CASE: backup volumes of on premise server
* Block storage using the iSCSI protocol backed by S3
* backed by EBS snapshots for backup/restore ON PREM
* two type:
    1. low latency - has a cache for most recent files on prem
    2. stored volume - entire dataset on premesis, with scheduled backup to s3



### Tape gateway
* USE CASE: backup tape library to the cloud
* backs up using iSCSI interface
* works with leading software vendors
* can store in s3 and/or glacier


### Gateways
* theres a software appliance you can run as a VM
* there's a hardware appliance you can get from AWS also
    * primarily if you don't have virtualization on premesis
* works with all of the gateways
* goes in a rack
* helpful for daily NFS backups in small data centers



### Useful architectures
* can host a gateway on-prem and one in AWS VPC and both attached to same s3 bucket
    * useful for migrating applications to the cloud

* can mount same bucket in differnt locations as a shared file system

* can still use FULL s3 funcitonality with storage gateway   
    * lambda events
    * analytics with: athena, redshift spectrum, EMR
    * cross region replication for backup
    * any other s3 functionality available in AWS
    * backup 
    * lifecycle policies - to move data to lower cost storage

* Read only replicas - can connect it to some server which writes to cloud and enable read only so that anything else mounting that bucket will not works

* versioning
    * can enable versioning for restore of earlier version of data
    * restore entire file system to previous version!
    * will need to trigger a sync locally!!!

* enable s3 object lock
    * WORM - write once read many
    * always creates a new version for any change that way will never lose any data
# migration

## 7_Rs.md
* 1. Rehost ("Lift & Shift")  
  Move the application as-is to the cloud without significant changes. Quickest, often automated with tools like AWS Migration Hub or Server Migration Service (SMS).

* 2. Replatform ("Lift, Tinker & Shift")  
  Make minimal changes (e.g., change the OS, switch databases, or move to managed services like RDS instead of self-hosted MySQL).

* 3. Repurchase ("Drop & Shop")  
  Replace the app with a SaaS solution. For example, move from a self-hosted CRM to Salesforce or Workday.

* 4. Refactor / Re-architect  
  Redesign the application to be cloud-native (e.g., move from monolith to microservices, use serverless or containers). Usually the most effort, but unlocks max cloud benefits.

* 5. Retire  
  Decommission unused or obsolete apps. No need to migrate something no one uses anymore!

* 6. Retain ("Revisit")  
  Keep the app as-is, on-premises or in a hybrid setup — at least for now. Often used for compliance or technical constraints.

* 7. Relocate  
  Move entire VMs or infrastructures to the cloud without purchasing new hardware — like VMware Cloud on AWS or AWS Snowball. Faster than rehosting, but keeps your architecture the same.

# migration

## snowball.md
* USE CASE 1: move large amounts of data
    * portable device to collect data at the edge and bring back into AWS
    * will recieve a device in the mail, you load, then ship back to AWS
    * secure
    * workaround for large datasets or slow connections
        * petabytes
    * rule of thumb -> if take longer than 1 week then use snowball

* USE CASE 2: process large amounts of data on the edge
    * truck on road, ship at sea, mining station underground, etc.
    * no or limited access to internet/compute power
    * snowball device has hundreds of gigs of ram and over 100 cpus
    * can run ec2 instance or lambda functions at the edge
    * preprocess data, machine learning, transcode media




### Improve transfer performance for snowfamily devices
* perform multiple write operations at one time - from multiple terminals
* transfer small files in batches - zip up small files together until at least 1MB
* don't perform operations on file during transfer
* reduce local network use
* eliminate uneccesary hops, plug directly to computer
* data transfer rate:
    * via file interface: 25 - 40 MB/s
    * via S3 adaptor for snowball: 250MB - 400MB /s
    

### Can integrate snowball and DMS
    * large data migrations may have TB to PB of data
    * Steps:
        1. use AWS SCT to extract data locally and move to an snowball edge device
        2. ship back to AWS
        3. AWS will load data into s3 
        4. DMS kicks in, takes the files from S3 and moves them to target data store
    * if use CDC (change data capture) any updates happening in on prem data source will be replicated over to the destination data store


# migration

## disaster_recovery.md
* SUPER IMPORTANT



* Disaster is any event that has negative impact on companies buisness continuity or finances
* DR is about preparing/recovering from disaster

* what kinds of DR are available?
    * on premise-traditional, very expensive
    * hybrid -> on premise using cloud recovery with hybrid recovery
    * cloud -> AWS region to different AWS region

* RPO - recovery point objective
    * how often you run backups
    * time between RPO and disaster is a data loss

* RTO - recovery time objective
    * when you recover from your disaster how much downtime between disaster and recovery
    * essentially downtime


* want RPO and RTO to be as small as possible
* as you reduce RPO and RTO you increase cost


* listed in order from slower to faster RTO and lower to higher cost
    * Backup and Restore
    * Pilot light
    * Warm standby
    * Hot site / multi site approach




* backup/restore
    * manually sending data to a data store that then needs to be recovered
    * objects -> s3 via storage gateway or snowball -> s3 -> lifecycle policy -> glacier
        * snowball RPO is on the order of days as it has to be mailed
    * databases, redshift, RDS, EBS -> snapshots
        * RPO based on snapshot frequency
    * application instance -> create AMIs 
    * all of this is cheap
    * takes a long time to recover 
    * high RPO high RTO

* pilot light
    * a small version of the app is running in the cloud or the data is highly available so can quickly spin up instances 
    * can point route53 at the new system
    * critical core 
    * same as backup and restore except already have core systems running
    * more expensive because have instances and data stores constantly running

* warm standby
    * full system up and running but at minimum size 
    * needs scaling to production load on disaster
    * for example: have minimum capacity ASG ready to scale and an RDS replica with route 53 ready to failover

* multi site
    * multiple production scale running
    * Note: will be using both of the sites at all times
    * can be on prem, cloud, or hybrid with multi sites being one any of these 

* all cloud
    * this is the same kind of architecture as multi site except without any on prem
    * there are additional improvements 
        * Aurora global database


*  a lot of customers opt for “Disaster Avoidance” capabilities, rather than “Disaster Recovery”. This is a perfectly viable approach, and essentially aims to implement highly-robust configurations spanning multiple locations to prevent downtime in the event of a hardware or geographical outage, and therefore avoiding a disaster scenario.

*### general 

 backup resources
    * snapshots: EBS, RDS
    * regular pushes to s3, lifecycle policies, glacier, cross region replication
    * from on prem to cloud->snowball or storage gateway
* high availability
    * route53 to route traffic between sites/regions
    * multi-AZ services, i.e. RDS, elasticache, efs, s3, aurora global
    * site to site VPN as a recovery for failure of direct connect service
* replication
    * RDS, Aurora global
    * database replication from on prem to AWS RDS
    * storage gateway
* automation
    * cloudformation / Beanstalk can create entire new environment in the cloud
    * recover reboot instances in EC2 if cloudwatch alarms fail
    * aws lambda for customized automation
* chaos testing
    * how to know if solution will work?
    * introduce chaos
    * netflix - has a program called 'simian army' randomly terminating EC2 instances
    * introduce chaos to ensure infrastructure is capable of surviving failures
# databases

## dynamo.md
* NoSQL database 
* fully managed
* massive scale 1,000,000 rps
* similar architecture to apache cassandra
    * can migrate from cassandra to dynamo
* max object size is 400kb
* capacity
    * provisioned mode: 
        * specify how many write capacity units(WCU)
        * specify how many read capacity units (RCU)
        * if want autoscaling on/off 
    * on-demand
        * pay for every write/read
        * better for more unpredicatable workload
* supports CRUD
* supports transaction across multiple tables(ACID support)
* backups/point in time recovery
* Table classes:
    * standard
    * Infrequent Access(IA)

#### STructure
* made up of tables
* each table has a primary key(decided at creation time)
* each table can have infinite number of rows
* each item has attributes(columns)
* data types: string, number, binary, boolean, mull
* documet types: list, map
* set types: string set, number set, binary set

#### Primary key
1. Partition key only (hash)
    * each row has unique primary key
    * each primary key must be diverse so that the data is distributed
        * want a complex random hash that works as a way to parition the data on shards

2. can use a composite primary key
    * partition key + sort key
    * the combination must be unique
    * partition key doesn't have to be unique
    * data will still be grouped by partition key
    * sort key also called a range key
    * example:
        * user_id is partition key
        * job_title is sort key
    * another good sort key is a timestamp

#### Objects
* object = partition key + sort key(optional) + attributes
    * somewhat equivalent to a row 
    * unlike relational each row can have different attributes/colums

1. DynamoDB Object:
    * Represents an item in a table.
    * Each item is a collection of attributes (key-value pairs).
    * Items do not need to have the same attributes (schema flexibility).
    * Includes a primary key (partition key or partition key + sort key) to uniquely identify each item.

2. Relational Database Row:
    * Represents a single record in a table.
    * Each row must conform to the table's schema (fixed set of columns).
    * Primary key (or unique identifier) is often required but structured differently (e.g., composite keys).


#### Indexes
* LSI (local secondary index)
    * Suppose you have a table of users and their orders. The default sort key might be the order date, but you also want to query orders by their status. An LSI lets you create an alternate index that sorts orders by status while still using the user ID as the partition key.

    * LSIs are useful when you need multiple ways to query the same data but within the same partition key scope.

    * LSI - local secondary index
        * keep the same primary key
        * select alternative sort key
        * the LSI must be defined at table creation time    

    * DynamoDB restricts each table to a maximum of 5 LSIs, and all LSIs must share the same partition key as the base table but can have different sort keys.

    * LSIs cannot be added after the table is created and are limited to 5.

* GSI (global secondary index)
    *  GSIs can be created at any time and are not restricted to sharing the same partition key as the base table.
    * A GSI lets you define a completely new partition key and/or sort key for querying data.
    * allows searching with both a new primary key and new sort key
    * GSIs allow you to define entirely new partition keys and sort keys for querying your table in different ways. 

#### Querying
* can only query on an existing index
* must query first on partition key
* you cannot perform a query in DynamoDB where the partition key is unspecified or matches "any" value.
* a query operation always requires an exact match on the partition key.
* if a sort key is present in a DynamoDB table or index, you can ignore it in a query. When querying a table or a Global Secondary Index (GSI) that includes a sort key, you only need to specify the partition key. If you omit the sort key in your query, DynamoDB will return all items that match the partition key, regardless of the sort key values.
* can then filter that even further with sort key if desired
* if want all of a certain file type must have a GSI with partition key as fileType
* if want all of a certain date range can have a GSI with date a partition key
* can have a dummy column with all values the same as partition key to return ALL objects, then use a sort key to sort that
    * but why?


#### Dynamo streams
* Record Size Limit
  * Each stream record is limited to 1 MB
  * If the record exceeds 1 MB, it will not be added to the stream

* Shard Throughput Limits
  * Per shard:
    * Up to 2 MB/second read throughput
    * Up to 5 read requests/second
  * DynamoDB will create more shards automatically if needed

* Stream Retention
  * Records are retained for 24 hours

* Lambda Invocation Size (if using Lambda triggers)
  * Maximum of 6 MB per batch event payload



#### Important features
* TTL- can make a row expire after certain amount of time
* Dynamo Streams    
    * react to changes to tables in real time
    * can be ready Lamda, EC2
    * basically when a table changes, that change is sent somewhere to be processed like lambda or kinesis

* Global Tables
    * cross region replication
    * table replication across all or many regions
    * useful for low latency
    * useful for disaster recovery with low RTO
    * requires streams to be enabled
    * all changes replicated across regions

* the stream can send the change to kinesis
    * can filter, aggregate, transform
    * can send to data analytics
    * can send to data warehouse(s3, redshift, etc.)


#### Architecture ideas
* index s3
    * can use s3 events to send s3 object metadata to lambda which then writes to dynamo
    * set LSI on date, size, type and can query based on them
    * set primary index on object id (or bucket) 
    * can set a GSI on filetype with someother column as sort type to find all objects of a certain file type


#### Dynamo DAX
* dynamo db accelerator
* seamless cache for dynamo, no applicaiton rewrite, write go through DAX to Dynamo
* microsecond latency for cache reads/queries
* solves the hot key problem where if a certain r ow is popular will get throttling
    * caching handles this problem
* by default data cached for 5 minutes in DAX (TTL)
* up to 10 nodes in DAX cluster, 3 reccomended for production use
* multi AZ
* secure: encryption at rest,


#### DAx vs elasticache
* anytime you need to access Dynamo use DAX 100% of time
* DAX has no code changes
* after computation(filter, aggregate, transform) use elasticache 
* DAX = individual object cache, query/scan cache
* Elasticache = whatever you want to put in it
# databases

## RDS.md
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


# databases

## opensearch.md
* Amazon opensearch(Elastic Search is the old name)
* Kibana is now open search dashboard
* Managed version of OpenSearch(open source project, fork of ElasticSearch)
* two modes 
    * managed cluster(see concepts.md for what this means)
    * serverless cluster

* use cases
    * log analytics
    * monitoring )
    * security analytics
    * clickstream analytics
    * indexing


* opensearch + opensearch dashboards + Logstash
    * opensearch provides seach/indexing capability

* opensearch dashboard (used to be Kibana)
    * real time dashboards on top of OpenSearch data
    * alternative to cloudwatch dashboards
* * 
Logstash    
    * log ingestion mechanism
    * requires the logstash agent
    * alternative to cloudwatch logs

* once data in opensearch can create own API to search items, hosted on an EC2 instance
* once items are searched, can link to the actual record in DynamoDB table

#### Architecture
* All data sent to Dynamo/Kinesis can be sent to OpenSearch
* data source -> dynamo -> dynamo stream -> lambda -> opensearch 
* data source -> kinesis data stream -> kinesis fire hose -> opensearch
* can search data in opensearch and then link to the data in dynamo

* cloudwatch logs -> subscription filter -> lambda -> opensearch
* cloudwatch logs -> subscription filter -> kinesis firehose -> opensearch


# databases

## DMS.md
* AWS Database Migration Service (DMS) is a fully managed service provided by Amazon Web Services that helps migrate databases from one source to another with minimal downtime. It supports migrations between various database types, including relational databases, NoSQL databases, and data warehouses.

* AWS DMS simplifies database migrations, especially for organizations moving workloads to the cloud or modernizing their database infrastructure, with minimal downtime and effort.

* AWS DMS uses change data capture (CDC) to replicate ongoing changes during the migration, ensuring that the source database remains fully operational.

* AWS handles all infrastructure management, scaling, and monitoring for the migration process.

* When migrating between heterogeneous databases(different), AWS DMS can work with the AWS Schema Conversion Tool (SCT) to convert database schemas and code automatically.

* can customize migrations
    * You can filter data, transform it, and perform partial migrations based on your requirements.
# databases

## aurora.md
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


# databases

## aurora_serverless.md
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


# storage

## datasync.md
* use case:
    * syncronize data
    * move large amount of data from one place to another

* move from:    
    * on prem <-> AWS
    * other cloud <-> AWS
    * AWS <-> AWS
    * will sync in either direction

* agent 
    * If on prem or another cloud, will need to install the datasync agent!!!
    * AWS -> AWS no agent needed
    * will give the datasync agent connection info to data sync service 
        * then configure inside of datasync where to send the data from there

* services can sync to in AWS
    * s3 (ANY STORAGE CLASS)
    * EFS
    * FSx

* replication can be hourly, weekly, daily

* File permisssion and metadata are preserved (NFS/POSIX, SMB)

* one agent task can use up to 10 GBps
* can setup a bandwidth limit


* If don't have network bandwidth to sync the data
    * will need to use AWS Snowcone device
    * Snowcone device has the agent preinstalled
    * I.E. sync data to snow cone
    * transport snowcone to AWS sync data from snowcone

* sync between different AWS storage services (s3, EFS, FSx)


* the data is diffed after initial copy is made

* can transfer live data
    * DataSync supports transferring files even when they are being read or written by your applications.
    * During incremental transfers, it only copies changed or new files after the initial transfer, minimizing disruptions.

* transfer options:
    * can have a public VIF directly to datasync via public internet
    * or can go through direct connect private VIF into a VPC and use a VPC private endpoint interface
# storage

## FSx.md
* launch 3rd party file systems as FULLY MANAGED service
    * lustre
    * windows file server
    * OpenZFS
    * NetApp ONTAP

* AWS fully manages the infrastructure, scaling, and maintenance, freeing you from managing your own ZFS servers.
* Seamless integration with AWS services like AWS Backup, AWS DataSync, and CloudWatch.


* Supports multi-AZ, backups, encryption, and monitoring
* Fully managed by AWS (no hardware, patching, etc.)

* Unlike S3 (object storage) or EBS (block storage), FSx provides file storage, which is ideal when you need things like POSIX-compliant file systems, Windows file shares, or high-speed HPC workloads.





### Use Cases - KNOW
* FSx for Windows File Server  
  * Use Case: Windows-based applications needing SMB, NTFS, Active Directory, or Windows ACLs  
  * Example: File shares, Microsoft SQL Server, home directories

* FSx for Lustre  
  * Use Case: High-performance compute, ML training, big data analytics, media rendering  
  * Example: EC2-based HPC jobs needing fast, parallel access to S3 data

* FSx for NetApp ONTAP  
  * Use Case: Enterprise-grade shared storage with NFS/SMB/iSCSI, snapshots, deduplication  
  * Example: Hybrid cloud storage, VMware workloads, shared storage across platforms

* FSx for OpenZFS  
  * Use Case: Linux workloads needing POSIX compliance, ZFS features like snapshots and clones  
  * Example: Developer environments, CI/CD pipelines, Linux-based applications









### More detail don't really need to know I dont think

#### FSx for Windows File Server 
* USE CASE: Windows-based applications needing SMB, NTFS, Active Directory, or Windows ACLs. Think file shares, SQL Server.
* fully managed
* supports SMB and NTFS, Active Directory, ACL's, user quotas
* can also be mounted on EC2 Linux instances
* supports microsoft distributed file system (DFS) namespaces(group files across multiple file systems)
* can use
    * SSD (faster)
    * HDD (cheaper)
* access from on pre using VPN or Direct Connect
* can be multi AZ for high availability
* data backed up daily to S3 for disaster recovery via scripts(no native integration with S3)
* no point in time instant cloning



#### FSx for Lustre
* USE CASE: High performance compute (HPC), ML training, media rendering, big data workloads. Can integrate with S3.
* disributed file system for large scale computing
* lustre = linux cluster
* Machine learning and HPC (high performance computing)
* storage
    * SSD - low latency, small 
    * HDD - thoughput intensive workloads
* seamless native integration with S3
    * can READ/WRITE S3 as a file system
    * can write result of computation back to S3
* no point in time instant cloning

* deployment options
    * scratch file system
        * temporary storage
        * only a single copy of file system, data is not replicated
        * faster: 6 times the performance of persistent FS
        * cheaper
        * uses: short term processing, cheap

    * persistent file system
        * long term storage
        * replicated in same AZ
            * files replaced within minutes
        * use case: long term processing, sensitive data

* data lazy loading
    * When you link an Amazon S3 bucket to an FSx for Lustre file system (using the ImportPath parameter), only the metadata about the files in the S3 bucket is loaded into the Lustre file system.
    * The actual file content is fetched from the S3 bucket only when the file is accessed for the first time (e.g., read or write operations).
    * Once fetched, the file data is cached in the Lustre file system for subsequent access.
    * if have all data in S3 
    * can start data processing right away without the full dataset being brought into lustre
    * only the data currently being processed is brought over to the Lustre FS
    * reduces transfer costs out of S3
    * eseentially lustre is a durable cache

#### FSx for NetApp ONTAP
* USE CASE: Enterprise workloads needing multi-protocol access (SMB, NFS, iSCSI), snapshots, data deduplication, hybrid/multi-cloud setups.
* compatible with NFS, SMB, iSCSI protocol
* use cases: used for workloads that are already running ONTAP or NFS
* very broad compatibility
    * works with windows, linux, mac, essentially any OS
* autoscaling- storage shrinks/grows automatically
* snapshots, replication, low-cost, compression, can do data de-duplication(find duplicates fo files)
* point in time instant cloning 
    * nice for testing new ideas: can clone an FS and now have a staging file system for a new direction
* main use case: move workloads running on ONTAP to AWS

#### FSx for OpenZFS
* USE CASE: Linux apps needing POSIX-compliant storage, ZFS features, snapshots, clones.
* compatible with NFS
* main use case: move workloads running on ZFS to AWS
* broad compatibility (linux, mac, windows)
* snapshot, compression, low cost, (no data deduplication)
* point in time instant cloning

# storage

## EFS.md
* managed Network File System
* note: NFS only works on Linux does NOT work on Windows
* NFS v4.1
* encryption at rest with KMS
* posix files system with standard (linux) file system api
* can attach to more than one EC2 instance
    * can be useful for autoscaling or load balancing etc.

#### Price
* more expensive than EBS
    * EFS: pay per GB used 
        * $0.30 per GB per month (varies by region) USED
    * EBS: pay per GB provisioned
        * $0.08 per GB per month provisioned

#### Scale
* scales automatically, pay per use, no capacity planning
* EFS Scale
    * 1000's of concurrent NFS clients
    * 10GB or more throughput
    * grow to petabyte sizre automatically
    * note throughput grows in size as more space utilized


#### Access
* EFS is region based and the same file system can attach to instances in different Zones
* attaches to one VPC with one mount target ENI per AZ
    * can have multiple AZ with an ENI in each AZ

* can access outside of it's VPC by VPC peering
* can access via on prem via direct connect or VPN

* important: when mounting from on prem MUST USE IPv4 NOT DNS
    * use ENI IP

#### Performance and storage classes

* performance mode
    * General Purpose (default)
        * latency sensitive use cases (i.e. web server)
    * Max I/O 
        * higher latency
        * but high througput
        * big data, media processing
    * throughput mode
        * Bursting Throughput is cost-efficient and works well for workloads with variable throughput needs.
        * Provisioned Throughput is ideal for applications that require predictable and consistently high throughput, regardless of storage size.
            * can set your throughput
            * costs more

#### Storage tiers 
    * standard  
        * Multiple AZ-(11 9s durability across multiple AZs)
        * Higher cost compared to other storage classes due to frequent access optimization.
        * Designed for frequently accessed data with high durability and low latency.
    * IA (infrequent access)
        * A lower-cost storage class for infrequently accessed data.
        * Suitable for data that requires high durability but is accessed less frequently.
        * good for Backup and disaster recovery or archiving
        * Multiple AZ-(11 9s durability across multiple AZs)
        * lower base cost but includes a per-GB retrieval fee when data is accessed.
    * One Zone/One Zone IA
        * same performance but less durability
        * 99.9% (3 9s), as it relies on a single AZ.
        * more affordable
        * Non-critical workloads with low durability requirements.
        * IA option allows reducing costs even further 
    * Amazon EFS offers lifecycle policies to automatically move data between storage classes, optimizing cost
        * i.e. if a file hasn't been accessed in >60 days will move to IA


#### Permissions
* can control access to the files via IAM

* Access Points
    * When multiple applications share the same EFS file system, access points can isolate them by defining separate root directories and POSIX identities.
    * application-specific entry points to an EFS file system
    * configure a specific user ID (UID) and group ID (GID) for applications accessing the file system through the access point.
    * Applications or clients mount the file system using the access point’s unique Access Point ID.
```
    sudo mount -t nfs4 -o nfsvers=4.1 \ fs-12345678.efs.region.amazonaws.com:/access-point-id /mnt
```
    * can also configure a default directory as the root directory 
    * can restrict access for clients using IAM policies
        * in IAM can configure what a client can access on an NFS file system
    * example:
        * can set a client uid/gid as 1001/1001 and only allow access to the /config directory
        * can set different client uid/gid to 1002/1002 and only allow access to /www directory

* File System Policies
    * these are IAM rules the you set ON THE FILE SYSTEM
        * restrict/allow access to other accounts, VPC's, specific IAM users, etc.
        * restrict/allow what these entities can do on the file system as well
    * apply access control rules to the entire EFS file system. 
    * by default it grants full access to all clients
    * They are similar to resource-based policies in AWS 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/EFSAccessRole"
      },
      "Action": [
        "elasticfilesystem:ClientMount",
        "elasticfilesystem:ClientWrite"
      ],
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-west-2"
        }
      }
    }
  ]
}
```

#### Cross Region Replication
* can replicat objects from one EFS file system to another regions EFS file system
* can replicate and setup new FS or replicate to existing FS
* Has RPO/RTO 
* doesn't use the EFS throughput, happens separately
* 
# storage

## data_exchange.md

#### S3 exchange
* find, subscribe, use 3rd party data in the cloud
* news data, health data, business data, location data

* will subscribe to a product then use AWS Data Exchange API to load it directly into S3
* can then analyze with machine learning and/or analytics services

#### Redshift exchange
* can also subscribe to third party data that can query in Amazon Redshift data warehouse in minutes
* if you have data you can license and share your data in Redshift via Data Exchange

### API exhcnage
* can find/subscribe to third party API's 
* consisent access using AWS SDK's
* conistent with aWS native auth and governance
# storage

## aws_transfer_family.md
* fully managed service for file transfers into/out of S3 or EFS using FTP protocol


* supports three kinds of protocols
    1. FTP 
        * (unencryption, other two are encrypted)
    2. FTPS (over SSL)
    3. SFTP (secure file transfer)

* pay per endpoint per hour 
* pay per data transferred

* can store and manage user credentials in the service
* can also integrate with existing auth providers 
    * AD
    * LDAP
    * Okta
    * Cognito
    * others/custom


* Exam will test on the following:

#### Public Endpoint on public net
* note the public endpoint IP's are dynamic and changes over time
* so use the DNS name 
* can't setup allow lists by IP addy in your firewall

#### VPC endpoint 
* only access the FTP endpoint via internal services to VPC
* can connect to VPC via VPN or Direct Connect 
* static private IPs (private) 
* can setup allow lists in firewall

#### VPC endpoint with internet facing access
* basically have the endpoint with a static private IP
* can use NAT or Network LB with a static EIP to provide access to an internet gateway
* can setup security groups to protect who can access 
# storage

## app_sync.md
* when see graphQL or access to real time data on exam, think app sync

* Managed service that uses graphQL
* Can integrate with all kinds of data sources
    * relational, http apis, dynamo, elastic search, many more
    * custom sources with lambda
* retrieve data in real time with Web Sockets or MQTT on websocket
    * know this real time aspect for the exam
* monitor with cloud watch


 * mobile apps


 * clients-> can be anything from mobile to web to offline sync to realtime dashboards
    * think REALTIME
 

* schemas
    * defines the structure of data and operations (queries, mutations, and subscriptions) for your AppSync API. It serves as the blueprint for how clients can interact with the API

 * resolvers
    * the connecting code to the data source 
    * connect the operations defined in the schemas to the dtaa source

* app sync can sync with cognito
    * can set roles and allowed actions like allowing a blogger to post but not a reader
# storage

## s3.md
* blob/object storage
* unlimited space
* pay as you go
* static content
* access using a key
* not file system, mountable
* not good:
    * to have lots of small files 
    * if need a file system
    * no search
    * not good for rapidly changing data
* 11 9's durability
* no indexing so CAN'T search for an object in S3 bucket
  * index objects in S3


#### Storage classes summary
* S3 Standard  
  - General-purpose storage for frequently accessed data  
  - High availability & durability  
  - Lowest latency, no retrieval fees  
  - Higher cost than other tiers  
  - Instant retrieval

* S3 Intelligent-Tiering  
  - Automatically moves data between frequent & infrequent tiers  
  - Great when access patterns are unpredictable  
  - Small monthly monitoring fee  
  - Saves money over Standard if access is irregular  

* S3 Standard-IA (Infrequent Access)  
  - Lower cost for data that’s accessed less often  
  - Same durability & latency as Standard  
  - Retrieval fees apply  
  - Minimum 30-day storage charge  
  - Retrieval fees are how it differs from Standard class

* S3 One Zone-IA  
  - Like Standard-IA but stored in a single AZ  
  - Cheaper, but less resilient  
  - Good for backup copies or re-creatable data  
  - Not suitable for mission-critical data  
  - Retrieval fees and lower durability are how it differes from standard

* S3 Glacier  
  - Archival storage for data rarely accessed  
  - Retrieval in minutes to hours  
  - Very low cost  
  - Good for long-term compliance/archive 
  - Retrieval times are how it differs from Standard (not instant retrieval, see retrieval tiers) 

* S3 Glacier Deep Archive  
  - Cheapest storage class for long-term archiving (7–10 years+)  
  - Retrieval time is 12+ hours  
  - Ideal for cold storage with compliance requirements  
  - Ultra-low cost, but slow to access  

* S3 Reduced Redundancy (deprecated)  
  - Was used for non-critical data with lower durability  
  - Avoid using — replaced by better classes like One Zone-IA  



### Glacier retrieval tiers
* Expedited  
  Retrieval Time: ~1–5 minutes  
  Cost: High  
  Use When: You need it immediately and can’t wait

* Standard  
  Retrieval Time: ~3–5 hours  
  Cost: Medium  
  Use When: You can wait a few hours; good default option

* Bulk  
  Retrieval Time: ~5–12 hours  
  Cost: Lowest  
  Use When: You're retrieving large amounts of data and have time to wait


#### Storage classes (also known as tiers)
* all classes have a base charge per volume of data stored
    * additional charges include retrieval, minium duration, minimum object, etc. 
    * base charge adjusts based on durability and frequency of access   
        * glacier base charge is extremely cheap but other charges add up when trying to retrieve
        * same with IA
        * one zone trades off AVAILABILITY for cheaper base charge  
            * note this is different from EFS one zone which trades off durability

* all have 11 9's durability
* all exist in >- 3 AZ's
    * except ONE ZONE classes which exists in one zone
* all have 99.9% availability 
    * except One Zone which has 99.5%

* Standard and Intelligent Tiering have no retrieval charge to get the item, all others have a retrieval charge

* Lifecycle Rules
    * transition objects between tiers automatically (or delete)
    * If you want to automatically move objects to Glacier after a certain time:


* Minimum Storage Duration Charge
    * AWS charges you as if the object is stored for a minimum of 180 days, even if you delete it earlier.

* Minimum Billable Object Size 
    * file smaller than this will still get charged for this size
    * If you store a file of 10 KB in Glacier Deep Archive, you will still be billed as if it were 40 KB.

* Cost to retrieve items
    * This fee is separate from the standard S3 request charges 
    * AWS prorates retrieval fees  based on the exact amount of data you retrieve,
        * i.e. if you retrieve 10MB will be charged based on a fraction of the 1GB price




* Standard:
    * S3 Standard: General-purpose storage for frequently accessed data.
    * Minimum Storage Duration Charge: None
    * Minimum Billable Object Size: None
    * Retrieval Fee: None

* Intelligent-Tiering:
  * Minimum Storage Duration Charge: None
  * Minimum Billable Object Size: None
  * Retrieval Fee: None

* Standard-IA(infrequent access):
  * Minimum Storage Duration Charge: 30 Days
  * Minimum Billable Object Size: 128 KB

* One Zone-IA(infrequent access):
  * Minimum Storage Duration Charge: 30 Days
  * Minimum Billable Object Size: 128 KB

* Glacier Instant Retrieval:
  * Minimum Storage Duration Charge: 90 Days
  * Minimum Billable Object Size: 128 KB

* Glacier Flexible Retrieval:
  * Minimum Storage Duration Charge: 90 Days
  * Minimum Billable Object Size: 40 KB

* Glacier Deep Archive:
  * Minimum Storage Duration Charge: 180 Dayskeep in mind 
  * Minimum Billable Object Size: 40 KB


#### Replication
* cross region replication (CRR)
* same region replication (SRR)
* designed to be used for backup and disaster

* can combine with lifecycle rules to transfer to different tiers

* Replication Time Control (RTC)
  * most objects replicated within seconds
  * 99.99% withing 15 minutes
  * get alarm if one is beyong 15 minute
  * helpful for compliance rules


#### S3 event notification
* s3 object: create/remove/restore/replicate...etc.
* for example: trigger an even when object uploaded and create a thumbnail from it
* these notifications typically delivered within seconds but can take up a minute or longer sometimes
* can trigger: SNS, SQS, Lambda, Amazon Event Bridge
* Event bridge
  * Once the events sent to Event Bridge can set up complex AWS logic to send to a bunch of AWS services
  * sends more meta-data about the s3 object to Event Bridge than other services
  * can set up multiple desinations for a single rule
  * have event functions: archive, replay
  * reliable delivery



#### Performance
* latency 100-200 ms
* application can achieve at least 3,500 POSTS/COPY/PUT/DELETE or 5,500 GET/HEAD per second per prefix in a bucket
* no limit to how many prefixes can have in a bucket
* the prefix is essentially the path of the file without the bucket nae or filename
  * /my-bucket/x/y/z/myfile.txt
  * the prefix would be /x/y/z/
* can create different prefixes for the file to scale more http requests
  * i.e. if spread reads across 4 prefixes can have up to 22,000 requests per second

* multi-part upload 
  * reccomended for files >100MB
  * required for files >100GB
  * parallelize the file upload for speed
  * note: if you stop the multi-part upload early and leave file upload incomplete there will be straggler data in S3 
    * set up a lifecycle policy to abort and delete the multipart upload stragglers after X number of days

* S3 transfer accelleration
  * client can transfer file to edge location which will then internally transfer file to s3 bucket
  * compatible with multi part upload so can combine to bump speed

* S3 byte range fetches
  * parlellize GETS by requesting specific byte ranges
  * basically chunks up the file and pulls all the chunks at once in parallel
  * better resilience in case of failures
  * can be used to speed up downloads
  * can also allow to retrieve parts of files i.e. submit a byte range, can save bandwidth costs

#### S3 select and Glacier select
* can use simple SQL statements to query CSV, JSON, and Parquet files
* store file in s3
* use S3 select API to query the file with a SQL statement
* this saves transfer bandwidth as it only transfers data you need


#### Storage Class Analysis
* feature of s3 that helps optimize storage costs by analyzing objects and determining the best storage class
* creates a CSV report
* report updated daily
* takes a day or two for it to start working after enabled
* can also visualize in Amazon Quick Sight
* helps to build lifecycle rules


#### Storage Lens
* Amazon S3 Storage Lens is an analytics tool that provides comprehensive insights into the storage usage and activity across all your Amazon S3 buckets.
* Provides over 60 metrics to analyze storage usage and activity.
* Aggregates data across multiple accounts, buckets, and regions into a single view.
* Offers a default user-friendly console dashboard, but can also customize your own
* Automatically generates actionable recommendations for optimizing costs and performance.
* Export metrics to Amazon S3 for further analysis with tools like Amazon QuickSight or third-party solutions.(JSON or Parquet)
* two tiers:
  * Free Metrics: Basic metrics are included at no additional cost.
    * storage only 14 days
    * 28 different metrics
  * Advanced Metrics and Recommendations: Paid tier with additional insights, activity metrics, and advanced recommendations.
    * storage is 15 months
    * collects metrics at the prefix level
    * can access metrics in cloudwatch free
    * add more metrics
* metrics
  * bytes and object count -> helps identify fastest growing or not used buckets and prefixes
  * cost optimization metrics
    * NonCurrentVersionStorageBytes - old versions unuusued
    * IncompleteMultipartUploadStorageBytes -  incomplete uploads not needed
    * can write life cycle 
  * data protection metrics
    * versioning enabled?
    * MFA required for delete?
    * crossregion replication rule count
    * identify buckets not following data protection best practices
  * access managment metrics - ownership related info
  * event metrics - events fired, enabled
  * performance metrics - s3 transfer acceleration
  * activity metrics - all requests/byt downloaded
  * status code metrics - 200's, forbiddens, notFound's

#### Static website hosting
* S3 can be enabled as a static website with enable static hosting config


#### Signed URL
* can create a temprary time limited url for access to files
* the url is created with permissions as the person who created the presigned url
# storage

## EBS.md
* network attached 
* elastic block store
* resizable
* attached to an ZONE (not VPC or region)
    * You cannot attach an EBS volume directly to an EC2 instance in a different AZ. To move an EBS volume across AZs, you need to create a snapshot of the volume and then restore it in the desired AZ.

* can pick an instance that is EBS optimized for maximum throughput if need to heavily use EBS


* EBS volume types
    * gp2/gp3
        * SSD
        * g = general purpose, balance price/performance
    * io1/io2
        * SSD
        * e = extreme performance, low latency, high through put
    * st1   
        * low cost HDD for normal use
    * sc1
        * low cost HDD for cold storage for less frequent access

* Only GP and IO series can be used as boot operation

* EBS vols are charachterize by: 
    * Size
    * Throughput
    * IOPS
    


#### Snapshots
    * incremental- will only backup changes from past snapshot
    * EBS backups will share the same IO as the actual workload/connection to the instance, so may get slowness during backup
    * store in S3, but you won't see t
    * Not necessary to detach volume to do back BUT RECCOMENDED
        * if volume is being used during back up you may get inconsistent state
    * Can copy a snapshot across region

* Snapshot -> AMI
    * can make an AMI out of your snapshot
    * can build an service and then make an AMI out of it 

* * How snapshots work at a data level
    * When restoring from a snapshot, an EBS volume goes through two phases:

    * Provisioning:
        * The volume is created and immediately available for attachment to an EC2 instance.

    * Lazy Loading:
        * As blocks are needed they are fetched from s3 and stored permanantly in EBS


* Warmup: EBS volumes restored from a snapshot will need to be pre-warmed
    * They will need to have all of their blocks loaded from s3 otherwise the default will be to lazy load a block at a time
    * 2 ways:
        * Fast Snapshot Restore: will read all blocks from s3
        * fio/dd commands 


#### Data life cycle manager  DLCM (Automation)
* can automate retention, creation
* can schedule backups/ cross-account, etc.
* use resource tags to identify the resources
    * i.e. prod, dev, test, etc
* NOTE: EVERYTHING HAS TO BE WITHIN DLCM
    * Can't work with one offs or anythign created outside OF DLCM
* Can't be used to manaage instance store backed AMI because it's not on the EBS infrastructure and is on the host machine rack
* DLCM va AWS backup
    * DLCM: creation, retention, deletion of EBS snapshots
    * AWS backup: 
        * a generic backup service for all service in AWS
        *  superset of DLCM, has DLCM plus every other service,

#### Encryption
    * 'Always encrypt new volumes'
        * per region setting to encrypt all of your volumnes in the region
    * by default EBS volumes are NOT encryptied

#### EBS multi-attach
    * for io volumes only
    * can attach same EBS volume to multiple instance in same AZ
    * full read/write for all attached instances to the vol
    * file system not normal XFS or EXT, it's a cluster aware file system


#### Local EC2 instance store

# caching

## cloudfront.md
* content cached at edge
* 200+ locations around globe
* protect against Network and Application layer attacks i.e. DDoS
* Integrate with:
    * AWS Shield
    * AWS WAF
    * Route 53
* can communicate with HTTPS and can expose HTTPS apis
* can use websocket protocol


* Cloudfront - origins
    * where the original data comes from
    * can actually used Cloudfront to load files into S3

    * origins:
        * s3
        * s3 configured as a website
        * AWS media services: media store container and media package endpoint
        * Any custom origin using http, ex: EC2, LB, API GW,any http backend you want (i.e. on prem)
            * must be public so public edge locations can access
            * can specify security group of IP's of only edge locations that can access
            * if want private Ec2, use an LB public

#### Cache location
1. CloudFront Edge Locations:
    * These are the primary locations where CloudFront caches and serves content closest to end-users.
    * If a user requests content that isn’t available in an edge location's cache, CloudFront forwards the request to a Regional Edge Cache.
    * hundreds of these globally

2. Regional Edge Caches:
    * These are larger, centralized caching layers that aggregate requests from multiple edge locations in a geographic region.
    * If the content is cached at the Regional Edge Cache, it is served from there.
    * If the content is not in the Regional Edge Cache, it forwards the request to the origin server.
    * A Regional Edge Cache aggregates requests from CloudFront Edge Locations within a single region. For example, all edge locations in North America will use the North America Regional Edge Cache.
    * If content is cached in the North America Regional Edge Cache, it will only be accessible to edge locations within North America.
    * If the same content is requested from another region (e.g., Europe), and it’s not available in the Europe Regional Edge Cache, the request will go to the origin server unless other caching layers contain it.

3. Origin Server:
    * The origin is the source of the content (e.g., S3, EC2, or on-premises server).
    * The origin delivers the content to the Regional Edge Cache, which then passes it back to the edge location and eventually to the user.



#### Alternatives
* s3 cross region replication - designed for backup not speed(can still work but is worse than Cloudfront)
* api gw edge uses cloudfront but creates and manages it for you
        


#### Access Control
* custom header
    * configure CF to send a custom request header
    * configure ALB to only send requests to instances that contain that header
    * header name + value must be kept secret!
* security groups
    * at a network level can restrict access to origin by using security groups
    * only allow cloudfront IP's to access
* Origin Access Control 
    * OAC allows you to restrict access to your backend origin (e.g., an Amazon S3 bucket or a custom HTTP server) so that it can’t be accessed directly from the internet. 
    * includes a header with an IAM signing of the request that the origin then verifys


#### Origin groups
* have a primary and secondary origin
* if primary returns error code will request from secondary
* note primary and secondary can be different regions

* if do this with s3 buckets, can combine with CRR to replicate cross region

#### Geo restriction
* allow list or block list for countries
* georestriction for copyrighted content
* the "country" is determined using a 3rd party IP data base
* adds a header called
    * CloudFront-Viewer-Country
    * that is what is accessible to origin
    * can add this yourself as well


#### Pricing
* edge locations all around the worl
* cost of data leaving location varies
* less expensive: USA-> most India
* see chart in this folder

#### Price classes
* reduce the number of regions to save money
* see chart in this folder
1. All regions
    * best performance
    * highest cost
2. Class 200
    * most regions but exclude most expensive
3. Class 1000
    * only least expensive regions


#### Cloudfront Signed URLS
* Signed URL
    * client will either visit an API to get a special URL with a time sensitive signature attached or use the aws cli 
    * allows access to non-publicly accessible content that is signed url enabled 
* can restrict by IP, path, date, expiration
* can upload a public/private key pair to cloufront console to generate a signed url
    * differs from s3 which uses the person who signed the url

#### Custom Error PAges
* Return objecgt to viewer when origin returns 4xxx or 5xx status code to CF
* instead of sending the origins error message will send custo error
* can store these custom pages is s3 (not sure if other places as well)
# caching

## edge_functions.md
* execute logic as close to user as possible
* code executed

* use cases: 
    * change the request/response, 
    * validate auth signatures like JWT
    * request filtering
    * A/B testing
    * bot mitigation at edge
    * 


#### Cloudfront edge
* javascript
* can't access external services
* operates at the EDGE baby
* super performant: sub-ms startup times, millions of req/ps
* managed entirely within CloudFront


##### Lambda Edge
* lambda/python
* can access anything
* not as performant: 1000's of rps
* operates at the 'regional edge'  so not as close as the edge
* When you create a Lambda@Edge function and associate it with an Amazon CloudFront distribution, it is automatically replicated to all Regional Edge Caches globally.

#### Types of request response
* viewer req/resp
    * the back and forth between edge function and user
* origin req/resp   
    * the back and forth between origin and edge function

* lambda can handle both origin req/resp and view req/resp
    * client -> viewer req ->  lambda edge function -> origin req -> origin
    * origin -> origin resp -> lambda edge function -> view resp -> client

* Note: cloudfront functions can only handle viewer req/resp
    * client -> viewer req ->  CF edge function  -> origin
    * origin -> CF edge function -> view resp -> client


* can combine cloudfront functions and lambda 
    * cloudfront functions handle viewer req/resp
    * lambda edge funct handles origin req/resp


#### use lambda edge
* when need longer execution time
* when you need network access
* 3rd party api calls
* access other services
* better resources
* larger package size
* 5 seconds of runtime for user req/resp and 30 sec of runtime for origin req/resp
* Note: worse QPS performance
* can use 3rd party libraries (i.e. Aws sdk to access other aws services)
* some use cases
    * if need other aws service
    * if need to access other apis
    * if need file system access
    * if need access to body of http requests
    * if need longer processing times

    * load content based on User Agent
        * i.e. browser get's higher/larger resolution image vs mobile device 

    * use lambda at edge to access dynamo and can access this via client request
        * can also integrate auth into the process inside the lambda 
        * this creates a basic serverless API like API Gateway + lambda but with way less features than API Gateway
        * global/serverless way to do api in AWS

    * modify origin
        * setup
            * have a cloudfront @ edge location in one region
            * have s3 bucket in another origin
            * initial get from origin could take a while as it's cross origin
        * solution:
            * set up cross region replication in s3 to same region as cloudfront 
            * setup a lambda@edge function to modify origin and send the request to the same region origin s3 
        * Note:
            * CloudFront Functions cannot change the origin domain name, origin region, or other origin-related parameters.
            * Interact with the Origin Request Lifecycle: CloudFront Functions don’t have access to the origin request/response lifecycle, so they can’t alter requests after they’ve been routed to the origin.

#### use CF func
* when need max performance
* only have 1ms execution time
* no access to body of request!!

* some use cases:
    * cache key normalization: can alter the headers,query strings,url to create an optimzed cache
    * header modification: insert, modify, delete headers in req/resp
    * URL rewrites/redirects
    * validate JWT's at edge to allow/deny requests to the origin
        * note: there's no integration with other service so have to manage key rotation another way
        * using a lambda would allow integration with other auth services 

# caching

## elasticache.md
* elasticache: Redis or Memcache
* Cache in memory database 
    * help reduce load on database for read
    * can do hot cache or pre calculated data
* helps make application stateless
* fully managed

* using elasticache requires heavy application code changes


* Application queries elasticache
* cache hit: gets data
* cache miss: will query RDS and then store the data in elasticache

* cache invalidation strategy
    * prevent consistency problem between invalid old data and database

* user session store
    * if have a 3 tier architecture with stateless server tier of numerous servers
    * if no sticky LB could use any of the servers
    * each server uses elasticache to write the session data to
    * if a user hits another instance, it can recover the session info



#### redis vs memcached
* redis
    * multi AZ with failover
    * read replicas to scale reads and have high availability
    * persistent
    * data durability
    * backup/restore features
* memcached
    * multi-node but for sharding not backing up(if lose a shard will lose data)
    * not persistent (lose cache lose data)
    * backup/restore only for serverless not self managed

# machine_learning

## all.md
#### all the servcies 
* Rekognition: face detection, labeling, celebrity recognition
* Transcribe: audio to text (ex: subtitles)
* Polly: text to audio
* Translate: translate langauges
* Lex: build conversational bots – chatbots
* Connect: use Lex to build a cloud contact center 
* Comprehend: natural language processing(sentiment analysis, important sections, etc)
* SageMaker: machine learning for every developer and data scientist
* Kendra: ML-powered search engine for document collection
* Personalize: real-time personalized recommendations
* Textract: extract text and data in documents/images



#### Rekognition
* USE CASE 
    * identify and moderate

* USE CASE EXAMPLES:
    * labeling
    * content moderation
    * text detection!
    * face detection and analysis(gender, age, range, emotions)
    * face search/verification
    * celebrity recognition
    * pathing (sport game analysis of a video) 

* content moderation 
    * inappropriate, offensive, unwanted content
    * used in many applications to create a safer user experience
    * make sure images displayed don't show anything offensive

* set minimum confidence threshold for things to be flagged 
    * either for identificatioan or for moderation

* can do a human manual review in A2I
    * amazon augmented A2
    * select optional manual review


#### Sagemaker
* fully managed service to develop machine learning models 
* intended for developers and data scientists
* collect a lot of data and feed into sagemaker
* label that data, train/tune that data
* can save that model and use it with future data



#### Personalize
* on exam: when see ML service for personalized reccomendations
* fully managed ML service to build apps with real time personalized reccomendations
* customized direct marketing
* same technology used by Amazon.com ( the reccomendation services )
* s3(non realtime) or personalize API(real time) -> personalize
* outputs can be websites, email, mobile, SMS, etc.



### All of these are text/document/speech based

#### Textract
* extracts text from scanned documents(many formats pdfs, images, etc) or handwriting
* can get it as a data file i.e. JSON or something
* can even have forms tables 
* finanical sector, health care, public sector,etc


#### Transcribe
* automatically convert speech to text
* pass in audio and get text back

* automatically remove an PII (personal identifying information) using redaction
    * name, ssn, etc

* supports automatic language identification for multi-lingual audio

 * search, transcribe, automate subtitles, translate into multiple languages
 
* does not user NLP is purely a speech to text with no understanding

#### Polly
* turn text into speech using deep learning
* create applications that will talk
* Lexicon
    * a metadata file you define and upload to the screen with the text
    * customize pronunciation of works with customized lexicon
    * example: can customize it to pronounce 3's as E and 4's as h: St3ep4ne
    * example: can make it say Amazone Web Services any time is sees: AWS
    * upload your defined lexicon and use in synthesize speech operation
    
* SSML
    * literally XML tags added to the written text to indicate functions the speaker should do
        * <break time= "1 second">
    * speech synthesis markup language
    * enables more customization in how speech is made and pronounced
    * emphasize specific words or phrases
    * include breathing sounds/whispering/news caster style/phonetic pronuncaiation/emphazise specific words/phrases/etc.



#### Translate
* simply a service to translate from one language to another at scale


#### Lex
* convert speech to text
* understands language, (natural language understanding) to recognize the intent of speech/text
* helps build chat bots/call center bots


### Amazon connect
* recieve calls, create contact flows, cloud based virtual contact center
* can integrate with other CRM's or other services in AWS
* way cheaper than traditional call center operations
* FLOW:
    * phone call to an Amazon Connect provided number
    * customer calls amazon connect
    * Lex streams all the info from this call and understands the intent of the call
    * Will invoke the right lambda function based on what it hears
    * i.e. an appointment scheduler lambda function that will go into a CRM and schedule a meeting

### Amazon Comprehend
* natural language processing (NLP)
* anytime see NLP on examp think comprehend
* fully managed and serverless service
* uses machine learning to find insights/relationships in text
* USE CASES:
    * langauges, key phrases, places, people, brands or events
    * sentiment analysis to understand how positibe of negative the text is
    * analyze text using tokenization and parts of speech
    * organize a collection of text files by topic 
* EXAMPLES:
    * anaylize customer interactions, emails, etc to find what leads to positive/negative customer experience
    * create and group topics that comprehend will discover


### Amazon Comprehend Medical
* can extract patient info, clinical info, etc
* can detect PHI (protected health information) (using NLP)
    * detectPHI API
* from copy/past text,  S3, kinesis, transcribe, etc  -> Comprehend Medical
* get insights



### KEndra
* when see document serach service on Exam think Kendra
* fully managed document search service powered by machine learning
* many many formats (i.e. pdf, txt, html, powerpoint, etc.)
* can connect and use many data sourced (google drive, box, s3, RDS, etc)
* will index the document
* builds an knowedge index powered by machine learning ]
* User can ask a question: where is the tech department, and Kendra can check it's knowledge base and reply
* 
# other

## other.md
#### Alexa for business
* book meeting room, increase meeting room efficiency


#### Workspaces
* Secure cloud desktop
* helps eliminate on prem VDI (virtual desktop infrastr..)
* pricing on demand or monthly
* integrated with microsoft AD
* Workspace updates managers -> keeps applications updated
* Windows update -> keeps windows updated
    * by default updates turned on
* can define update maintenance windows 
    * default is 12 AM to 4AM
    * workspaces will reboot automatically for you

* Multi region failover
    * must use an AD connector and not a multi region AD

* IP access control groups
    * similar to security groups for Amazon workspaces
    * list of IP's/CIDR ranges that users are authorized to connect from
    * must whitelist any VPN or NAT

#### Appstream
* simply streams an app in a web browser
* no machine required
* like geforce now but for apps

#### Device farm
* if want to test an mobile/web application across multiple devices
* runs across real browsers and mobile devices
* fully automated using a framework
* Will generate videos and logs to document the issues encountered
* can also remotely log into the devices to debug


#### Macie
* fully managed data security and privacy service
* uses machine learning to discover and protect your sensitive data
* alerts if it discovers PII (personally idenitifable information)
* put the data in S3 for Macie which then notify via event bridge
* can integrate event bridge with SNS topic, lambda function

#### SES (simple email service)
* Fully managed service to send emails at scale
* allows for outbound and inbound emails
* app communicates with it via API, AWS console, SMTP
* reputation dashboard, performance insigts, anti-spam feedback
* stats on deliveries, bounces, feedback loop results, email opens
* supports DKIM(domain keys identified mail) and SPF(sender policy framework)
* flexible IP deployment: shared, dedicated, customer owned IP's
* transactional, marketing, bulk email communications 
* Configuration sets in Amazon SES are used to group and manage email sending settings.
    * Main purposes:
        * Track email sending metrics (opens, clicks, bounces, complaints)
        * Control where metrics are sent (CloudWatch, Kinesis Data Firehose, SNS)
        * Apply sending policies (IP pool selection, event publishing)
    * Key features:
        * Event destinations:
            * CloudWatch – monitoring and alarms
            * SNS – immediate , real-time notifications
            * Kinesis Data Firehose – data storage and analytics
        * IP pool assignment:
            * Assign specific IP pools to manage deliverability and reputation

    * An event is a recorded action or outcome of an email message.
    * Common types of SES events:
        * Send: the email was successfully accepted by SES for sending
        * Delivery: the email was successfully delivered to the recipient's mail server
        * Bounce: the email could not be delivered (hard or soft bounce)
        * Complaint: the recipient marked the email as spam
        * Open: the recipient opened the email (tracked with a pixel)
        * Click: the recipient clicked a link in the email
        * Reject: SES rejected the email before attempting delivery (e.g. policy violation)
        * Rendering Failure: the email couldn’t be rendered for open/click tracking
    * Events are useful for:
        * Monitoring email performance
        * Debugging delivery issues
        * Triggering alerts or workflows using services like SNS or Lambda
        * Analyzing user engagement through clicks and opens
 
    * Sending authorization and suppression lists:
        * Control sending behaviors with rules or suppression lists
    * How it works:
    * Create a configuration set
        * Define event destinations and optional IP pool
        * Specify the configuration set name when sending emails
        * SES applies the rules and tracks metrics accordingly
    * EXAMPLE:
        * Open events (along with clicks, bounces, deliveries, etc.) can be sent to Kinesis via event destinations.
        * To do this:
            * Create a configuration set in Amazon SES
            * Define an event destination within the config set
            * Choose "Kinesis Data Firehose" as the destination type
            * Select which event types to publish (e.g., open, click)
        * Benefits of sending events like opens to Kinesis:
            * Real-time stream processing
            * Store events in S3, Redshift, or Elasticsearch
            * Build dashboards, analytics pipelines, or alerting systems


### Pinpoint
* main functions:
    * marketing campaigns: has message templates, delivery schedules, highly-targeted segments, and full campaigns
    * deliver: integrates with SNS, SMS
    * track: can recieve events into various locations for tracking analysis 
* scalable 2 way inbound/outbound marketing communications service
* supports email, SMS, push, voice, and in-app messaging
* ability to segment and personalize messages with the right content to customers
* can recieve replys
* can scale to billions of messages per day
* run campaigns by sending bulk marketing email
* bulk transactional SMS messages
* all the events such as text or email success, deliver will be delivered to SNS, Firehose, Cloudwatch logs
    * easily build automation 


### EC2 image builder
* used to automate the creation of virtual machines(EC2 AMI's) or container images
* create, maintain, validate, test 
* can run at set custom schedules (i.e. weekly, on push, etc.)
* free service, only pay for underliying resources
* can publish the AMI toi multiple regions and accounts


EC2 Image builder will:
spin up a blank EC2 instance
will run the build components software
will create AMI From this
will test by:
     spinning up a new EC2 instance from the AMI 
     run all the test suite (AMI working, secure, etc)
AMI will be distributed to multiple regions and/or accounts




CICD Architecture
* code pipeline defines all of the following
1. code commit
2. code build
3. cloudformation to automate and launch EC2 image builder service 
4. EC2 image builder service will then take last code delpoyed and create an AMI out of it
5. Pipeline will then use cloudformation to rollout the AMI in production to a large group of instance behind an ASG and can do canary style one at a time



#### IoT core
* easily connect IoT devices to the cloud 
* serverless, secure, scalable to billions of devices and trillions of messages
* integrates with alot of AWS services (lambda, sagemaker, s3, etc)
* gather, process, analyze, and act on data 
* IoT topic
    * take data in, in various formats
    * setup one or more IoT rules
    * rules have one or more actions
    * actions related to AWS services(many options, S3, SNS, kinesis, dynamo, lambda, sQS, etc.)
    * so can send the IoT data to one of many rules which has one of many actions which connects to an AWS service
    * important integration:
        * kinesis firehose
            * can do transformations in the firehose
            * persist in S3, redshift, OpenSearch
# EC2

## autoscaling.md
* dynamic scaling policies
    1. target tracking scaling
        * simplest
        * take metrics 
        * if above the increase metric will add instances 
        * if beneath the reduced metric remove instances

        * simple/step scaling
            * example: when cloudwatch alarm triggered add 2 units

        * scheduled scaling
            * anticipate based on known usage patterns

        * predictive scaling
            * AWS will analyze your historical load and generate a forecast based on that
            * AWS will then setup scaling and adctions to predict the right anoubt of resources to sustain that load
            * good if you have patterns in load
        
* Good metrics to scale on
    * CPUUtilization: average CPU
    * RequestCountPerTarget: to ensure the network requests spread out to all the ASG instances are stable and no instance overloaded 
    * Average network In/Out: 
        * if applcation is network bound
        * ex: a video uploader
        
* Other autoscaling info
    * spot fleets (mix of spot and on demand instances)
    * lifecycle hooks:
        * allows perform actions at stages of instance lifecycle
            * ex: before instance terminated or when it starts
        * ex: clean up logs, log extraction, special health checks
    * to upgrade an AMI
        1. must update the launch/configuration template of the ASG
        2. 
            * must terminate instances manually(cloudformation can help)  OR
            * use EC2 instance refresh for auto-scaling to terminate instance for you 
                * the new ones come up and have the new AMI setting in the ASG template
    * autoscaling: instance refresh
        * if you update ASG launch template
        * specifiy minimum perctange healthy of instances
        * the ASG will automatically ternminate percentage and bring up new ones with the new launch template settings
        * continue this until all instances replaced by new ones 
        * can specify warm up time until instance is considered ready to use (to ensure bring up services)

* all the processes in the autoscaling group
    * Launch: add new EC2 to the group, increasing capacity
    * Terminate: removes EC2 instance ,decreasing capacity
    * HealthCheck: checks health of instance
    * ReplaceUnhealthy: terminate/recreate unhealthy instances
    * AZRebalance: balance number of instances across AZ's
    * AlarmNotification: accepts notifications from Cloudwatch
    * ScheduledAction: perform scheduled actions you create
    * AddToLoadBalancer: add instances to LB or target group
    * InstanceRefresh: performs a phased kill and recreate all instances in the ASG

* Health checks
    * ec2 status checks
    * ELB health check (http based): the ELB will consistently check the instance
    * if instance is deemed unhealthy based on the status checks
        * AWS will terminate and the launch new one to replace
    * make sure the health check is simple and correctly checks the HEALTH of the instance
    * a good check is an http endpoint called /health-check or something like that
    * a bad check is checking a route that does something heavy i.e. reach out to database for example
        * this could take a long time or the database could fail
        * would give a false alert that EC2 has failed 


#### Auto Scaling Update Strategies
* how to update an application in an autoscaling group
* there's different architectures possible

* background info
    * A target group is what a LB distributes traffic to
    * An target group is associated with an ASG so that each instance an ASG creates is registered to a target group
    * A launch template is used by ASG's to specify the new instance details
    * A single ASG is only allowed to use a single target group(associated with the ASG not the launch template)
    * A single ASG can use multiple launch templates

* architecture:  LB -> ASG -> Launch Template -> Target Group

* different architectures possible to do this: 

1. single ASG, multiple launch templates
    * will spin up different versions in the same target group
    * both versions will be live and recieving traffic at the same time
    * old versioned instances gradually shut down as new versioned instances spin up
    * LB does not know about instance details only target groups, so can't differentiate to send different percentages of traffic
    * this is called a rolling deployment

2. two ASG each with a different launch template and target group
    * LB can differentiate between target groups and can adjust traffic
    * each ASG can have a different version in the launch template
    * allows for a Canary deployment(gradual increasing  % of traffic between versions), or Blue/Green(switch versions all at once but retain old one as backup)


3. Multiple ALBs each with their own ASG's and target groups
    * basically entire environment replicated including the load balancer
    * the client would need to have traffic switching done at the DNS level
        * use CNAME and and can have 'weighted record' to allow weighted traffic rollout
        * note: relys on clients to have sane DNS settings to split traffic
        * pros: can test the full architecture with the new version 

# EC2

## AMI.md

# EC2

## basic.md
* types: R(RAM),C(CPU),M(Medium/balance),I(I/O),G(GPU), T2,T3(burstable), T2/T3 unlimited(unlimited burst)


* placement groups
    * by default when launch an instance it's placed randomly 
    * strategies
        * spread: 
            * each instance is on different hardware on different racks with separate power/network
            * can span across different AZ's
            * reduce risk of failure
            * limited to 7 instances per AZ per placement group
            * intended for workloads with critical uptimes: Database nodes, caching layers, or critical services with strict uptime requirements.
        * Partition: spreads across many partitions which are separate racks
            * all the instances are grouped into partitions
            * 7 partitions per AZ
            * EC2 metadata service can give the instance access to which partition they belong to
            * if the instance count is equal to or less than the number of partitions, each partition will host one instance, then it will try to even balance when instances exceed partitions
            * each partition is a groups of racks with dedicated power/networking that aren't shared with other partiitons
            * intended for large-scale distributed systems(hadoop, cassandra, Kafka, etc)
            * sort of a less robust spread strategy
        * cluster
            * all instances on same rack in same AZ 
            * this gives low latency, high bandwidth (10G between instances) 
            * if the rack fails ALL instances fail
            * choose instance type with enhanced networking for the speed
            * types of uses: big data job that needs to complete fast or application that needs low latency
    * can change an instances placement group, (very important to know)
        * have to stop instance
        * use CLI (modify-instance-placemenbt)
        * start instance

* ways to launch instances
    * on demand: short workload, predicatable pricing, reliable
    * spot: 
        * short workloads, cheap, can lose instances (not reliable), 
        * good if app is reslient to failure
        * no discount
    * reserved: 
        * purchase then for minimum of 1 year
        * high discount
        * long workloads
    * convertible reserved
        * long workloads 
        * will allow to convert instance type
        * middle discount
    * dedicate instances
        * no other customer will share your hardware
    * dedicated host
        * books entire physical server
        * great for software licences that operate on a per core basis that might not work on a virtualized instance
        * host affinity so that instance reboots are kept on the same host


* EC2 Graviton processor
    * delivers the best price performance
    * many OS support it NOT WINDOWS
    * Gravitron 2: 40% price improvment over 5th gen x86 instances
    * Graviton 3: 3x better performance 


* Metrics
    * CPU utilization + Credit Usage/Balance
    * Network: Network in.out
    * Status check
        * instance status: status of the VM
        * system status: status of the underlying hardware host
    * Disk
        * read/write for ops/bytes 
    * RAM NOT INCLUDED IN METRICS
        * Have to push from instance to cloudwatch as a custom metric

* EC2 Instance recovery
    * recover instance if the two status checks fail
    * EC2 monitored by Cloudwatch alarm with StatusCheckFailed_System alarm
    * there is an action called "EC2 instance recovery" to recover that is triggered by the cloudwatch alarm
    * this recovery will keep: IP's(private, public, elastic), metadata, placement group
    * cloudwatch can alert an SNS topic to let you know failure/recovery/whatever



#### High performance computing(HPC)
* HPC
    * cloud greatly enables this
    * can build a big multi instance infrastructure and destroy when done
    * limits cost to what we used
    * can expand to as much as have money for and quickly

* AWS direct connect 
    * Direct connect hardline to on prem 
    * allows to move a lot of data into AWS
    * very secure

* Snowball
    * Move Petabytes of data to cloud

* Datasync
    * move large amount of data between on prem and S3, EFS, FSx for Windows

* HPC compute(CPU)
    * computer/network optimized
    * spot instances/spot fleet for cost savings and also autoscaling
    * if instances need to talk to each other, put them in a cluster placement group for speedy connection

* HPC neworking
    * the instance type determines the network speed!
    * attach an ENI to connect the instance to the VPC network(not this is simply an interface and has nothing to do with speed)
    * Instances with ENA or Intel 82599 VF (Virtual Function) support enhanced networking, enabling high-speed, low-latency connections.
    * Elastic network adaptor(ENA) up to 400Gigs
    * ENA used specifically for High Performance Networking
    * alternative to using ENA is using an Intel networking hardware but only up to 10 gigs-LEGACY
    * Elastic Fabric Adaptor
        * Improved enhanced networking fast!
        * great for inter-node comms/tightly coupled workloads
        * uses message passing interface standard(MPI)
        * bypasses the underlying Linux OS to provide low-latency reliable transport
    * EC2 enhanced networking (SR-IOV), higher bandwidth/lower latency


* Be able to differentiate between ENA or EFA or ENI


* HPC storage
    * how to store HPC data
    * attached directly to instance
        * EBS(256,000 iops with io2 block eexpress)
        * instance store: scale to millions of IOPS, linked to EC2 instance on hardware, low latency
    * network storage
        * S3 
        * basic EFS: scales iops based on total size of file system
            * can also use provisioned iops 
        * Amaaon FSx for Lustre
            * HPC optimized distributed file system
            * million of IOPS
            * in backend it's backed by S3

* HPC automation and orchestration
    * AWS Batch
        * supports multi-node parrallel jobs 
        * this enables run single jobs that span multiple instances
        * easily shcedule jovs and launch instance accordingly
    * AWS Parallel Cluster
        * open source cluster management tool to deploy HPC on AWS
        * Configure with text files
        * automate creation of VPC, Subnet, cluster type, and instance types


#### Spot Instance
* get discount up to 90% compared to demand
* define your max spot price(mxp) and while current spot price(csp) < your max spot price(msp) you will get the instance
* hourly CSP varies by capacity and offer
* if CSP is greater than your MSP then you have a 2 minute grace period to stop/terminate your instances
* great for batch jobs, data analysis, failure resistant workloads
* do not use for critical apps or databases because you can lose them quickly

#### Spot Fleets
* allow us to automatically request spot instances with the lowest price
* set of spot instances + optional on demand instances
* will try to meet target capacity with price constraints
* launch from launch pools
* define multiple launch pools and then AWS fleet will choose which one at the moment is best filled
* spot fleet keeps spinning up instances until reaches capacity or max cost
* spot fleet strategies:
    * lowestPrice: launch instances from the pool with lowest price
    * diversified: spot instances distributed amongst all the pools
    * capacityOptimized: pool with optimal capacity for the number of instances
    * priceCapacityOptimized: pools with highest capacity available then select pool with lowest price
        * this is best choice for most workloads

    

#### Storage
* Instance store volume backed instance: 
    * very FAST
    * block storage
    * cannot increase in size
    * Root volume resides on ephemeral storage that provides high performance but no persistence. Best for temporary or stateless workloads.
    * Stopping instance is NOT allowed
    * REboot WILL KEEP THE DATA
    * The instance store data is lost if you terminate the instance!!!
    * Stopping the instance NOT ALLOWED
        * Stopping would require saving the instance's state (similar to an EBS snapshot), which instance store-backed instances are not designed to do.
    * physically attached local disks on the host machine where the instance is running.


* EBS-Backed volume instance: 
    * Root volume resides on persistent, durable, and scalable EBS storage, making it the default choice for most use cases.
    * Most modern AMIs are EBS-backed. Without EBS, they cannot boot because they rely on an EBS volume for their root filesystem.


* can have OS/apps on an instance backed and then also have an EBS volume for persistent data


# web_layer

## api_gateway.md
#### API gateway
* resides in a region but in aws cloud

* limits
    * timeout on any request on API gateway is 29 seconds
        * this means once API GW recieves a request and forwards it to the 'integration' handling the request it will only wait 29 seconds for a response
        * this applies to websockets only in the sense that it waits for the response from the integration for 29 seconds to establish the web socket connection
        * will shut a web socket connection after 10 minutes of inactivity 
    * 10MB max payload size in one request

* deployment stages
    * API changes are save as 'deployment stages'
    * name the stages anything 'dev, test, lemur'
    * stages can be rolled back as history is kept of all changes

* 3 ways to deploy API GW
    * edge optimized 
        * sends requests through Cloudfront Edge in order to reduce latency
        * note: API GW still sits in a single region
        * When you configure an API Gateway as edge-optimized, AWS creates a global CloudFront distribution for your API.
        * This distribution uses CloudFront's network of edge locations around the world.
        * The edge location routes the request over Amazon's private, high-speed global backbone network to the region where the API Gateway is deployed.

    * Regional
        * normal mode, API GW is in a single region 
        * can spin up a Cloudfront distribution seperately to integrat with this
    * private
        * only access within VPC
        * uses a VPC interface endpoint
            * each VPC interface endpoint can access multiple APIs
        * control access with endpoint policy or gateway resource policy
            * can allow cross account access

* caching API responsed
    * reduce number of calls made to backend
    * checks cache first before
    * data in cache has TTL
        * 300ms is default
        * can set TTL from 0(no cacheing) to 3600 seconds(1 hour)
    * caching can be set per method
    * client sending request can invalidate cache with header Cache-Control: max-age=0
    * can flush(invalidate) entire cache if you want
    * cache can be encrypted
    * cacpcaity can be between .5GB to 237GB

* errors
    * 4XX- indicates request sent from client was malformed/bad/not authorized
    * 403- access denied
    * 429-quota exceeded/throttle
    * 5XX- indicats an error on the server side
    * 502-


* security
    * can load SSL certs onto API GW
    * use route 53 to define a CNAME
    * resource policy that controls who can access the API
        * AWS accounts, CIDR ranges, IPs, VPC's
    * IAM execution roles for API GW 
        * to be able to invoke/access AWS services like lambda, s3
    * CORS
        * can enable access from certain domains or from all domains

* authentication(uses authorizers in API gateway)
    * IAM
        * good for private interal use, pass IAM creds in headers
    * Lambda authorizor
        * custom auth logic
        * use lambda to verify custom 3rd party auth(Oauth,SAML)
        * will use the lambda to send a request to a 3rd party the return if auth or not(e.g., Auth0, Firebase, or self-issued JWT tokens)
    * Cognito
        * AWS service that handles users and authorization
        * client authenticates with Cognito and gets a JWT token
        * it passes the token to API gateway which then checks with cognito user pool
        * the user will then be included with the

* logging/monitoring/traces
    * cloudwatch logs/metrics
        * can log full request/responses
        * can send logs to kinesis fire hose
        * metrics per stage and have standard metrics like latency, cachecount, etc
    * xray
        * can get tracing throught the entire API GW to Lambda



* Usage plan and API keys
    * usage plan
        * can define who can access, quota(total how much), throttle/meter(how much in a time period)
        * auth is via API key
        * 429 too many requests error

* throttling limits
    * API Gateway has two levels of throttling:
        * Account-Level Limits:
            * By default, AWS API Gateway limits the number of requests per region per account.
            * Soft limits:
                * 10,000 requests per second (RPS).
                * 5,000 concurrent requests (burst).
                * These can be increased by submitting a request to AWS Support.
        * API-Level Limits:
            * You can set specific rate and burst limits on individual API Gateway stages or methods.
            * Rate limit: Steady-state number of requests per second.
            * Burst limit: Maximum number of requests that can be handled temporarily (short-term spike).


* websocket
    * the web socket stays open with the API Gateway!
    * can trigger lambdas when sending a json to the api gateway!
        * can either use an action key in the json which triggers a route in API gateway or have a generic lambda handler that will trigger other lambdas based on values in the json payload you send it
    * note the lambda will not be aware of the websocket connection, so it will send it's response back to a specific url representing that api gateway connection on that api gateway stage. 
        * wss://abc123xyz.execute-api.us-east-1.amazonaws.com/dev/@connections/{some cnnection id}
```
    # inside the lambda, event is recieved from api gw
    connection_id = event['requestContext']['connectionId']
    domain_name = event['requestContext']['domainName']
    stage = event['requestContext']['stage']
    
    # API Gateway Management API Endpoint
    endpoint = f"https://{domain_name}/{stage}"
    apigateway_management_api = boto3.client('apigatewaymanagementapi', endpoint_url=endpoint)

```
    * can invoke dynamo without using a lambda using AWS service proxy(essentially a mapper)
    * API Gateway supports direct service integrations with DynamoDB through its AWS service proxy feature. This allows API Gateway to directly perform actions like PutItem, GetItem, UpdateItem, or Query on DynamoDB tables.


#### Integration
* Can integrated DIRECTLY with these service with no lambda needed

* AWS Lambda
* Amazon S3
* Amazon DynamoDB
* Amazon SNS (Simple Notification Service)
* Amazon SQS (Simple Queue Service)
* AWS Step Functions
* Amazon Kinesis
* Amazon RDS (Relational Database Service)
* AWS AppSync
* Amazon CloudWatch
* AWS Secrets Manager
* AWS IoT Core
* Amazon ECS / Fargate
* AWS WAF (Web Application Firewall)




#### Usages
* versioning
* authorization
* traffic management
    * API Key
    * throttles
* huge scale
* serverless
* req/resp transformations
* OpenAPI spec
    * can generate a client library from that spec in many programming langs
    * allows documentation
* CORS



#### Architecture
* want to upload files through API GW to s3
    * will have a 10MB limit

* want to have an API GW redirect to s3 url
    * can use an lambda to generate an 'signed url'
    * 'signed url' is a url with an AWS signature and upload expiration and file metadata for secure uploads

*  client -> send request -> API GW -> Lambda, which generates a signed url to send back to client
*  client uses signed url -> upload to s3




# web_layer

## load_balancers.md
* 4 kinds(in order of release date)


* Classic
    * old generation
    * HTTP, HTTPS, TCP, SSL(secure TCP)
    * Health checks can be L7 via HTTP or layer 4 via TCP
    * only one SSL certificate allowed(must use multiple CLB for multiple)
    * TCP passes all the traffic to the EC2 instance only way 

    
* Application
    * HTTP, HTTPS, Websocket
    * Layer 7 only HTTP(S), Websocket, HTTP/2
    * multiple SSL certs allowed
    * Can load balance to multiple target groups i.e. HTTP applications/services 
    * health checks at the target group level
    * Can load balance to multiple services/applications on the same machine which is a great fit for containers
        * dynamic port mapping
    * can write routing rules to LB traffic to in detail:  path, headers, query string, etc.
        * ex: one route for search, and one for login
    * can integrate it directly with various services
        * EC2
        * ECS on EC2
        * ECS on Fargate
        * AWS Global Accelerator
        * AWS WAF
        * S3 (Static Website Hosting)
        * API Gateway (as an HTTP backend)
        * Lambda


* Network LB
    * TCP, TLS(secure TCP), UDP
    * handle millions of RPS
    * this is the speed LB, very high performance
    * less latency than ALB also
    * has one static IP per AZ
    * supports assigning an Elastic IP-helpful for whitelisting an IP
    * not included in AWS free tier
    * target groups: EC2 instance, or an Appliation Load Balancer
    * can only send traffic to privte ips


* Gateway LB
    * operates at layer 3(network)-IP protocol
    * deploy scale/manage 3rd party network virtual appliances in AWS
    * Firewalls, intrusion detection, deep packet inspection, payload manipulation
    * operates on IP packets (layer 3)
    * transparent exit/entry
    * distribute to applicances
    * Uses Geneve protocol on port 6081
    * allows you to spin up a bunch of parallel traffic analyzer tools and get the traffic Load Balanced between them
    * After traffic analysis the applicancds send the data back to LB which forwards to the application
    * target groups: EC2, or private IPs

* target groups
    * EC2 instances: http
    * ECS tasks: http
    * Lambda -> http request tranlated into json
    * any private ip address: http

* DNS
    * all load balancers have a DNS url upon creation
    * AWS Network Load Balancer (NLB) provides a unique zonal DNS name for each availability zone (AZ) where it is deployed. These zonal DNS names allow clients to directly access specific load balancer nodes in a particular AZ, which is useful for certain advanced networking scenarios
    * Normal regional url: <load-balancer-name>-<hash>.<region>.elb.amazonaws.com
    * Zonal url: <AZ>.<load-balancer-name>-<hash>.<region>.elb.amazonaws.com
    * This has a url for each AZ in the LB and has a url for the LB in general
    
* cross zone load Balancing
    * LB disgtributes traffic evenly across all registered instances in ALL AZs
    * i.e. if have two instances i one AZ and 8 in another AZ the traffic will STILL be distributed even across all 10 instances
        * i.e. 10% of traffic to each instance no matter the AZ
    * always on (cant be disabled in ALB, must be enabled in all the rest)



* sticky session
    * the client always communicates with the same instance
    * makes sure user doens;t lose session data (i.e. if cookie in memory or somegthing)
    * enabling this, may bring imabalance to the load over back end EC2 instances


* Routing algorithms
    * Least Outstanding Request
        * instance with lowest number or pending/unfinished requests
        * CLB and ALB have
    * Round robin
        * just cyclers thru
        * ALB, CLB
    
    * Flow Hash
        * take a bunch of data from the request packet and generate a hash and route based on that hash
        * with this its permanantly sticky




#### ways to connect to load balancers
Yes, among the AWS load balancers, Network Load Balancers (NLBs) can be internet-facing and associated with Elastic IPs (EIPs). However, Application Load Balancers (ALBs) and Gateway Load Balancers (GWLBs) do not directly support Elastic IPs.

Here’s how Elastic IPs work with different load balancer types:

1. Network Load Balancer (NLB)
* Supports Elastic IPs: 
* For each subnet where you deploy an NLB, you can associate a specific Elastic IP (EIP). This makes the NLB's public-facing IP address static, which is ideal for predictable client-side configurations.
* Internet-Facing:
* NLBs can be configured as internet-facing to expose services to the public internet.
* Use Case:
* Ideal for applications requiring low latency, high throughput, and static IPs (e.g., FTP, gaming, VoIP).

Steps to Configure an Internet-Facing NLB with EIP:
* Create an NLB with internet-facing scheme.
* Add listeners for the required ports (e.g., 21 for FTP).
* Associate an EIP for each public subnet used by the NLB.

2. Application Load Balancer (ALB)
* Does Not Support Elastic IPs:
* ALBs are designed to route traffic using DNS-based endpoints rather than static IPs. They use dynamic public IPs managed by AWS.
* Internet-Facing:
* ALBs can still be configured as internet-facing but rely on AWS DNS names (e.g., abc123.elb.amazonaws.com) instead of static IPs.
* Use Case:
* Best suited for HTTP/HTTPS workloads with advanced Layer 7 routing features.

Workaround for Static IPs with ALB:
* Use a Static IP Proxy:
* Deploy an NLB in front of the ALB and associate EIPs with the NLB. The NLB forwards traffic to the ALB.
* Use AWS Global Accelerator:
* Provides static IPs that route traffic to the ALB via a global edge network.

3. Gateway Load Balancer (GWLB)
* Does Not Support Elastic IPs:
* GWLB is designed for traffic inspection and routing through virtual appliances, not for public internet-facing use.
* Use Case:
* Ideal for deploying and managing third-party virtual appliances (e.g., firewalls, intrusion detection systems).

Workaround for Public Traffic with GWLB:
* Use an NLB with EIP in front of the GWLB for public-facing traffic.

4. Classic Load Balancer (CLB)
* Supports Elastic IPs:
* For each subnet where you deploy a CLB, you can associate an EIP.
* Internet-Facing:
* CLBs can be internet-facing and use EIPs for static IP configuration.
* Use Case:
* Legacy applications still relying on CLBs for Layer 4 and basic Layer 7 routing.

Summary of Elastic IP Compatibility
Network Load Balancer (NLB): Supports Elastic IPs and can be internet-facing, ideal for low latency and static IP needs.
Application Load Balancer (ALB): Does not support Elastic IPs but can be internet-facing with advanced routing for HTTP/HTTPS.
Gateway Load Balancer (GWLB): Does not support Elastic IPs and is not internet-facing, used for traffic inspection.
Classic Load Balancer (CLB): Supports Elastic IPs and can be internet-facing for legacy workloads.

Conclusion
* If you need static IPs with internet-facing capability, the best choice is the Network Load Balancer (NLB) or Classic Load Balancer (CLB).
* For ALBs or GWLBs, workarounds like pairing with an NLB or AWS Global Accelerator can provide static IP functionality.

Would you like step-by-step instructions for setting up an NLB with EIPs?

# containers

## Fargate.md
* No EC2 foundation management at all
* considered "serverless"
* Fargate manages underlying infrastructure
* submit tasks to fargate and these are created automatically without you having to think about underlying infra.

* you just create task definitions
    * specify how much CPU/RAM you need

* to scale, just increase number of tasks or enable autoscaling
* default networking mode is awsVpc

* can use spot instances for cost savings at reliability tradeoff
# containers

## ECR.md
* store/manage docker on AWS
* public/private images
* fully integrated with ECS
* IAM integration

* vulnerability scanning, image tags, image lifecycle


* ECR is region based!

* ECR supports both cross region/cross account replication
    * if you configure this, you can push image to ECR in one region and it will be replicated to other regions/accounts

* image scanning
    * scan these containers to look for vulnerabilitys
    * manual(user triggered) or automatic(scan on push)
    * two types:
        1. basic scan
            * looks for common vulnerabilities
            * free
        2. enhanced scanning
            * uses amazon inspector($$)
            * looks for operating system and programming lang vulnerabilities
            * costs money
    
# containers

## EKS.md
* managed Kubernetes cluster 
* k8's open source, ECS is not
* alternative to ECS for container orchestration of containers
* K8's is cloud agnostic, can migrate

* EKS supports 2 launch modes:
    1. ECS - to manage the worker nodes
    2. Fargate - to have serverless 


* EKS worker nodes in private subnets (pods)
* Nodes can be autoscaled
* can setup  load balancers to talk to the web

* Node management: 
    1.  managed node groups
        *  AWS creates/manages nodes for you
        *  support for on demand and spot
        * AWS manages the lifecycle of nodes, including provisioning, patching, and upgrades.
        * You still manage the AMI, Kubernetes versions, and instance configurations.
        * good for if you have custom configurations you need

    2. self managed nodes
        * you manage everythign
        * create nodes and register
        * manage those with ASG
        * can use EKS optimzed AMI
        * also supports on demands 

    3. fargate mode
        * don't even look at nodes
        * AWS handles everything


* data volumes 
    * need to specify a StorageClass manifest in your EKS cluster
    * leverages Container Storage Interface(CSI) driver
    * Support for
        * EBS
        * EFS(only storage that works with fargate)
        * FSx for Lustre
        * FSx for NetApp ONTAP
# containers

## ECS.md
* Run multiple containers on same machine
* Easy service discovery to enhance communication

* Direct integration with ALB and NLB

* Auto Scaling

* run batch processing and scheduled tasks
    * run on demand/reserved/spot instances

* migrate applications to the cloud 
    * dockerize legacy apps running on prem
    * move docker containers to run on ECS

* ECS Cluster
    * logical grouping of ECS instances 
    * AWS runs ECS service on top of these instances

* ECS Service
    * defines how many tasks should run and how they should be run
    * similar to a k8 deployment/replicaSet
    * manages pods and ensures the desired number of replicas are running, handles updates, ensures 

* ECS Task 
    * literally a container
    * Task Definition
        * metadata in JSON form to tell ECS how to run a Docker container
    * instance of a task definition - running a Docker container
    * a run once ephemeral deal
    * Provide details for each container, such as:
        * Container image(s) to use.
        * CPU and memory requirements.
        * Port mappings.
        * Environment variables and secrets.
        * Networking mode and volumes.
    * Containers are created from Task Definitions and run on the EC2 cluster beneath it

* ECS Service
    * A task in it's basic form is a run once ephemeral workload
    * A service is a higher-level abstraction that manages and maintains the desired number of running tasks for long-lived applications
    * A service manages one or more tasks
    * A service defines:
        * Desired task count.
        * Load balancer integration (if needed).
        * Deployment strategy (e.g., rolling updates).
  
* ECS agent
    * run on all ECS cluster instances
    * it is a daemon on the actual instance and communicates with ECS service and the docker runtime on the instance 
    * will spin up containers when instructer
    * will monitor health
    * will report status of the container/s to ECS

* ECS service
    * will listen to the ECS agents on all of the instances and then configure what needs to be configures inside of AWS
    * i.e. Load Balancer/target groups, Cloudwatch, etc

* EC2 foundation
    * When you create an ECS cluster in ECS it:
    * sets up the instance profile 
    * will also install the ECS agent on the EC2 instances in this cluster
    * attaches the correct IAM role to the instances
    * you setup ASG such that it knows it's a part of the cluster and will spin up instances in the ECS subnet attached to the named ECS cluster with the correct ECS IAM role

* ECS IAM roles
    * EC2 instance profile that the containers are on: instance specific calls, logs, etc.
    * ECS Task IAM role: container/task specific calls, aws services, etc.
    * Available to attach to cluster when you create your ECS cluster

* ECS integration with ALB
    * if you run the same container multiple times on one instance will need to expose the service on different ports
    * ECS will assign a dynamic port on the host for each container and registers that ip/port with the target group attached to the service 
    *  called dynamic port mapping
    
* ECS logging
    * The ECS agent communicates directly with CloudWatch Logs for container logs.
    * Task and instance-level metrics are sent to CloudWatch either through the ECS control plane or optional tools like CloudWatch Agent or Container Insights.
    * For detailed logging and metrics, configuration in the task definition or ECS cluster settings is required.

* Can integrate Secrets and Configurations as Environmental variables into Docker containers
    * SSM parameter store
    * secrets manager

* ECS tasks types of networking
    1. none: no network connectivity, no port mappings
    2. bridge: docker default networking
    3. host: use underlying host network interface
    4. awsVpc: every task launched gets it's own ENI and private IP address
        * allows security group, VPC flow log,  monitoring, etc. like any ENI
        * this is default mode for fargate

* ECS TASK autoscaling
    * do not need a ASG, ECS handles scaling up/down the tasks on the instances
    * can trigger based on a variety of metrics in Cloudwatch
    * can also step wise scale and scheduled scale just like in an normal ASG

* ECS EC2 autoscaling
    * If tasks don't have enough resources will need to scale number of EC2 instances
    * ECS integrates with ASGs to handle infrastructure scaling automatically.
    * ECS determines if additional EC2 capacity is required to place new tasks and triggers the ASG to scale.
    * ECS uses a capacity provider to autoscale
    * a capacity provider is to determine how many instances are required to serve the desired number of tasks and scale the number of instances to match that value
    * instead of a CPU or RAM metric the ASG will autoscale to match the number of tasks(containers) needed
        * note: the tasks definition you specify the CPU/Mem a task needs when it's created
    * The capacity provider will calculate the lower bound on the number of instances required based on the number of tasks, taking into account vCPU, memory, ENI, ports, and GPUs of the tasks and the instances
    * there's a tiny algorith that goes into figuring this all out


* ECS spot instances 
    * can use spot instances to back an ASG in ECS
    * good for cost but impact reliablity





    great capacity provider reference:
    https://medium.com/yipitdata-engineering/instance-auto-scaling-using-aws-capacity-providers-9ea7e66e311f
# containers

## AppRunner.md
* fully managed service you can use with no infrastructure knowledge needed
* scalable
* start with source code or a docker image
* you configure settings like:  
    * cpu, memory, enable autoscaling?, health check, load balancing
* can provide access to VPC which means can access all AWS resources(database, cache, message quueue)
* it automatically builds/deploys webapp
* you can access it using a url

#### Architecture
* upload docker image to ECR
    * have ECR replication cross region
* have a dynamo DB
    * have dynamo globally replicated across regions

* use an app runner service in more regions and it now has access to both ECR and Dynamo 

* can use route53 for DNS load balancer and set it to direct to an endpoint based on which has the least latency.
# containers

## ECS_EKS_anywhere.md
* ECS anywhere
    * easily run containers on customer managed on prem hard ware
    * can deploy native ECS tasks in any environment
    * the hosts communicate with ECS control plane in AWSa
    * ECS container agent and SSM agent need to be installed on the host(will register with AWS cloud)
    * specify the "External" launch type for our services and tasks in ECS on AWS
    * must have a stable connection to AWS (region with your ECS control plane)
    * useful for compliance, reduced latency
    * run apps closer to their on prem services


* EKS anywhere
    * create/operate kubernetes cluster operated outside AWS
    * use AWS EKS distro (AWS bundled release of EKS)
    * This works without any connection to AWS!
    * can use EKS connector to connect the on prem EKS to AWS cloud and use EKS console on prem.

    * Managing your own Kubernetes cluster involves maintaining multiple tools (like kubeadm, Helm, or others), dealing with compatibility issues, and ensuring all components (e.g., etcd, networking, etc.) are configured correctly.
        * EKS-A abstracts much of this complexity.
        * ALLOWS INTEGRATION WITH other AWS services like cloudwatch, systems manager, etc.
        * many third-party monitoring, logging, and security tools are integrated already
        * simplifies tasks like cluster upgrades and backup management, which can be complex in self-managed environments.
        * EKS Anywhere ships with pre-configured, validated networking, storage, and observability components.

    
