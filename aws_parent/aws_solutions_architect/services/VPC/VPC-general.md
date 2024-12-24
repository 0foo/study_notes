* VPC segmentation
    * VPC created in region 
    * Anything with the word zone requires a subnet(local zone, wavelength zone, availability zone)
    

* Main types of connections into VPC
    * internet (via IGW and/or IGW)
    * VPC peering
    * direct connect
    * VPN


* Security types in VPC
    * NACL's are stateless
        * must declare both inbound and outbound rules
    * Security groups are stateful
        * if inbound allowed, outbound allowed

* Rules can filter by ip,port,dns,inbound/outbound, regex, etc
* allow, block, alert


* active flow inspection: dynamically inspect traffic live 
    * can get detailed like inspecting handshakes 
    * detect unusual traffic patterns
    * port scans

* can also send logs to s3, cloudwatch, kinesis for analysis

* Rules can be centrally managed cross account to apply to many VPC's

