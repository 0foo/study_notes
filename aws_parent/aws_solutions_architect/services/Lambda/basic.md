* main integration
    * API gateway
    * Kenesis
    * DunamoDB 
    * S3 
    * IoR
    * Event Bridge
    * Cloudwatch logs
    * SNS
    * Cognito
    * SQS

* Serverless thumbnail creation
    1. New image in S3
    2. Trigger Lambda
         * create a thumbnail
         * push the new thumbnail to s3
         * push the metadata to DynamoDB
    
* Serverless Cron job
    1. Event bridge to create a time based trigger
    2. Triggers AWS lambda

* Languages(don't need to know)
    * node
    * pythong
    * java
    * C#
    * ruby
    * custom runtime API(rust/golang)


* Use container image on lambda
    * max image size is 10GB
    * container image must implement lambda runtime API
    * prefer to use ECS or Fargate instead of Lambda for containers

* Resources
    * 128Megs to 10Gigs of RAM
    * CPU is linked to RAM (cant be set)
        * example: 2vcpus allocated at 1,769 MB of RAM
        * 6vcpu's allocated @ 10Gig
* Timeout 
    * max amount of time lambda can run before AWS stops its execution
    * can run up to 15 minutes

* /tmp storage 
    * 10,248 MB

* Deployment package limits
    * 50 MB zipped
    * 250MB unzipped

* concurrency
    * up to 1000 concurrent executions by ALL SERVICES(soft limit can be increase by AWS team)
    * anything trying to use Lambda past this will be throttled
    * A workaround is to send requests to SQS and let lambda process them if tolerant to async
    * Reserved Concurrency: can set a reserved concurrency for a specific lambda
        * allocate a specific number of concurrent execution slots exclusively for a particular Lambda function. 
        * If a function exceeds its reserved concurrency, additional requests are throttled, returning a ThrottlingException.
        * A function has its slots available to it but CANT EXCEED THEM even if slots are available

    * Provisioned Concurrency: Keeps a specified number of execution environments initialized and ready to serve requests with low latency.

* Lambda async/sync
    * Synchronous Lambda
        * Immediate response from the Lambda
        * API gateway for example
        * larger payload sizes because the client manages the full lifecycle of the request and response.
        * Errors handled client side(retrys, backoff, etc)

    * Async Lambda
        * AWS handles the queuing internally
        * Used for event driven architecture
        * no immediate reponse
        * Smaller payload sizes
        * can define dead letter queue for if the async event fails and then fails the set number of retrys also
        * uses: event driven events, any sort of job: s3 thumbnail creation, SNS event, etc.


* Invokation/Output Payload max size
    * 6MB when synchronous
    * 256KB when asynchronous
    * Workarounds for Large Payloads
        * If you need to process payloads larger than these limits:
        1. Use Amazon S3
            * Store the large payload in an S3 bucket and pass the S3 object key or a pre-signed URL to the Lambda function.
            * This approach works for both synchronous and asynchronous invocations.
        2. Use Amazon SQS
            * For asynchronous workflows, split the payload into smaller chunks (if possible) and send each chunk as a separate SQS message.
        3. Use API Gateway or Step Functions
            * Combine Lambda with API Gateway or AWS Step Functions for orchestrating large workflows where payloads can be handled in multiple steps.

* Lambda and Code Deploy
    * integrated with the SAM framework
    * can help automate traffic shift for Lambda aliases 
        * gradually shift traffic from a v1 endpoint to a v2 by a percentage amounts
    *  Strategies:
        * Linear: linear increase by X amount in Y minutes
        * Canary: X amount over Y time frame then all in
        * AllAtOnce
    * Can run pre/post traffic hooks to check the health of a Lambda function so wont move traffic if Lambda unhealthy

* Logging/Monitoring/Tracing
    * AWS execution logs/metrics are in Cloudwatch
    * ensure AWS Lambda role has IAM policy to allow write to Cloudwatch

* X-Ray
    * Its possible to trace Lambda with X-Ray
    * Enable it in the Lambda configuration(will run the X Ray daemon for you)
    * If need XRay instrumentation in CODE: Use AWS SDK 
    * Ensure Lamda has IAM access to XRay
    * Note: Xray can trace all kinds of stuff including a request flow through AWS, database performance, etc.
    



#### Lambda in a VPC
* by default Lambda not deployed in a VPC, deployed to the AWS cloud at large
* Can't connect to internal VPC stuff
* Note: by default lambda in a VPC will not have internet access
* If deploy lambda in a private VPC, can connect InternetGW/NAT gateway in public subnet to reach/be accessible by internet
    * this will also allow access to some out of VPC AWS public services
* Could also create VPC endpoint for Lambda to reach out of VPC AWS services 
* If lambda deployed in public cloud, will get a random public AWS IP
* If deployed in private VPC NAT will take care of this with its Public IP



#### architectures

* Whats the difference:
    * s3 -> SNS -> lambda
    * s3 -> SNS -> SQS -> lambda