* multiple VPC's to one customer site (on CGW)
    1. AWS transit gateway
    2. Each vpc has it's own VGW and it connects to the single CGW
    3. VPC peering/private link
        * one hub VPC with all the others peered to it
        * can route VPN traffic to a single peered VPC

* multiple customers sites to one VPC
    1. AWS Transit gateway
    2. VPG can take multiple VPN connections(up to 10 by default)
        * does not support transitive routing, so customer sites cannot communicate with each other directly.
    

* Shared services VPC
    * can proxy or replicate all data/services from one site into a central VPC 
    * other VPC's can hub and spoke to this VPC and access all the stuff in this BUT can't access transitive services one hop over
    * this works for corporate on prem or cloud VPC's

* work around VPC non-transitivity when VPC peering
    * proxy services at the instance level from an accessible VPC to non-accessible
    * transit gateway 


### Lambda
* Serverless thumbnail creation
    1. New image in S3
    2. Trigger Lambda
         * create a thumbnail
         * push the new thumbnail to s3
         * push the metadata to DynamoDB
    
* Serverless Cron job
    1. Event bridge to create a time based trigger
    2. Triggers AWS lambda

* Whats the difference:
    * s3 -> SNS -> lambda
    * s3 -> SNS -> SQS -> lambda

#### AWS Network firewall

* set up an "inspection VPC" that has network firewall enabled that all traffic goes through
    *  how to do with: multiple VPCs, direct connect, VPN, internet, etc?
    * HUB and Spoke model around a TGW with routing tables all configured to send all traffic through inspection VPC
    * will have to use TRANSIT GATWEWAY to direct all traffic from all sources to go through inspection VPC first
    then BACK to transit gate way to go to the VPC with the IGW
    


#### Web Layer/Application layer architecture
* Note: all of these can have Route53 integrated to get DNS

* EC2 on its own with Elastic IP
    * can have a failover standby instance
    * elactic IP can move to back up instance in case of primary failover
    * client see same elastic IP and never sees change

* EC2 with Route53
    * a bunch of EC2 instances with DNS based load balancing to each one
    * DNS returns one or numerous IP's based on configuration
    * If more than one is returned client will select one randomly
    * Can add new EC2 instances and add them to the hosted zone in DNS
    * downside: 
        * if a host goes down, a client will not be able to get a new DNS until TTL expires
        * also if add a new instance will take some time until TTL expires for it to get traffic

* ALB + ASG
    * client gets DNS from route 53 then sends request to ALB attached to an ASG
    * ALB: health checks, multi AZ
    * ASG: scaling
    * very classic 
    * new instances added right away because they register with ALB
    * during autoscaling it's slow because have to build the new EC2 instances: 
        * startup + userdata script
        * use AMI to help but still not much
        * on the order of minutes
    * can do cross zone load balancing
    * ALB elastic but can't handle huge peak of demand: pre-warm to fix this
    * can use cloudwatch to trigger autoscaling based on resource utilization
        * tip: good target utilization should be between 40% - 70%


* ALB + ECS on EC2
    * same as ALB + ASG but also has containers on top of the EC2 instances
    * ALB will use port mapping so can run the same containers on an instance to maximize usage of an instance
    * this has two layers of autoscaling
        1. the instances that host the containers
        2. the containers/tasks
    * pain in the but to orchestrate both ECS autoscaling and ASG autoscaling
        * will need multiple layers of ruls

* ALB + ECS on Fargate
    * AWS handles the EC2 layers i.e. application tier
        * we don't manage the autoscaling group for EC2
        * A load balancer still exists, it's just managed by AWS and we don't use it at all
    * only manage the container autoscaling based on certain resource utilization
    * the autoscaling if relatively fast (30 second or so) as it just spins up docker container

* ALB + Lambda(or other AWS services)
    * can connect ALB directly to a number of AWS services 
    * ALB can use lambda as a target
    * seamless scaling thanks to lambda runtime 
        * keep in mind lambda time and max limits
    * cost savings 10X or more from using API gateway
    * note: this has lambda cold starts up to a second when autoscaling (but still faster than any other method of autoscaling)

* API Gateway + Lambda
    * can connect API Gateway directly to AWS Lambda
    * Get all the great benefits of AWS GW plus seamless autoscaling with Lambda
    * autoscaling basically instant
    * limits:
        * 10,000/second API GW
        * 1000 concurrent Lambda 
        * 10MB mas payload API GW
        * both soft limits that can be increaed by AWS support
    * note: this has lambda cold starts up to a second when autoscaling (but still faster than any other method of autoscaling)


* API Gateway connected directly to an AWS Service
    * instead of going through a lambda have the API GW integrate directly with the service
    * remember API gateway limit 10 MB

* API Gateway + HTTP backend (ex: ALB)
    * connect API GW To ALB, on-prem, EC2, some other HTTP host
    * can use HTTP integrations inside API GW if needed
