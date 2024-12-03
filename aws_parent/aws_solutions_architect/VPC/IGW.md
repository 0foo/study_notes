* Attachement scope: attached to VPC (not subnet)
* common configurations: can be attached to a VPC router or a NAT gateway

*  An Internet Gateway (IGW) in AWS only allows traffic originating from resources inside the VPC to which it is attached. This is a critical design principle for security and routing in AWS.

* The Internet Gateway (IGW) only allows outbound traffic from:
    * Instances in public subnets with public IPs.
    * Private subnets via a NAT Gateway for traffic originating within the VPC.

* Traffic coming from a VPN connection via a VGW is treated as "non-VPC-originating traffic" and is not allowed to flow through the IGW.


* workarounds:
    * NAT Instance
        * route traffic into an instance on the network which will then use the instances IP to send traffic via internet
        * this seems to be sort of a hack?
        * Note: NAT Gateway WILL NOT WORK
    * Transit Gateway
        * hub and spoke and can set routing table rules to route VPN traffic to an egress VPC with an IGW