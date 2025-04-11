* SUPER IMPORTANT



* Disaster is any event that has negative impact on companies buisness continuity or finances
* DR is about preparing/recovering from disaster

* what kinds of DR are available?
    * on premise-traditional, very expensive
    * hybrid -> on premise using cloud recovery with hybrid recovery
    * cloud -> AWS region to different AWS region

* RPO - recovery point objective
    * how often you run backups
    * time between RPO and disaster is a data loss

* RTO - recovery time objective
    * when you recover from your disaster how much downtime between disaster and recovery
    * essentially downtime


* want RPO and RTO to be as small as possible
* as you reduce RPO and RTO you increase cost


* listed in order from slower to faster RTO and lower to higher cost
    * Backup and Restore
    * Pilot light
    * Warm standby
    * Hot site / multi site approach




* backup/restore
    * manually sending data to a data store that then needs to be recovered
    * objects -> s3 via storage gateway or snowball -> s3 -> lifecycle policy -> glacier
        * snowball RPO is on the order of days as it has to be mailed
    * databases, redshift, RDS, EBS -> snapshots
        * RPO based on snapshot frequency
    * application instance -> create AMIs 
    * all of this is cheap
    * takes a long time to recover 
    * high RPO high RTO

* pilot light
    * a small version of the app is running in the cloud or the data is highly available so can quickly spin up instances 
    * can point route53 at the new system
    * critical core 
    * same as backup and restore except already have core systems running
    * more expensive because have instances and data stores constantly running

* warm standby
    * full system up and running but at minimum size 
    * needs scaling to production load on disaster
    * for example: have minimum capacity ASG ready to scale and an RDS replica with route 53 ready to failover

* multi site
    * multiple production scale running
    * Note: will be using both of the sites at all times
    * can be on prem, cloud, or hybrid with multi sites being one any of these 

* all cloud
    * this is the same kind of architecture as multi site except without any on prem
    * there are additional improvements 
        * Aurora global database



*### general 

 backup resources
    * snapshots: EBS, RDS
    * regular pushes to s3, lifecycle policies, glacier, cross region replication
    * from on prem to cloud->snowball or storage gateway
* high availability
    * route53 to route traffic between sites/regions
    * multi-AZ services, i.e. RDS, elasticache, efs, s3, aurora global
    * site to site VPN as a recovery for failure of direct connect service
* replication
    * RDS, Aurora global
    * database replication from on prem to AWS RDS
    * storage gateway
* automation
    * cloudformation / Beanstalk can create entire new environment in the cloud
    * recover reboot instances in EC2 if cloudwatch alarms fail
    * aws lambda for customized automation
* chaos testing
    * how to know if solution will work?
    * introduce chaos
    * netflix - has a program called 'simian army' randomly terminating EC2 instances
    * introduce chaos to ensure infrastructure is capable of surviving failures