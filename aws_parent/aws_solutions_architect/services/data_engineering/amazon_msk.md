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