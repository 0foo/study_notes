* Anycast IP
    * essentially an IP that multiple servers share
    * Multiple servers in different geographic locations are configured to use the same IP address.
    * Routing to the Nearest Server:
        * The Border Gateway Protocol (BGP) or other routing protocols ensure that traffic is directed to the closest (or most optimal) server based on metrics like latency, hop count, or path cost.
    * Dynamic Failover:
        * If a server goes offline, the traffic is automatically rerouted to another server sharing the same anycast IP, ensuring high availability.
* 2 anycast IP are created for your applications
* Anycast IP will route traffic to closest edge location
* The AWS  will then route the traffic to your resources in whatever region they're in over the high speed internal AWS backbone

#### how it works

* Global Entry Points:
    * When you set up Global Accelerator, AWS assigns you two static IP addresses from different network zones for redundancy.
    * Users connect to these static IPs to access your application.

* Traffic Optimization:
    * The user’s request is routed to the AWS global edge location nearest to them.
    * From the edge location, traffic travels over the AWS global network to the endpoint closest to the user or the best-performing one.

* Endpoint Management:
    * You can add various AWS resources as endpoints:
        * Elastic Load Balancers (ALB, NLB)
        * EC2 instances
        * Elastic IP addresses
    * Endpoints can be in different AWS Regions, allowing for global application deployment.

* Health Monitoring:
    * Global Accelerator does health checks of your application
    * Global Accelerator continuously monitors the health of your application endpoints and reroutes traffic to healthy endpoints as needed.

* DDoS protection
    * AWS Shield


#### Cloudfront vs Global Accelerator
* Cloudfront
    * improves performance for cacheable content: images, videos, API returns, HTML, etc. 
    * content is served and cached at the edge

* GA
    * It's essentially an edge proxy that will send your traffic over high speed AWS network to your application in any region
    * works for non HTTP use cases also: gaming, IoT, VOIP
    * good for HTTP needing failover 
    * good for HTTP needing static IP's