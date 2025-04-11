#### Alexa for business
* book meeting room, increase meeting room efficiency


#### Workspaces
* Secure cloud desktop
* helps eliminate on prem VDI (virtual desktop infrastr..)
* pricing on demand or monthly
* integrated with microsoft AD
* Workspace updates managers -> keeps applications updated
* Windows update -> keeps windows updated
    * by default updates turned on
* can define update maintenance windows 
    * default is 12 AM to 4AM
    * workspaces will reboot automatically for you

* Multi region failover
    * must use an AD connector and not a multi region AD

* IP access control groups
    * similar to security groups for Amazon workspaces
    * list of IP's/CIDR ranges that users are authorized to connect from
    * must whitelist any VPN or NAT

#### Appstream
* simply streams an app in a web browser
* no machine required
* like geforce now but for apps

#### Device farm
* if want to test an mobile/web application across multiple devices
* runs across real browsers and mobile devices
* fully automated using a framework
* Will generate videos and logs to document the issues encountered
* can also remotely log into the devices to debug


#### Macie
* fully managed data security and privacy service
* uses machine learning to discover and protect your sensitive data
* alerts if it discovers PII (personally idenitifable information)
* put the data in S3 for Macie which then notify via event bridge
* can integrate event bridge with SNS topic, lambda function

#### SES (simple email service)
* Fully managed service to send emails at scale
* allows for outbound and inbound emails
* app communicates with it via API, AWS console, SMTP
* reputation dashboard, performance insigts, anti-spam feedback
* stats on deliveries, bounces, feedback loop results, email opens
* supports DKIM(domain keys identified mail) and SPF(sender policy framework)
* flexible IP deployment: shared, dedicated, customer owned IP's
* transactional, marketing, bulk email communications 
* Configuration sets in Amazon SES are used to group and manage email sending settings.
    * Main purposes:
        * Track email sending metrics (opens, clicks, bounces, complaints)
        * Control where metrics are sent (CloudWatch, Kinesis Data Firehose, SNS)
        * Apply sending policies (IP pool selection, event publishing)
    * Key features:
        * Event destinations:
            * CloudWatch – monitoring and alarms
            * SNS – immediate , real-time notifications
            * Kinesis Data Firehose – data storage and analytics
        * IP pool assignment:
            * Assign specific IP pools to manage deliverability and reputation

    * An event is a recorded action or outcome of an email message.
    * Common types of SES events:
        * Send: the email was successfully accepted by SES for sending
        * Delivery: the email was successfully delivered to the recipient's mail server
        * Bounce: the email could not be delivered (hard or soft bounce)
        * Complaint: the recipient marked the email as spam
        * Open: the recipient opened the email (tracked with a pixel)
        * Click: the recipient clicked a link in the email
        * Reject: SES rejected the email before attempting delivery (e.g. policy violation)
        * Rendering Failure: the email couldn’t be rendered for open/click tracking
    * Events are useful for:
        * Monitoring email performance
        * Debugging delivery issues
        * Triggering alerts or workflows using services like SNS or Lambda
        * Analyzing user engagement through clicks and opens
 
    * Sending authorization and suppression lists:
        * Control sending behaviors with rules or suppression lists
    * How it works:
    * Create a configuration set
        * Define event destinations and optional IP pool
        * Specify the configuration set name when sending emails
        * SES applies the rules and tracks metrics accordingly
    * EXAMPLE:
        * Open events (along with clicks, bounces, deliveries, etc.) can be sent to Kinesis via event destinations.
        * To do this:
            * Create a configuration set in Amazon SES
            * Define an event destination within the config set
            * Choose "Kinesis Data Firehose" as the destination type
            * Select which event types to publish (e.g., open, click)
        * Benefits of sending events like opens to Kinesis:
            * Real-time stream processing
            * Store events in S3, Redshift, or Elasticsearch
            * Build dashboards, analytics pipelines, or alerting systems


### Pinpoint
* main functions:
    * marketing campaigns: has message templates, delivery schedules, highly-targeted segments, and full campaigns
    * deliver: integrates with SNS, SMS
    * track: can recieve events into various locations for tracking analysis 
* scalable 2 way inbound/outbound marketing communications service
* supports email, SMS, push, voice, and in-app messaging
* ability to segment and personalize messages with the right content to customers
* can recieve replys
* can scale to billions of messages per day
* run campaigns by sending bulk marketing email
* bulk transactional SMS messages
* all the events such as text or email success, deliver will be delivered to SNS, Firehose, Cloudwatch logs
    * easily build automation 


### EC2 image builder
* used to automate the creation of virtual machines(EC2 AMI's) or container images
* create, maintain, validate, test 
* can run at set custom schedules (i.e. weekly, on push, etc.)
* free service, only pay for underliying resources
* can publish the AMI toi multiple regions and accounts


EC2 Image builder will:
spin up a blank EC2 instance
will run the build components software
will create AMI From this
will test by:
     spinning up a new EC2 instance from the AMI 
     run all the test suite (AMI working, secure, etc)
AMI will be distributed to multiple regions and/or accounts




CICD Architecture
* code pipeline defines all of the following
1. code commit
2. code build
3. cloudformation to automate and launch EC2 image builder service 
4. EC2 image builder service will then take last code delpoyed and create an AMI out of it
5. Pipeline will then use cloudformation to rollout the AMI in production to a large group of instance behind an ASG and can do canary style one at a time



#### IoT core
* easily connect IoT devices to the cloud 
* serverless, secure, scalable to billions of devices and trillions of messages
* integrates with alot of AWS services (lambda, sagemaker, s3, etc)
* gather, process, analyze, and act on data 
* IoT topic
    * take data in, in various formats
    * setup one or more IoT rules
    * rules have one or more actions
    * actions related to AWS services(many options, S3, SNS, kinesis, dynamo, lambda, sQS, etc.)
    * so can send the IoT data to one of many rules which has one of many actions which connects to an AWS service
    * important integration:
        * kinesis firehose
            * can do transformations in the firehose
            * persist in S3, redshift, OpenSearch