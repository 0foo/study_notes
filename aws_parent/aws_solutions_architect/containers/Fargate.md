* No EC2 foundation management at all
* considered "serverless"
* Fargate manages underlying infrastructure
* submit tasks to fargate and these are created automatically without you having to think about underlying infra.

* you just create task definitions
    * specify how much CPU/RAM you need

* to scale, just increase number of tasks or enable autoscaling
* default networking mode is awsVpc

* can use spot instances for cost savings at reliability tradeoff