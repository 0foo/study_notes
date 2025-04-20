* idea: a developer centric view of deploying an application on AWS cloud
* wrapper around all native AWS components(EC2, RDS, ASG, etc)
* one view that's easy to make sense of

* free to use beanstalk, but pay for underlying resources

* Beanstalk supports numerous runtime languages: java, golang, php, node, etc.

* can also use docker with beanstalk 
* if you can dockerize your application, then you can migrate it to elastic beanstalk

* great to replatform your appliation from on prem to cloud


* managed service: instance configuration/ OS config handled by Beanstalk
* deployment strategy is configurable but handled by beanstalk, so can have different rollout strategies
* develoer is just responsible for the application code 

### three architecture models
    * Devlopment: single instance w/ elastic IP
    * High Avilability: LB + ASG + Multi-AZ (standard stuff)
        * web tier: ALB, ASG, EC2
    * Worker envi: data -> web tier -> SQS -> Auto Scaling Group( can adapt to SQS size)
        * useful for long running tasks and/or resource intensive that can take a while to complete
        * anytime hear 'decoupling' think SQS
        * ex: processing video, generating zip file, etc.
        * can configure them to be periodic as well


* blue/green deployment
    * create a new stage environment and deploy the new version there
    * route 53 to use weighted routing to slowing increase traffic
    * can use the "swap URL" which will just swap all traffic from one to another
    * from blue to green
    * can either do gradual(canary) or full
