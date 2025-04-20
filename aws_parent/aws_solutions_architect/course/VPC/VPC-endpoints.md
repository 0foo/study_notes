#### AWS managed interface
* An AWS Managed Interface refers to an Elastic Network Interface (ENI) that is created and managed automatically by AWS to facilitate communication between AWS-managed services and resources within your Amazon Virtual Private Cloud (VPC). These interfaces provide seamless private connectivity for various AWS services.

* functions as a normal interface with security groups, flow logs, etc.

* Types:
    1. VPC Endpoint (Interface Endpoint)
    2. AWS Client VPN
    3. Elastic Load Balancer (ALB/NLB)
    4. AWS PrivateLink
    5. Network Firewall or Transit Gateway:

* Costs:
    * There are charges associated with the use of managed interfaces, such as data transfer costs and hourly charges for services like Interface Endpoints.





### Endpoints general
* connect a vpc to an AWS service 
* services normally have to access AWS resources via the public internet
* this opens up way to access aws resources on private aws network
* when add them DNS is automatically updated with the url to PRIVATE IP instead of public IP, overrides
* route table is also automatically updated
* very important: GW endpoints only work for things INSIDE A VPC. NOT TRANSITIVE


### gateway endpoint
* endpoint gateway is specifically for s3 and dynamo
* doesn't use interface
* in the routing table the target is the public ip's of the service and the destination is a vpce (vpc endpoint)

### VPC endpoint interface
* Is essentially an ENI in a subnet with an IP/security group that the whole subnet can send data to
* need to "enable DNS hostnames" and "enable DNS support"
* sharable so can be accessed from Direct Connect or Site to site VPN

#### Differences
Gateway Endpoint:
    Works at the route table level. i.e. acts like the service 
    Traffic is routed automatically to the Gateway Endpoint when the route table is updated.
    Access can be controlled using VPC policies and bucket/table policies.
    Does not support security groups.
    Is free


Interface Endpoint:
    Works at the application level.
    Applications or services must explicitly connect to the endpoint by using the endpoint's private IP address or domain name (resolved via private DNS).
    not free
    can have security groups


#### Gateway - Endpoint policies
* similar to a security group in purpose
* speicifc policies different than IAM or service specific policies
* note: sometimes it's good to add a full deny on the aws resource to anything not coming from the vpc endpoint
* this requires a condition statement
    * aws:sourceVpce: <some vpce id>
    * aws:sourceVpce: only works for vpc endpoint

* example: add a s3 bucket policy to the s3 bucket to deny any access with a condition not equals aws:sourceVpce

### Troubleshooting
* outbound security group on the instance are open , ie attached to the instance
* check route tables
* check DNS 
* check security groups if it's an non-gateway interface endpoint
* check VPC endpoint policy if it's a gateway
* check the actual AWS resource policy i.e. the policy attached to s3
* check IAM roles







