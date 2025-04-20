* DEDICATED LINE between your Data Center and AWS
* traffic does not travel over public internet
* traffic does not go through ISP, so no payment to an ISP
* NOT redundant so will need setup to a second connection or VPN
* Connect to a single region!!!

* typicallly uses BGP and advertises the network of subset of network to the VPC

#### Physical Layter
* architecture
    * customer site -> direct connect hub -> virtual private gateway attached to the direct connect hub->vpc

* direct connect hub is structure located somewhere.

#### VIF
* virtual interface
* The VIF is the logical interface that AWS provides to route traffic
* A VIF (Virtual Interface) is on the AWS side of the Direct Connect connection. It is created and managed within AWS to define how traffic is routed between your on-premises network and AWS resources over the Direct Connect link.
* Your on-premises router communicates with the VIF using BGP for traffic routing.

* types:
    1. public VIF 
        * connect to public facing AWS endpoints like s3, EC2, many more
    2. private VIF - connect to private resources inside of VPC
        * EC2
        * VPC interface endpoints 
        * can then use an Interface VPC endpoint to connect to other servicea
            * this is a more private alternative to public VIF
        * associates with a VPG when it needs to connect to a VPC
            * VPG uses BGP and recieves BGP
    3. transit VIF - when using a Transit Gateway 


* When you create a Virtual Interface (VIF) in AWS Direct Connect, it will attach to your Direct Connect connection but not directly to a VPC. Instead, the VIF connects to a gateway (like a Virtual Private Gateway, or Direct Connect Gateway) that links the VIF to the VPC.

* a single Virtual Interface (VIF) cannot connect to multiple Virtual Private Gateways (VPGs) directly. A Private VIF is limited to a one-to-one connection with either:
    * A Virtual Private Gateway (VPG) (for a single VPC).
    * A Direct Connect Gateway (DX Gateway), which can provide access to multiple VPGs or VPCs via a Transit Gateway or directly to multiple VPG's.


#### Gateways
* transit gateway
    * transit VIF - when using a Transit Gateway 
    * A VIF cannot directly connect to a Transit Gateway. 
    * requires a Direct Connect Gateway to connect to a transit gateway
    * so the architecture is:
        * on prem -- direct connect -- direct connect gateway -- transit gateway -- numerous other things

* Direct Connect Gateway
    * associate a VIF with a DCGW
    * then must connect DCGW to a VPG or a Transit GW which then connect to VPC
    * has BGP for routing
    * There is a limit to the number of Virtual Private Gateways (VGWs) that a Direct Connect Gateway (DX Gateway) can connect to. Currently, a DX Gateway can connect to a maximum of 10 VGWs by default.

    * DCGW can connect to up to 10 VGW

* VPG
    * can connect a private VIF to a VPC directly via a VPG
    * limited to a single VPC connectivity
    * If you are connecting a Private VIF to a single VPC in the same region as the Direct Connect location, you can connect the Private VIF directly to the VPG.


#### Architectures
* on prem - direct connect - VIF - VPG - VPC
    * simple, connect a private VIF to a single VPG to a single VPC
* on prem - direct connect - VIF - DCGW - VPG(up to 10) - VPC  
    * connect up to 10 VPG which also means 10 separate VPC's
* on prem - direct connect - VIF - DCGW - Transit Gateway where anything goes

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


#### Connection via VPG
* can connect a private VIF to a VPG in a VPC
* single connection to a single VPC
* for multiple VPC connection would need a VPG in each VPC




#### Other
* can use transit gateway with direct connect but that will only link things in the same region
* can use a direct connect gateway to link single direct connect vif to multiple transit gateways in multiple regions


####  direct connect-sitelink

* if two offices each with their own direct connect link to AWS
* each of these offices is connected to a direct connect location in a different region
* can use DCG-sitelink so they can speak with each other and bypass going thru AWS
* the direct connections will go to AWS then hit the DCG and then sent back out to the other location, avoiding 