* fully managed service for file transfers into/out of S3 or EFS using FTP protocol


* supports three kinds of protocols
    1. FTP 
        * (unencryption, other two are encrypted)
    2. FTPS (over SSL)
    3. SFTP (secure file transfer)

* pay per endpoint per hour 
* pay per data transferred

* can store and manage user credentials in the service
* can also integrate with existing auth providers 
    * AD
    * LDAP
    * Okta
    * Cognito
    * others/custom


* Exam will test on the following:

#### Public Endpoint on public net
* note the public endpoint IP's are dynamic and changes over time
* so use the DNS name 
* can't setup allow lists by IP addy in your firewall

#### VPC endpoint 
* only access the FTP endpoint via internal services to VPC
* can connect to VPC via VPN or Direct Connect 
* static private IPs (private) 
* can setup allow lists in firewall

#### VPC endpoint with internet facing access
* basically have the endpoint with a static private IP
* can use NAT or Network LB with a static EIP to provide access to an internet gateway
* can setup security groups to protect who can access 