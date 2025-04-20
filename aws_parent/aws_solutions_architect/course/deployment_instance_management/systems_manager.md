* get operational insights about the state of your infrastructure
* helps manage EC2 and on-prem instances
* Easily detect problems
* patch automation at scale
* integrated with cloudwatch metric/dashboard
* integrated with AWS config
* totally FREE

* need to install the SSM agent on the systems we control
    * by default installed on AWS made and some Ubuntu AMI's
    * need to make sure the SSM agent has proper IAM permissions to register with system 
    * if on prem - make sure the access keys are correct for the agent to connect to systems manager


### Functionality

* run a command across multiple instances
    * define resource groups to group instances
    * rate control / error control to define how fast to run this command across instances and what to do with any that error
    * fully integrated with cloudtrail and IAM
    * no need for SSH, the agent takes care of it
    * results are shown in the SSM console

* session manager
    * can get a console on a host
    * different than SSH, does not need any SSH configurations or keys
    * access via aws cli, SDK, aws console
    * can send the session info to logs
    * can configure a hook to send startSession events to cloudtrail to tell when someone has started an SSM session


* patch manager
    * define a patch baseline, patch groups(i.e. dev, test, etc)
    * maintenance windows
    * monitor patch compliance using SSM inventory
    * define rate control ( errors  and concurrency ) 

* OpsCenter
    * differs' from SSM ops center in that Health dashboard gives you all the issues that AWS is experiencing
        * whereas AWS SSM ops center gives you all the issues happning in your environment
    * logs, alarms, config info, stack info
    * By default — OpsCenter won’t show anything unless something creates an OpsItem.
    * It’s not automatic for all issues. You need to configure sources or rules that send issues to OpsCenter. 
    * ex: cloudwatch alarm for high cpu -> eventbridge -> eventbridge rule will send to opscenter
    * can define a runbook for fixing those issues
        * runbook is a series of automations that run to possibly fix an issue
    