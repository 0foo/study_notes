* serverless managed queue, no need to provision anything
* extreme scale

* used to decouple services
* max message size 256KB
* if need larger size, upload the larger file to s3, then add a pointer in the SQS message that consumer can read

#### Consumer
* EC2 with autoscale
* Lambda
* use as write buffer to dynamo db
    * may have write provisioned to a certain amount in dynamo
    * so can buffer in SQS and only feed to dynamo at certain speed
    * avoids dynamo throttle 


#### Type
* FIFO - 
    * processed in order recieved
    * Limited Scale: 300 message/s with no batching, 3000 messages/s with batching
* 


#### Deadletter Queue
* if consumer fails to process a message
    * message goes back into the queue
    * maintains a fail count
    * when hits a certain number of fails(threshold), will send to Dead Letter Queue
* DLQ: useful for debugging
* DLQ of a FIFO queue must also be a FIFO queue
* DLQ of standard queue must also be a standard queue
* DLQ has retention time, so can set a time to retain DLQ messages at which point they are lost
    * good to set this to longer times

* redrive to source
    * after inspecting a DLQ message and figuring out and fixing what's wrong
    * can redrive the DLQ message back to it's original source (native feature in SQS no additional code needed)

#### Idempotency
* messages can be processed twice by consumers
* need to make sure that consumers won't duplicate the effect if process additional time
* the responsibility of ensuring messages aren't duplicated falls on CONSUMER as SQS may duplicate messages
* consumers can do a hash of a part of the data and upsert into db with hash as key
    * that way will update the data if it's a duplicate


#### Event source mapping
* Event Source Mapping in the context of Amazon SQS refers to the process by which AWS services, such as AWS Lambda, automatically poll and consume messages from an SQS queue without requiring you to write or manage the polling logic yourself.
* Messages from the SQS queue are batched and sent to the configured Lambda function for processing.
* Lambda scales automatically with the rate of incoming messages in the queue.
* The number of concurrent Lambda invocations adjusts based on the batch size and the processing rate of the function.
    * define a batch size and lambda will pull that many from the queue
    * if theres more than that batch size in the queue more lambdas will be created to handle them
* queue visibility timeout should be 6x the timeout of your lambda function(reccomended via aws docs)
    * maybe explain this more with GPT
* DLQ is possible


#### Architecture ideas
* can separate clien and server by a request queue and a response queue
    * completely decouples, fault tolerance, load balancing