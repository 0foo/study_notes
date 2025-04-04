### Interesting aspects

* notice multiple accounts sending to a centralized event bus

* notice a summarizer lambda that pulls events off the queue and stores in dynamo DB table
* notice the DLQ (dead letter)

* slack notifier with parameter store for slack creds


* can further extend this by adding a lambda to hit the service quotas API to increase service limits