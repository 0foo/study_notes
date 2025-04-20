* dynamic scaling policies
    1. target tracking scaling
        * simplest
        * take metrics 
        * if above the increase metric will add instances 
        * if beneath the reduced metric remove instances

        * simple/step scaling
            * example: when cloudwatch alarm triggered add 2 units

        * scheduled scaling
            * anticipate based on known usage patterns

        * predictive scaling
            * AWS will analyze your historical load and generate a forecast based on that
            * AWS will then setup scaling and adctions to predict the right anoubt of resources to sustain that load
            * good if you have patterns in load
        
* Good metrics to scale on
    * CPUUtilization: average CPU
    * RequestCountPerTarget: to ensure the network requests spread out to all the ASG instances are stable and no instance overloaded 
    * Average network In/Out: 
        * if applcation is network bound
        * ex: a video uploader
        
* Other autoscaling info
    * spot fleets (mix of spot and on demand instances)
    * lifecycle hooks:
        * allows perform actions at stages of instance lifecycle
            * ex: before instance terminated or when it starts
        * ex: clean up logs, log extraction, special health checks
    * to upgrade an AMI
        1. must update the launch/configuration template of the ASG
        2. 
            * must terminate instances manually(cloudformation can help)  OR
            * use EC2 instance refresh for auto-scaling to terminate instance for you 
                * the new ones come up and have the new AMI setting in the ASG template
    * autoscaling: instance refresh
        * if you update ASG launch template
        * specifiy minimum perctange healthy of instances
        * the ASG will automatically ternminate percentage and bring up new ones with the new launch template settings
        * continue this until all instances replaced by new ones 
        * can specify warm up time until instance is considered ready to use (to ensure bring up services)

* all the processes in the autoscaling group
    * Launch: add new EC2 to the group, increasing capacity
    * Terminate: removes EC2 instance ,decreasing capacity
    * HealthCheck: checks health of instance
    * ReplaceUnhealthy: terminate/recreate unhealthy instances
    * AZRebalance: balance number of instances across AZ's
    * AlarmNotification: accepts notifications from Cloudwatch
    * ScheduledAction: perform scheduled actions you create
    * AddToLoadBalancer: add instances to LB or target group
    * InstanceRefresh: performs a phased kill and recreate all instances in the ASG

* Health checks
    * ec2 status checks
    * ELB health check (http based): the ELB will consistently check the instance
    * if instance is deemed unhealthy based on the status checks
        * AWS will terminate and the launch new one to replace
    * make sure the health check is simple and correctly checks the HEALTH of the instance
    * a good check is an http endpoint called /health-check or something like that
    * a bad check is checking a route that does something heavy i.e. reach out to database for example
        * this could take a long time or the database could fail
        * would give a false alert that EC2 has failed 


#### Auto Scaling Update Strategies
* how to update an application in an autoscaling group
* there's different architectures possible

* background info
    * A target group is what a LB distributes traffic to
    * An target group is associated with an ASG so that each instance an ASG creates is registered to a target group
    * A launch template is used by ASG's to specify the new instance details
    * A single ASG is only allowed to use a single target group(associated with the ASG not the launch template)
    * A single ASG can use multiple launch templates

* architecture:  LB -> ASG -> Launch Template -> Target Group

* different architectures possible to do this: 

1. single ASG, multiple launch templates
    * will spin up different versions in the same target group
    * both versions will be live and recieving traffic at the same time
    * old versioned instances gradually shut down as new versioned instances spin up
    * LB does not know about instance details only target groups, so can't differentiate to send different percentages of traffic
    * this is called a rolling deployment

2. two ASG each with a different launch template and target group
    * LB can differentiate between target groups and can adjust traffic
    * each ASG can have a different version in the launch template
    * allows for a Canary deployment(gradual increasing  % of traffic between versions), or Blue/Green(switch versions all at once but retain old one as backup)


3. Multiple ALBs each with their own ASG's and target groups
    * basically entire environment replicated including the load balancer
    * the client would need to have traffic switching done at the DNS level
        * use CNAME and and can have 'weighted record' to allow weighted traffic rollout
        * note: relys on clients to have sane DNS settings to split traffic
        * pros: can test the full architecture with the new version 
