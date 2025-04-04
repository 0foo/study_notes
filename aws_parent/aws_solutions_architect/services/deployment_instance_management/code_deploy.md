* applications deploy to many EC2 instances
* go from one version to another version
* (not managed by elastic beanstalk)
* can deploy to EC2, ASG, ECS, Lambda

* half at a time deployment
    * take half of existing instances down(or some proportion)
    * upgrade them
    * bring them back up 
    * bring the other half down
    * upgrade
    * bring back up
    * IN PLACE UPDATES


* blue/green or canary: 
    * essentially create new environment, test it, then switch traffic to it
    * if traffic switched all at once is blue/green, if trickle is a canary



### EC2
* define how to deploy with an file named: appspec.yml + deployment strategy(i.e. cnary? blue/green, how fast/gradual? etc)
* appspec.yaml
* does in place updates i.e. doesn't create new instances
* can define hooks to verify the deployment is working great after each deployment phase
* can use half at a timeIt  theanswers question:




### code deploy to ASG
* one of two ways:
    * in place updates: 
        * updates current existing EC2 instances in ASG (see half at time deployment)
    * blue/green:
        * new autoscaling group created, settings copied, and instances copied from one instance to another
        * new ASG created via launch template
        * can choose how long to keep the old instances
        * ASG will be serving to both version while transitioning
        * At some point will remove the old versions if everything is working well


### Lambda
* creates a new lambda and then 
* essentially blue/green with a lambda alias that will allow traffic shifting to the v2 lambda 
* allowed to run a pre and post deploy lambda(will need to define these)
* can monitor deploy with cloudwatch metric and setup an alarm to trigger a rollback
* can roll back with cloudwatch alarms, set it up to monitor some metrics to test to see if working if not rollbacks
* if both the pre/post hook lambda pass the deploy is successful
* easy and automated rollbacks with cloudwatch alarm
* SAM framework natively does code deployment


### ECS / Fargate
* write a new task i.e. next version of the task
* the tasks are sent traffic by the ALB
* traffic shifting will happen from old task to new in either blue/green or canary fashion
* once new task is validated the old task will be deleted

* can code deploy to ECS with blue/green deploys or canary deploys
* setup is done withing ECS service NOT code deploy
* new task set is created and traffic routed there
* if everything stable for some pre-defined minutes then the old task set is terminated
* architecture: ALB -> ECS service which uses ECS task to launch ECS tasks



### Deployment strategies
* half at a time (will take half down, upgrade, then go live, then do other half)
