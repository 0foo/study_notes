* run batch jobs as docker images
* two ways:
    1. run on fargate, serverless
    2. dynamic provisioning of the instance in your VPC

* optimal quantity and type based on volume and requirements
* no need to manage clusters/ fully serverless
* batch processes of images running thousands of concurrent jobs
* Schedule batch jobs using Amazon Eventbridge
* orchestrate using AWS Step functions


* Architecture
1. s3 trigger event bridge  
2. event bridge trigger AWS batch
3. batch job invoked (fargate/docker, ec2, spot instance)
4. fargate/docker will pull image from ECR and instantiate containers
5. batch jobs may need to retrieve data from s3 for the job 
6. can send the final product to s3 and maybe insert metadata into dynamo



#### Batch vs Lambda
* Lambda
    * time limit
    * space limit
    * limit on what runtimes can use

* batch
    * no time limit
    * any runtime as long as packaged in a docker image
    * rely on EBS/instance store for disk space
    * relies on EC2 or AWS Fargate

#### Managed batch environment
* AWS manages capacity and instance types
* can choose on demand or spot
* set max price for spot
* all the instances launced within own VPC
    * needs access to ECS
    * will need a NAT gateway or NAT instance  or using VPC endpoint for ECS
* set min/max vCPU
    * note this will launch all different types of spot instances as they're available
    * all that matters is the vCPU
* can setup autoscaling to expand/contract spot instance count in response to increase/decrease in jobs


#### Batch job queue 
* how batch jobs distribute jobs to instances
* send job to job queue in a number of ways
    * SDK
    * Lambda
    * Clouwatch events
    * Step function
    * etc.


#### Multinode mode
* Most important:
    * does not work with spot instances
    * works better if EC2 launch mode is in a placement group "cluster" to get the enhanced networkgin
        * means everything is on same rack within same AZ
* Other:
    * good for HPC
    * leverage multiple EC2/ECS instances at the same time to run your job
    * you specify how many
    * good for when you have tightly coupled workloads
    * 1 main node and many child nodes
    * main node will launch and then launch/manage other nodes
    * all nodes run the job, then shutdown


#### Unmanaged batch environment
* you control and manage instance config, provisioning, and scaling
