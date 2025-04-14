* FLINK CANNOT READ FROM FIREHOSE!!!!
* FIREHOSE CAN READ FROM FLINK!!!

* CANNOT SEND DATA DIRECTLY TO S3 FROM KINESIS STREAMS!!!
    * must go through firehose


* Dynamo streams can function as a real time data pipeline the same as Kinesis Streams BUT 50X more EXPENSIVE


* Architecture
1. s3 trigger event bridge  
2. event bridge trigger AWS batch
3. batch job invoked (fargate/docker, ec2, spot instance)
4. fargate/docker will pull image from ECR and instantiate containers
5. batch jobs may need to retrieve data from s3 for the job 
6. can send the final product to s3 and maybe insert metadata into dynamo




#### Ways to run jobs
1. provision EC2 and use cron
2.  * not highly available, scalable
    * never use

* amazon event bridge and lambda
    * serverless
    * periodic lambda
    * has lamabda limitations

* have reactive workflow to invoke actions when something happens
    * event bridge, s3, api gateway, sqs, etc, etc

* use aws batch
    * none of the limitations of lambda
    * doens't have built in periodicity
    * can integrate with event bridge to trigger a batch job
    * event bridge has time based events


* use fargate
    * more barebones than batch


* use EMR 
    * better for long running or big data workloads
