* 4 kinds(in order of release date)


* Classic
    * old generation
    * HTTP, HTTPS, TCP, SSL(secure TCP)
    * Health checks can be L7 via HTTP or layer 4 via TCP
    * only one SSL certificate allowed(must use multiple CLB for multiple)
    * TCP passes all the traffic to the EC2 instance only way 

    
* Application
    * HTTP, HTTPS, Websocket
    * Layer 7 only HTTP(S), Websocket, HTTP/2
    * multiple SSL certs allowed
    * Can load balance to multiple target groups i.e. HTTP applications/services 
    * health checks at the target group level
    * Can load balance to multiple services/applications on the same machine which is a great fit for containers
        * dynamic port mapping
    * can write routing rules to LB traffic to in detail:  path, headers, query string, etc.
        * ex: one route for search, and one for login
    * can integrate it directly with various services
        * EC2
        * ECS on EC2
        * ECS on Fargate
        * AWS Global Accelerator
        * AWS WAF
        * S3 (Static Website Hosting)
        * API Gateway (as an HTTP backend)
        * Lambda


* Network LB
    * TCP, TLS(secure TCP), UDP
    * handle millions of RPS
    * this is the speed LB, very high performance
    * less latency than ALB also
    * has one static IP per AZ
    * supports assigning an Elastic IP-helpful for whitelisting an IP
    * not included in AWS free tier
    * target groups: EC2 instance, or an Appliation Load Balancer
    * can only send traffic to privte ips


* Gateway LB
    * operates at layer 3(network)-IP protocol
    * deploy scale/manage 3rd party network virtual appliances in AWS
    * Firewalls, intrusion detection, deep packet inspection, payload manipulation
    * operates on IP packets (layer 3)
    * transparent exit/entry
    * distribute to applicances
    * Uses Geneve protocol on port 6081
    * allows you to spin up a bunch of parallel traffic analyzer tools and get the traffic Load Balanced between them
    * After traffic analysis the applicancds send the data back to LB which forwards to the application
    * target groups: EC2, or private IPs

* target groups
    * EC2 instances: http
    * ECS tasks: http
    * Lambda -> http request tranlated into json
    * any private ip address: http

* DNS
    * all load balancers have a DNS url upon creation
    * AWS Network Load Balancer (NLB) provides a unique zonal DNS name for each availability zone (AZ) where it is deployed. These zonal DNS names allow clients to directly access specific load balancer nodes in a particular AZ, which is useful for certain advanced networking scenarios
    * Normal regional url: <load-balancer-name>-<hash>.<region>.elb.amazonaws.com
    * Zonal url: <AZ>.<load-balancer-name>-<hash>.<region>.elb.amazonaws.com
    * This has a url for each AZ in the LB and has a url for the LB in general
    
* cross zone load Balancing
    * LB disgtributes traffic evenly across all registered instances in ALL AZs
    * i.e. if have two instances i one AZ and 8 in another AZ the traffic will STILL be distributed even across all 10 instances
        * i.e. 10% of traffic to each instance no matter the AZ
    * always on (cant be disabled in ALB, must be enabled in all the rest)



* sticky session
    * the client always communicates with the same instance
    * makes sure user doens;t lose session data (i.e. if cookie in memory or somegthing)
    * enabling this, may bring imabalance to the load over back end EC2 instances


* Routing algorithms
    * Least Outstanding Request
        * instance with lowest number or pending/unfinished requests
        * CLB and ALB have
    * Round robin
        * just cyclers thru
        * ALB, CLB
    
    * Flow Hash
        * take a bunch of data from the request packet and generate a hash and route based on that hash
        * with this its permanantly sticky




#### ways to connect to load balancers
Yes, among the AWS load balancers, Network Load Balancers (NLBs) can be internet-facing and associated with Elastic IPs (EIPs). However, Application Load Balancers (ALBs) and Gateway Load Balancers (GWLBs) do not directly support Elastic IPs.

Here’s how Elastic IPs work with different load balancer types:

1. Network Load Balancer (NLB)
* Supports Elastic IPs: 
* For each subnet where you deploy an NLB, you can associate a specific Elastic IP (EIP). This makes the NLB's public-facing IP address static, which is ideal for predictable client-side configurations.
* Internet-Facing:
* NLBs can be configured as internet-facing to expose services to the public internet.
* Use Case:
* Ideal for applications requiring low latency, high throughput, and static IPs (e.g., FTP, gaming, VoIP).

Steps to Configure an Internet-Facing NLB with EIP:
* Create an NLB with internet-facing scheme.
* Add listeners for the required ports (e.g., 21 for FTP).
* Associate an EIP for each public subnet used by the NLB.

2. Application Load Balancer (ALB)
* Does Not Support Elastic IPs:
* ALBs are designed to route traffic using DNS-based endpoints rather than static IPs. They use dynamic public IPs managed by AWS.
* Internet-Facing:
* ALBs can still be configured as internet-facing but rely on AWS DNS names (e.g., abc123.elb.amazonaws.com) instead of static IPs.
* Use Case:
* Best suited for HTTP/HTTPS workloads with advanced Layer 7 routing features.

Workaround for Static IPs with ALB:
* Use a Static IP Proxy:
* Deploy an NLB in front of the ALB and associate EIPs with the NLB. The NLB forwards traffic to the ALB.
* Use AWS Global Accelerator:
* Provides static IPs that route traffic to the ALB via a global edge network.

3. Gateway Load Balancer (GWLB)
* Does Not Support Elastic IPs:
* GWLB is designed for traffic inspection and routing through virtual appliances, not for public internet-facing use.
* Use Case:
* Ideal for deploying and managing third-party virtual appliances (e.g., firewalls, intrusion detection systems).

Workaround for Public Traffic with GWLB:
* Use an NLB with EIP in front of the GWLB for public-facing traffic.

4. Classic Load Balancer (CLB)
* Supports Elastic IPs:
* For each subnet where you deploy a CLB, you can associate an EIP.
* Internet-Facing:
* CLBs can be internet-facing and use EIPs for static IP configuration.
* Use Case:
* Legacy applications still relying on CLBs for Layer 4 and basic Layer 7 routing.

Summary of Elastic IP Compatibility
Network Load Balancer (NLB): Supports Elastic IPs and can be internet-facing, ideal for low latency and static IP needs.
Application Load Balancer (ALB): Does not support Elastic IPs but can be internet-facing with advanced routing for HTTP/HTTPS.
Gateway Load Balancer (GWLB): Does not support Elastic IPs and is not internet-facing, used for traffic inspection.
Classic Load Balancer (CLB): Supports Elastic IPs and can be internet-facing for legacy workloads.

Conclusion
* If you need static IPs with internet-facing capability, the best choice is the Network Load Balancer (NLB) or Classic Load Balancer (CLB).
* For ALBs or GWLBs, workarounds like pairing with an NLB or AWS Global Accelerator can provide static IP functionality.

Would you like step-by-step instructions for setting up an NLB with EIPs?
