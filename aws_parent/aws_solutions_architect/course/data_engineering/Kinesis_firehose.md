* Designed for data delivery to storage or analytics destinations (S3, Redshift, etc.).


#### Main benefits
* you upload data to firehose and get these benefits
    * automatic scaling!!!
    * buffering(i.e. for saving money on writes to s3)
    * can add custom transformation logic with lambda
    * data compression/encryption(can configure Firehose to compress data (e.g., GZIP, Snappy) and encrypt it )
    * error handling/retry mechanisms (Firehose retries failed data deliveries and supports logging errors for troubleshooting.)
    * encrypted at rest and in transit

#### Flow of KDF
1. Sources:
    * Kinesis data streams - MOST COMMON
    * Amazon cloudwatch
    * AWS IoT
    * clients directly
    * other AWS services

2. transform data optional
    * has some automatic transformations
    * can use lambda to do custom transforms to the data
    * there's several blueprint lambda templates
        * example: json to csv or compress of data
    * Firehose supports data compression (e.g., GZIP, Snappy) to save storage costs
    * firehose supports many data formats, conversions, transformation,compression
    * Lambda is invoked for every batch of data sent by Firehose to the function for transformation.
    * Invocation cost: $0.20 per million invocations.
    * Frequent invocations (due to small Firehose buffer sizes) can increase costs.
    * want a large buffer to use one lambda
    * Note this can get expensive

    * if have high throughput, the size buffer will be reached

3. data is buffered if enabled
    * has size and time buffers that can be specified
    * can disable buffering
    * can allow buffer to autoscale as well
    * Firehose buffers incoming data before delivering it, reducing the number of writes to the destination and improving efficiency.
    * adjustable buffer interval from 0 to 900 seconds 
    * also has a few second constant delivery time interval
    * useful for example with s3: this reduces the number of PUT requests to S3, lowering S3 costs.
    * time and size
        * when buffer size is reached, it's flushed and sent to deis
        * If after set time even if buffer is not full, it will flush
            * minium time: is 1 minute
    * firehose can automatically scale the buffer size if have high throughput
    * if have low throughput the buffer time limit will reached


4. destinations
    * can send to multiple destinations
    * 3 types of destination:
        * AWS destination  REMEMBER THESE VERY IMPORTANT FOR TEST
            * S3
            * redshift(copies to s3 first! very important! then KDF issues a copy command to copy from s3 to redshift)
            * opensearch
            * splunk
            * lambda (as transformation NOT final endpoint)
            * API Gateway via POST calls, which then call a lambda
                * Set Firehose’s destination to HTTP endpoint.
                * Create an API Gateway + Lambda combo to accept incoming POSTs from Firehose.
                * In your Lambda, write data to Timestream or any other custom destination.

        * 3rd party (splunk, datadog, mongo etc)
        * custom HTTP api 
    * can deliver to one or more destination 
    * NOTE: Sparc and KCL CANNOT read from FIREHOSE, ONLY kinesis data stream
    


5. post processing
    * after data sent to destinations can also output the source records to s3 as a backup
    * can have a sort of DLQ by sending data that was failed to write to a s3 bucket

#### Capacity planning
* NONE! 
* automatic scaling


#### Price
* pay only for data going through firehose

 


#### When to use streams vs firehose
* streams
    * Designed for real-time DATA STREAMING.
    * More suitable for applications that need real-time, event-driven processing.
    * Provides more flexibility for complex or real-time transformations.
    * data processed in real time (under 200ms)!!!
    * Requires you to write and deploy producers/consumers to move data to storage or analytics systems.
    * data stays in system from 1 to 365 days and is immutable
    * Multiple consumers can consume the data(different from SQS which one consumer removes post from queue)
    * manage scaling yourself: shard splitting merging(autoscale exsist now)
    * pay by provisioned capacity!!
    * support replay capability


* firehose
    * Designed for DATA DELIVERY to storage or analytics destinations (S3, Redshift, etc.).
    * Ideal for low-maintenance, near-real-time data pipelines.
    * load streaming data into (S3/Redshift/Opensearch)/3rd Party/custom HTTP
    * near real time!!
    * fully managed
    * automated scaling!
    * pay by usage!!!
    * no data storage
    * can send to multiple destinations
    * buffering(i.e. for saving money on writes to s3) 
    * can add custom transformation logic with lambda
    * automatic scaling
    * data compression/encryption(can configure Firehose to compress data (e.g., GZIP, Snappy) and encrypt it )
    * error handling/retry mechanisms (Firehose retries failed data deliveries and supports logging errors for troubleshooting.)


#### Why?
* Firehose automatically delivers streaming data to the specified destination without requiring you to manage and scale the infrastructure for data ingestion.
* Supports destinations like Amazon S3, Amazon Redshift, Amazon OpenSearch Service (formerly Elasticsearch), and third-party services like Splunk.
* Without Firehose, you would need to write, deploy, and maintain custom ingestion and delivery code. Firehose abstracts this for you.
* Firehose scales automatically to handle incoming data volume, eliminating the need to manually provision resources.
* It can handle gigabytes per second of input data, making it suitable for high-throughput use cases.
* Firehose can invoke an AWS Lambda function to transform or enrich data before delivering it to the destination.
    * Example: Format raw JSON logs into a structured CSV format for storage in Amazon S3 or Redshift.

