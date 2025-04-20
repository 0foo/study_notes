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