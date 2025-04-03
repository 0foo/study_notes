* applications deploy to many EC2 instances
* go from one version to another version
* (not managed by elastic beanstalk)
* can deploy to EC2, ASG, ECS, Lambda


### EC2
* define how to deploy with an appspec.yml + deployment strategy
* does in place updates i.e. doesn't create new instances
* can define hooks to verify the deployment is working great after each deployment phase
    * 


### ASG
* in place updates: updates current existing EC2 instances in ASG
* new ASG created instances will automatically have the new version
* blue/green: new autoscaling group created, settings copied, and instances copied from one instance to another
    * can choose how long to keep the old instances
*   * ASG will be serving to both version while transitioning
    * At some point will remove the old versions if everything is working wlel


### Deployment strategies
* half at a time (will take half down, upgrade, then go live, then do other half)
