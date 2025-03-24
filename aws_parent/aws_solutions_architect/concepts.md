* For exam think about
    * migration
    * price
    * capacity planning
    * is it self managed, AWS managed, serverless?
    * encryption at rest/in flight
    * security: authentication/authorization
    * location: subnet, region, AZ, VPC, AWS public, internet public, on prem, cross account

* tradeoffs
    * durability
    * reliability
    * latency
    * throughput
    * scale
    * cost

* disaster recovery terms
    * RPO (Recovery Point Objective)
        * basically time between backups which means that data is lost
        * If your RPO is 15 minutes, you must have backups or replication that ensure data is saved at least every 15 minutes. If a failure occurs, only the last 15 minutes of data might be lost.
        * the time interval between the last recoverable backup or replicated data and the point of failure
    *  RTO (Recovery Time Objective)
        * how quick a recovery happens
        * If your RTO is 1 hour, your disaster recovery processes (backups, failover, etc.) must ensure systems are fully functional within that time after an incident.


* FULLY MANAGED HAS:
    * patching
    * OS maintenance
    * optimizations
    * setup
    * configuration
    * monitoring
    * failure recovery
    * backups

* Serverless
    * none of the above are even considered
    * just given an API or DSL to use and that's it
    * no capacity planning at all

* Security concepts
    * Authentication
        * What it means: Verifying who someone is.
        * Users provide credentials (e.g., username and password, biometrics, tokens).
        * The system verifies these credentials against a trusted source (e.g., a database or identity provider).
        
    * Authorization
        What it means: Determining what someone can do or what resources they can access.




* capacity planning
    * TBD



* service communication
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

* payment
    * pay by provisioning
    * pay by usage