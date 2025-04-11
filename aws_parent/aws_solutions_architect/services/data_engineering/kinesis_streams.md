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