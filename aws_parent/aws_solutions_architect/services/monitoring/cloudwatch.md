* Cloudwatch Default Metrics
    * provided by many AWS services
    * by default for EC2 standard monitoring is 5 minutes
        * can enable detailed which gives you metrics every 1 minute
    * CPU, Network, 
    * RAM is NOT build in metric with standard 
    * to get memory will need to create a custom metric and use the Cloudwatch Unified agent

* Custom metric
    * Default Resolution is one minute
    * can enable high resolution mode and get that down to 1 second


* Cloudwatch Alarm integrations
    * can trigger these things (know this)
        * EC2 action (reboot, stop, terminate,recover)
        * autoscaling
        * SNS 
            * notifications (emails, chats, etc)
            * from SNS can also send to:
                * SQS
                * Lambda function
                    * can use this to trigger Route 53 to shift traffic away from instance with problems
        * can send alarm to EventBridge
            * Kinesis
            * Step Function
            * Lambda function
            * etc


* Cloudwatch Dashboards
    * Display metrics and Alarms
    * Show metrics of multiple regions

* Cloudwatch Synthetics Canary
    * configurable script that monitors your API's, URL's, Websites, etc.
    * Run some sort of health check inside your canary
    * Regularly run a check to reproduce customer behavior with a script to find issues before the customers does
    * Check availability and latency of endpoints
    * Can store the latency data and screenshots of UI
    * trigger a cloudwatch Alarm if there's issues
    * scripts written in node/python, with a headless Chrome browser included
    * Blueprints
        * heartbeat monitor
        * API canary(basic read write functions of APIs)
        * Broken Link Checker(pass in a URL and will ensure that all links are not 404)
        * Visual Monitoring(compare periodic screenshot with a baseline screenshot)
        * Canary Recorder   
            * used with Cloudwatch synthetics recorder
            * lets your record your actions on a website and generate a script to replay
        * GUI workflow builder
            * create, customize, and manage canary scripts visually and programmatically to monitor your applications and APIs.


### Cloudwatch Logs
* Sources: How to push data into CW logs 
    1. SDK
    2. Logs agent
        * Can be installed on EC2 or on prem hosts
    3. Unified Agent
    4. Integration with a service - some services have direct integrations with CS logs
        * ECS
        * Beanstalk*
        * Lambda
        * VPC flow logs
        * API gateway
        * Cloudtrail
        * Route53 - log DNS queries
* Log groups
    * give it any name you want that usually represents an application
* Log stream
    * inside a log group
    * Subdivide a log group up, different log files for example
* Can define log expiration policies(never expire, 30 days, etc.)
* can encrypt CW logs with KMS
* Can further send logs to other destination:
    * S3
    * Kinesis data stream, firehose
    * Lambda
    * Elastic Search via Lambda


* metric filters
    * can monitor the logs and when a condition occurs will increment the metric filter
    * essentially creates another metric datapoint
    * for example
        * find how many times a specific IP has occured
        * count the count of the occurence of the word ERROR 
    * can be used to trigger CW alarms

* Cloudwatch logs insight
    * can query logs in real time
    * can add queries to a CW dashboard

