### Eventbridge

* What is EventBridge?
  * A fully managed event bus service
  * Allows you to build event-driven applications using events from AWS services, SaaS apps, or custom sources

* Key Concepts:
  * Event Bus:
    * Default, Partner, or Custom
    * Receives and routes events
  * Rules:
    * Match incoming events using patterns
    * Route matched events to targets
  * Event Pattern:
    * JSON structure that defines what events to match (by service, type, resource, etc.)
  * Target:
    * AWS services like Lambda, Step Functions, SQS, SNS, Kinesis, etc.

* Sources of Events:
  * AWS services (e.g., EC2, CodePipeline, S3, DynamoDB)
  * SaaS partners (e.g., Zendesk, Datadog, PagerDuty)
  * Custom applications (via PutEvents API)

* Use Cases:
  * Orchestrate microservices
  * Trigger workflows (e.g., Lambda or Step Functions)
  * Audit and compliance tracking
  * Real-time data processing
  * Integrate SaaS tools with AWS services

* Features:
  * Schema registry (for event validation/discovery)
  * Archive and replay events
  * Event transformation (with input transformers)
  * Fine-grained access control with IAM


* how it works example:
    * S3 emits events (e.g., object created, deleted, restored)
    * If EventBridge is enabled for the bucket, those events are automatically sent to the EventBridge default event bus
        * no need for SNS or lambda intermediary
    * You write a rule in EventBridge to match those events and send them to a target (Lambda, SQS, etc.)








* formerly known as cloudwatch events


* periodic: schedule cron jobs in the cloud
    * trigger a lambda function at some period

* reactive: can set rules that react to a service doing something
    * i.e. a root user logs in
    * will send an email


* a lot of services can send to Event Bridge


* cloudtrails can intercept ANY API call made in your AWS accounts and the send to Event Bridge for further processing/notifying/alert/etc/

* Event bridge output is a json document that represents the details about your event

* This JSON document can be sent to a lot of services and used to trigger a lot of things(ECS, Lambda, SQS, Kinesis, etc.)

* can archive the events- indefintite or set time, 

* can replay these archived events-troubleshooting, debugging

### Event Bus

* event brige is default internal event bus
* also have a partner event bus

* Partner Event bus
    * AWS has integrated with third party partners and they send their events into your partner event bus
    * can react to changes happening outside of AWS

* Custom event bus-can define


### Schema Registry
* Event bridge recieves events from a lot of places
    * what do these events look like?
    * JSON
    * store in schema registry
    * event bridge anaylye events in bus, then infer the schema
    * Schema registry allows you to generate code for your application that can output events properly formatted to an specific schema
    * Schema can be versioned as well

###  resource based policy for EvBr
    * manage specific policies for a specific event bus
    * a speicific event bus can allow/deny from other region or other accounts

* Can have a central Event Bus for all your AWS accounts
    * these events will be aggregated
