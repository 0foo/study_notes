### VPC flow logs
* capture traffic info

* can monitor:
    * vpc 
    * subnet 
    * ENI 
    * anything that can be an AWS managed interface(ENI)
        * ELB, RDS, NATGW, etc. etc.

* traffic can go into S3, cloudwatch, kinesis
* can query with Athena on S3 or cloudwatch insights

* examples of monitoring:
    * success or rejection of traffic by a security group or NAC
    * analytics of usage behavior, malicious behavior, port scanning etc


* can send flow logs to cloudwatch log service
    * output flow logs to cloudwatch and analyze with:
        * cloudwatch contributor insights: 
            * can do data analysis i.e. top 10 interfaces pulling the most network
            
        * cloudwatch metric filter that will go off when logs hit some mettic
            * then send to CW alarm -> SNS
            * i.e. if too much ssh or somethingg
    * output flow logs to S3 bucket then analyze with Amazon Athena 