* fully managed service you can use with no infrastructure knowledge needed
* scalable
* start with source code or a docker image
* you configure settings like:  
    * cpu, memory, enable autoscaling?, health check, load balancing
* can provide access to VPC which means can access all AWS resources(database, cache, message quueue)
* it automatically builds/deploys webapp
* you can access it using a url

#### Architecture
* upload docker image to ECR
    * have ECR replication cross region
* have a dynamo DB
    * have dynamo globally replicated across regions

* use an app runner service in more regions and it now has access to both ECR and Dynamo 

* can use route53 for DNS load balancer and set it to direct to an endpoint based on which has the least latency.