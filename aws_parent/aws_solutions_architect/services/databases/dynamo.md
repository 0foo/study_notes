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