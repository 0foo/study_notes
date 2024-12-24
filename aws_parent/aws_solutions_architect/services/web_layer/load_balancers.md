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