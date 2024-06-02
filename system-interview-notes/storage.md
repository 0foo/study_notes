
<span style="text-decoration:underline;">Push/Pull/Hybrid</span>



* 1. Pull: Clients can pull the News-Feed contents from the server at a regular interval or manually whenever they need it. Possible problems with this approach are a) New data might not be shown to the users until clients issue a pull request b) Most of the time, pull requests will result in an empty response if there is no new data.
* 2. Push: Servers can push new data to the users as soon as it is available. To efficiently manage this, users have to maintain a [Long Poll](https://en.wikipedia.org/wiki/Push_technology#Long_polling) request with the server for receiving the updates. A possible problem with this approach is a user who follows a lot of people or a celebrity user who has millions of followers; in this case, the server has to push updates quite frequently.
* 3. Hybrid: We can adopt a hybrid approach. We can move all the users who have a high number of followers to a pull-based model and only push data to those who have a few hundred (or thousand) follows. Another approach could be that the server pushes updates to all the users not more than a certain frequency and letting users with a lot of followers/updates to pull data regularly.

<span style="text-decoration:underline;">File Storage/Block Storage/Object Storage</span>



* File Storage
    * manages data as a hierarchy of files
    * fixed metadata in file systems (filename, creation date, type, etc.)
* Block Storage
    * manages data as blocks within sectors and tracks
* Object storage/Blob storage
    * also known as blob storage
    * manages data as objects
    * Each object typically includes the data itself, a variable amount of [metadata](https://en.wikipedia.org/wiki/Metadata), and a [globally unique identifier](https://en.wikipedia.org/wiki/Globally_unique_identifier). 
    * completely custom meta-data (it’s stored separately from the object)
    * Like a large hash table, no hierarchy built in, can use UUID or GUID for the object key
    * by using GUIDs instead of the hierarchies characteristic of file storage or block storage, object storage allows for infinite scalability. In other words, by doing away with structure, there’s more room for data.
* distributed file storage(s3, HDFS hadoop)

<span style="text-decoration:underline;">Databases</span>



* types:
* Key Value
    * ex: redis, dynamo
* NoSql
    * ex: mongo
* Relational
    * database schema-entities/relationships
    * any SQL database
* Graph
    * TBI
* Data Warehouse
    * ex: redshift, bigquery

<span style="text-decoration:underline;">Data Partitioning</span>



* generic term for dividing data across tables or databases.
* <span style="text-decoration:underline;">Sharding</span> is one specific type of partitioning: what is called horizontal partitioning.
    * replicate the schema across (typically) multiple instances or servers, using some kind of logic or identifier to know which instance or server to look for the data. An identifier of this kind is often called a "Shard Key".
* 
* Consistent Hashing
    * tbi
* Horizontal Partitioning
    * Also known as sharding or range based partitioning
    * In this scheme, we put different rows into different tables. 
    * Problem is that if the value whose range is used for partitioning isn’t chosen carefully, then the partitioning scheme will lead to unbalanced servers
        * for example if zip code is used as partitioning key, new york servers will be super over whelmed
    * Store data into separate partitions based on some condition
        * Examples
            * First letter of the data
            * Hash Based Partitioning
                * Take a hash of the data and store
                * Also could be an attribute * the modulus of the number of shards
                * if user id is 143 and there’s 10 shards
                * 143 % 10 = 3 
                    * stored on shard number 3
                * Note: It effectively fixes the number of DB servers because if you increase the server count you will change the result of the modulus or server based hash function
                    * solution: consistent hashing
* Vertical Partitioning
    * data is partitioned based on FEATURE
    * ex: user profile information on one DB server, friend lists on another, and photos on a third server.
* Directory Based Partitioning
    * create a directory server that stores the mappings
    * query the Directory Server to find out where the data resides
* Partitioning Problems
    * Joins and Denormalization
        * once a database is partitioned and spread across multiple machines it is often not feasible to perform joins that span database partitions.
    *  Referential integrity
        * trying to enforce data integrity constraints such as foreign keys in a partitioned database can be extremely difficult.
    * ** **Rebalancing
        * results from uniform partitions or a lot of load on a partition
        * either we have to create more DB partitions or have to rebalance existing partitions, which means the partitioning scheme changed and all existing data moved to new locations. 
        * Doing this without incurring downtime is extremely difficult.
        * Directory based partitioning helps, at the expense of adding complexity to the system

<span style="text-decoration:underline;">Key Generation Service</span>



* Avoids collisions or duplications
* generates random six letters(or more) strings beforehand and stores them in a database (let’s call it key-DB)
* Allows the service to grab the key from key-DB and KGS will mark it as used
* make sure all the keys inserted in key-DB are unique.
* KGS can use two tables to store keys,
    *  one for keys that are not used yet
    * one for all the used keys
* KGS can always keep some keys in memory so that whenever a server needs them, it can quickly provide them. 

<span style="text-decoration:underline;">Bifurcated Metadata Database Pattern</span>



* Can split database into 
    * 1. metadata database
        * stores all of the info about the record
    * 2. record database
        * stores the actual record
* Note this strategy works well for storing in an object store and having metadata in a database 

<span style="text-decoration:underline;">Bifurcated Read/Write Database Pattern</span>



* web servers and database servers have a connection limit
* Users uploading to data store through the application web servers
* Uploading users can consume all the available connections in the application connection pool, as uploading is a slow process. 
* This means that ‘reads’ cannot be served if the system gets busy with all the ‘write’ requests.
* To handle this bottleneck, we can split reads and writes into separate services. 
*  Have dedicated servers for reads and different servers for writes to ensure that uploads don’t hog the system.
    * allows scaling and optimizing these two operations independently

<span style="text-decoration:underline;">Media File Management Service</span>



* Separate media management service to manage images, videos, audio
* **this includes entirely separate upload web servers **
    * uploading large media files takes a lot of time and soaks up connection pools
    * need specialized system for this functionality
* These are large files and typically have special requirements
* Have a separate service to manage these files
* Can use object storage for media files
* Can have an upload pipeline that will save the uploaded file to an object store then submit a message to a queue for a pipeline to indicate this file needs processing.
    * will send the image through a pipeline to:
    * encode to specific formats/file size/resolutions/etc.
    * generate thumbnails
* Caching of these media files via CDN

<span style="text-decoration:underline;">Newsfeed Generation Service</span>



* news feed generation is time consuming and resource intensive requiring joining all kings
* have dedicated servers that are constantly generating news feeds 
* generates a news feed with a timestamp
* when a news feed needs to be generated, the news feed is already generated and all that has to be done is from present time to the news feed time stamp

<span style="text-decoration:underline;">Caching</span>



* take advantage of the locality of reference principle: recently requested data is likely to be requested again. 
* short-term memory: it has a limited amount of space, but is typically faster than the original data source and contains the most recently accessed items. Caches can exist at all levels in architecture, but are often found at the level nearest to the front end, where they are implemented to return data quickly without taxing downstream levels.
* Some examples of things to cache:
    * Large media files via CDN 
    * Cache hot database rows
        * Least recently used database row ejection
        * user redis or memcache
    * pregenerate commonly used queries(materialized views)
    * have separate service constantly generating and caching resource intensive function-see Newsfeed generation service
* Content Delivery Network(CDN)
    * Caching for media files
    * Typically regional
    * caching = decrease latency
    * caches media
    * proxies and caches web data at edge locations as close to users as possible.
    * CDN will check its cache and if not present will summon the data from the database and then cache it
        * may use LRU eviction if size is limited
    * NOTE: for small systems can start with a separate webserver for media files and then upgrade to a CDN down the line
* 80/20 rule
    * 20% of the data is used the most and needs to be cached
* Cache writing:
    * Write-through cache: Under this scheme, data is written into the cache and the corresponding database simultaneously. The cached data allows for fast retrieval and, since the same data gets written in the permanent storage, we will have complete data consistency between the cache and the storage. Also, this scheme ensures that nothing will get lost in case of a crash, power failure, or other system disruptions.Although, write-through minimizes the risk of data loss, since every write operation must be done twice before returning success to the client, this scheme has the disadvantage of higher latency for write operations.
    * Write-around cache: This technique is similar to write-through cache, but data is written directly to permanent storage, bypassing the cache. This can reduce the cache being flooded with write operations that will not subsequently be re-read, but has the disadvantage that a read request for recently written data will create a “cache miss” and must be read from slower back-end storage and experience higher latency.
    * Write-back cache: Under this scheme, data is written to cache alone, and completion is immediately confirmed to the client. The write to the permanent storage is done after specified intervals or under certain conditions. This results in low-latency and high-throughput for write-intensive applications; however, this speed comes with the risk of data loss in case of a crash or other adverse event because the only copy of the written data is in the cache. \

* Cache Eviction
    * what to evict when the cache is full
    * Types of cache eviction:
        * LRU
    * Least Recently Used(LRU)
1. Application keeps a count of every item hit in the cache
2. When there’s a cache miss, the application will hit the database
3. The Application will reject the item with the lowest count and insert the new item 
* LRU implemented with: Linked Hash Map
    * [https://leetcode.com/problems/lru-cache/](https://leetcode.com/problems/lru-cache/)
    * https://www.geeksforgeeks.org/lru-cache-implementation/
    * Uses Queue/Doubly Linked List and a hash
* Other types of cache eviction:
    * First In First Out (FIFO): The cache evicts the first block accessed first without any regard to how often or how many times it was accessed before.
    * Last In First Out (LIFO): The cache evicts the block accessed most recently first without any regard to how often or how many times it was accessed before.
    * Most Recently Used (MRU): Discards, in contrast to LRU, the most recently used items first.
    * Random Replacement (RR): Randomly selects a candidate item and discards it to make space when necessary.

<span style="text-decoration:underline;">ACID Guarantees </span>



* Atomicity:
* [Transactions](https://en.wikipedia.org/wiki/Database_transaction) are often composed of multiple [statements](https://en.wikipedia.org/wiki/SQL_syntax). [Atomicity](https://en.wikipedia.org/wiki/Atomicity_(database_systems)) guarantees that each transaction is treated as a single "unit", which either succeeds completely, or fails completely: if any of the statements constituting a transaction fails to complete, the entire transaction fails and the database is left unchanged.
* Consistency
    * data must meet all validation rules
    * any data written to the database must be valid according to all defined rules, including [constraints](https://en.wikipedia.org/wiki/Integrity_constraints), [cascades](https://en.wikipedia.org/wiki/Cascading_rollback), [triggers](https://en.wikipedia.org/wiki/Database_trigger), and any combination thereof. This prevents database corruption by an illegal transaction, but does not guarantee that a transaction is correct. 
* Concurrency
    * Transactions are often executed [concurrently](https://en.wikipedia.org/wiki/Concurrent_computing) (e.g., multiple transactions reading and writing to a table at the same time). [Isolation](https://en.wikipedia.org/wiki/Isolation_(database_systems)) ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially. 
* Durability
    * [Durability](https://en.wikipedia.org/wiki/Durability_(computer_science)) guarantees that once a transaction has been committed, it will remain committed even in the case of a system failure (e.g., power outage or [crash](https://en.wikipedia.org/wiki/Crash_(computing))). 
    * Means that transactions are written to non-volatile storage