* multiple VPC's to one customer site (on CGW)
    1. AWS transit gateway
    2. Each vpc has it's own VGW and it connects to the single CGW
    3. VPC peering/private link
        * one hub VPC with all the others peered to it
        * can route VPN traffic to a single peered VPC

* multiple customers sites to one VPC
    1. AWS Transit gateway
    2. VPG can take multiple VPN connections(up to 10 by default)
        * does not support transitive routing, so customer sites cannot communicate with each other directly.
    

* Shared services VPC
    * can proxy or replicate all data/services from one site into a central VPC 
    * other VPC's can hub and spoke to this VPC and access all the stuff in this BUT can't access transitive services one hop over
    * this works for corporate on prem or cloud VPC's

* work around VPC non-transitivity when VPC peering
    * proxy services at the instance level from an accessible VPC to non-accessible
    * transit gateway 


### Lambda
* Serverless thumbnail creation
    1. New image in S3
    2. Trigger Lambda
         * create a thumbnail
         * push the new thumbnail to s3
         * push the metadata to DynamoDB
    
* Serverless Cron job
    1. Event bridge to create a time based trigger
    2. Triggers AWS lambda

* Whats the difference:
    * s3 -> SNS -> lambda
    * s3 -> SNS -> SQS -> lambda

#### AWS Network firewall

* set up an "inspection VPC" that has network firewall enabled that all traffic goes through
    *  how to do with: multiple VPCs, direct connect, VPN, internet, etc?
    * HUB and Spoke model around a TGW with routing tables all configured to send all traffic through inspection VPC
    * will have to use TRANSIT GATWEWAY to direct all traffic from all sources to go through inspection VPC first
    then BACK to transit gate way to go to the VPC with the IGW
    
