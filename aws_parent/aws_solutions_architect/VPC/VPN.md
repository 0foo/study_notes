### Site to Site VPN
* consists of a customer gate way(CGW) and virtual private gateway(VPG)
    * virtual private gateway also used for direct connect

* customer network - vpn appliance - customer gateway(aws) - virtual private gateway - vpc
* can either use static routing in the routing tables 
* or can use BGP
    * BGP propogates routes between networks
    * have to give each side of the connection an autonomouse 


* customer site <-> CGW <->VPN <-> VGW on VPC <-> NAT <-> IGW <-> internet
    * customer site  can't access internet, see IGW, doesn't allow off VPC traffic


* the reverse direction DOES work though
    * can access internet from VPC via the customer site
    * Internet <- customer site <-> CGW <-> VPN <-> VGW <-> VPC 


* VPN cloud hub
    * can connect a bunch of CGW to a single VPG
    * useful for if an company has a bunch of offices that all need VPN
    * useful for reduncany also



#### AWS client VPN
* it's a simple way to connect to your VPC via OpenVPN
* it will put an ENI for your local machine on one or more subnets of the VPC
* Essentially your machine is treated as an instance on the VPN
* can combine this with a Site to Site VPN inside the VPC to access on prem infrastructure in a corporate data center or some such from yor local laptop or client machine
* very important concept: it acts like your machine is ON the VPC
    * can access edge resources and peered resources
    * this means you can acceas resources on a peered VPC,  access internet via IGW, access corporate on prem, etc.



####  On Premise redundant connection
1. Site to Site Active connection
    * have two office locations connected to AWS via their own VPN/Direct Connect line
    * the two offices are connected with each other also separately from anything AWS related
    * if one of the offices lose VPN/Direct connection, can route the traffic through other office connection and then VPN/Direct connection to access AWS

2. Can also have varous flavors of VPN connectivity/Direct Connect via one or more offices all connected to each other for redundancy