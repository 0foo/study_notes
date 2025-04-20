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
