#### Alexa for business
* book meeting room, increase meeting room efficiency


#### Workspaces
* Secure cloud desktop
* helps eliminate on prem VDI (virtual desktop infrastr..)
* pricing on demand or monthly
* integrated with microsoft AD
* Workspace updates managers -> keeps applications updated
* Windows update -> keeps windows updated
    * by default updates turned on
* can define update maintenance windows 
    * default is 12 AM to 4AM
    * workspaces will reboot automatically for you

* Multi region failover
    * must use an AD connector and not a multi region AD

* IP access control groups
    * similar to security groups for Amazon workspaces
    * list of IP's/CIDR ranges that users are authorized to connect from
    * must whitelist any VPN or NAT

#### Appstream
* simply streams an app in a web browser
* no machine required
* like geforce now but for apps

#### Device farm
* if want to test an mobile/web application across multiple devices
* runs across real browsers and mobile devices
* fully automated using a framework
* Will generate videos and logs to document the issues encountered
* can also remotely log into the devices to debug


#### Macie
* fully managed data security and privacy service
* uses machine learning to discover and protect your sensitive data
* alerts if it discovers PII (personally idenitifable information)
* put the data in S3 for Macie which then notify via event bridge
* can integrate event bridge with SNS topic, lambda function