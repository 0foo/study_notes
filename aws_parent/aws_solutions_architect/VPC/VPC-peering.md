* VPC Peering in AWS allows you to establish a direct network connection between two Virtual Private Clouds (VPCs). This connection enables instances in one VPC to communicate with instances in another as if they were in the same network. It works over AWS's private network infrastructure, providing secure and scalable connectivity.

* can be cross region

* send peering connection and both accepts
* then both VPC's need to configure routes/DNS to the respective peering connection


* VPC is non-edge allowed: cont' connect one VPC to resources that are on the edge THROUGH another VPC via peering
    * VPN
    * Direct Connect
    * Internet GW
    * NAT GW
    * Gateway VPC endpoint (s3 and dynamo)

* VPC is non-transitive
    * can't connect to another VPC VIA another VPC

* No overlapping CIDR in VPC's if trying to peer them
    * even just one, AWS will not allow!!!

* Data transfer charges apply for traffic sent across VPC peering connections, especially for cross-region traffic.

