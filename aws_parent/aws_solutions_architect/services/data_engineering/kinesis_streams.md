#### Major rundown
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



#### General description
* ingest data 
* NOTE: SQS recieves messages (around 256 KB)



#### Throughput
* Data streams are divided into shards, which determine the stream's capacity.
* Streams can scale by adding or removing shards.
* if need more read/write throughput need to add more shards
* multiple applications can consume from the same stream
    * SQS can't do that as a consumer takes the message from the queue
    * pub/sub architecture for streaming data 
* once data inserted into Kinesis it can't be deleted, is immutable
* can autoscale

#### Producers
* You write data to a stream, not directly to a shard. 
    * You specify the data payload and a partition key.
    * Kinesis uses the partition key to determine which shard the data will be routed to.
    * The partition key is hashed using a MD5 hash function, and the resulting hash determines the shard.
    * ensure you have a random partition key such that data is distributed equally amongst the shards

* Each shard in the stream has a hash range.
```
Example:
    Shard 1: Hash range 0 to 2^128/3
    Shard 2: Hash range 2^128/3 + 1 to 2^128*2/3
    Shard 3: Hash range 2^128*2/3 + 1 to 2^128 - 1
```
* The hash of the partition key determines which shard the record is sent to.


* You do not need to manage shards directly when writing data—the stream handles this distribution based on the partition key.
* Amazon Kinesis Data Streams automatically assigns records to specific shards based on the partition key you provide when sending data.
* Applications, devices, or services send records to a data stream.
* The stream ingests data in real-time and organizes it into shards based on the partition key.

#### Consumer
* When you access data from an Amazon Kinesis Data Stream, you pull data from a shard, not directly from the stream as a whole. The stream is composed of multiple shards, and each shard contains a subset of the data based on the partition key that determined its placement.

* When consuming data, your application reads from each shard in the stream separately.
* The consumer must poll all shards in the stream to retrieve all the data.*


#### Retention
* data retention is 24 hours by default can increase up to 365 days
* data is STORED there until it expires

#### Capacity planning
* two modes: 
    1. on demand: scales automatically
    2. provisioned: you managed number of shards over time (this was first original mode of streams)

* can send single or batch of messages
* number of shards can evolve over time 
* can reshard or merge shards
* records ordered per shard


#### Producers
* AWS SDK: simple producer
* Kinesis Producer Library(KPL)
    * batch, compression, retries, C++, Java
    * library for C++/java
    * for your own application
* Kinesis agent (built with KPL)
    * installed on hosts and run to monitor log files and send to Kinesis directly
    * can write to either KDStreams or KDFirehose


#### Consumers
* AWS SDK: simple consumer
* Lambda (through even source mapping)
* Kinesis Client Library(KCL)
    * read in parallel from kinesis stream
    * checkpointing, co-ordinated reads across multiple ec2 instances
    * can spin up multiple EC2 instances which all claim part of the work in each shard by setting up checkpoint claims in dynamo



#### Limits
* if need more read/write throughput need to add more shards
* A shard is a unit of capacity within a stream.
* Each shard can:
    * Ingest up to 1 MB/sec or 1,000 records/sec.
    * Output up to 2 MB/sec.

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