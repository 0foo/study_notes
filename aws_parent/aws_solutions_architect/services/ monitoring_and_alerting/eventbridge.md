### Eventbridge

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
