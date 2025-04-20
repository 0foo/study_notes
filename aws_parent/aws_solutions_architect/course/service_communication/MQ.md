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