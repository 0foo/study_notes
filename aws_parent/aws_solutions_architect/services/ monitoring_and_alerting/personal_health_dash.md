* bell icon in the nav bar at the top
* will tell you all of the AWS internal issues going on as well as others you define
* Global service
* Show how outages happen in AWS
* Show impact on resources
* List issues/actions you can do to remediate them


* will show you all the maintenance events from AWS
    * keyword to look for in the exam

* can access all this info programatically via AWS Health API

* if have enabled AWS organizations -> can aggregate all these health events in one place


### Health Event Notifications
* can use event bridge or cloudwatch to react to changes for AWS health events in your AWS account
* AWS personal health will trigger an event which will be sent to even bridge or cloudwatch which will invoke some other service( SNS, lambda, kinesis, etc) 
* Use cases: notification, logging, trigger corrective actions
* can't be used to return public events from the even dashboard(??? look more into) 
* Example: Want to recieve email notification when EC2 instances are scheduled for updates


### GUI
* in website AWS console will have a list of all infrastructure related events both by you and AWS itself
* 