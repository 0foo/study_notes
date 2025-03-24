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