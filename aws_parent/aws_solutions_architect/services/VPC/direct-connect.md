* DEDICATED LINE between your Data Center and AWS
* traffic does not travel over public internet
* traffic does not go through ISP, so no payment to an ISP
* NOT redundant so will need setup to a second connection or VPN
* Connect to a single region!!!

#### VIF
* virtual interface
* public VIF - connect to public AWS endpoints like s3, EC2
* private VIF - connect to private resources inside of VPC
    * EC2
    * VPC interface endpoints 
    
* transit VIF - when using a Transit Gateway 


customer site -> direct connect hub -> virtual private gateway attached to the direct connect hub->vpc

* direct connect hub is structure located somewhere.
* public and private VIF's go from customer site to AWS


#### connection types
1. 
* A Dedicated Connection is a physical connection between your on-premises network and an AWS Direct Connect location.
* It is provisioned directly by AWS.
* Ownership: You own and manage the physical connection.
* dedicated non-scalable bandwidth requires upgrade for more


2. 
* A Hosted Connection is provisioned by an AWS Partner who owns the physical Direct Connect infrastructure.
* The partner provides logical connectivity to your organization.
* The AWS Partner provisions the connection, making it simpler to set up.
* You do not need to deal with physical cabling or colocations.
* The physical connection is shared between multiple customers, with each getting a logically isolated portion.
* can scale the bandwidth because the aws partner can logically allocate you more


* takes at least a month for a direct connect link


#### encryption
* direct connect is not encrypted
* however, it IS private on a private line
* to encrypt would have to use VPN as well

* would use the direct connect as the physical infrastructure and the VPN would work on top of that


#### Link Aggregation Group (LAG)
* can create a LAG by having multiple direct connect hard lines and summing them up into one logical one
* this increase speed and failover
* can aggregate up to 4 connections
* must have same bandwidth and terminate at same direct connect location
* can set minimum number of connections for lag to function

#### Direct Connect Gateway
* something you add inside of AWS that the direct connect links connect to
* have to have a DCG to be able to connect to one or VPC's in different regions/accounts
* Direct Connect connects into a single region
* add the private VIF to the DCG
* this will allow the private VIF to be assignable to multiple regions/vpcs/accounts
* has BGP for routing

* direct connect-sitelink
    * if two offices each with their own direct connect link to AWS
    * each of these offices is connected to a direct connect location in a different region
    * can use DCG-sitelink so they can speak with each other and bypass going thru AWS
    * the direct connections will go to AWS then hit the DCG and then sent back out to the other location, avoiding 

#### Other
* can use transit gateway with direct connect but that will only link things in the same region
* can use a direct connect gateway to link single direct connect vif to multiple transit gateways in multiple regions
