* build in service
* analyze account and provide reccomendations
    * cost optimize - KNOW
    * security
    * fault tolerance
    * performance
    * service limits - KNOW 
    * operational excellence - KNOW


* basic advisor: get 7 core checks and reccomendations
    * all customer have access

* full advisor only available to business and enterprise support plans

* cloudwatch alarms, email notifications, access via API


support plans
basic - all customers, is free, get 7 score checks via Trus.Adv
developer - pay, more support, but still only get access to the core checks
business/enterprise
    * access to full set of Trus. Adv. checks
    * can get programattic access to trusted advisor via API


### What can it check
* can check if a bucket is public 
    * CANNOT check if anything is public inside the bucket(see below)
* service limits    
    * only monitored NOT changed in trusted advisor
    * have to either open a case or use service quotas service



### increase service limits


### Check public items inside of buckets
How to check for public objects instead:

* Amazon EventBridge / S3 Events
    * Set up event notifications for changes in object ACLs or bucket policies. When an object becomes public, an event can trigger a Lambda function or another alerting mechanism.

* AWS Config Rules
    * Use AWS Config to continuously monitor AWS resource configurations. Specifically:
    * Use the managed rule: s3-bucket-public-read-prohibited
    * Use custom Config rules with Lambda to dive deeper into object-level access.

* in summary, To detect public S3 objects, not just buckets:
    * Use AWS Config Rules for ongoing compliance.
    * Use EventBridge or S3 Event Notifications to react to access control changes in real-time.