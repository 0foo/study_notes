#### Hosted Zone
* a Hosted Zone is essentially just a domain with all the records attached to it
* can associate a traffic policy with a hosted zone
* public zone - for internet resolving
* private -     resolvable only within AWS

#### DNS record types
* A/AAA
    * A: maps hostname to ipv4
    * AAA: maps hostname to ipv6
    * Can point multiple domains/subdomains to the same  IP with multiple A/AAA

* CNAME: maps hostname to another hostname
    * target must have an A record
    * cannot create a CNAME for a TLD
        * can only create a CNAME for a subdomain
        * would have to be a www.somesite.com, not somesite.com
* NS: record of the nameserver/s that hold which authoritative name servers are responsible for handling queries for a particular domain or subdomain
    * If a DNS server doesn't know how to resolve a domain, it responds with NS records for the next level of the DNS hierarchy.
    * This process continues until:
        * The record is found, or
        * An NXDOMAIN response is returned if the domain does not exist. (failure mode)

* ALIAS record: An ALIAS record in Route 53 is a special type of DNS record specific to AWS. It allows you to point a domain name (or subdomain) to an AWS resource instead of an IP address.
    * ALIAS records are AWS-specific, designed to simplify integration with AWS resources and handle dynamic IP changes automatically.
    * NOTE: ALIAS are completely transparent to the client which views them essentially as an A record
    * Here’s what happens:
        * The dig query requests the A record for example.com.
        * Route 53 resolves the ALIAS target (my-cloudfront-distribution.cloudfront.net) into its corresponding IP addresses.
        * The client receives the resolved IP addresses as if they were direct A records.
    * When a resolver queries an ALIAS record, Route 53 dynamically resolves the ALIAS target (e.g., the IP addresses for the CloudFront distribution or ELB) and responds with the resolved A or AAAA records.
    * The TTL value returned for an ALIAS record is inherited from the target resource's TTL (not explicitly set on the ALIAS record itself).
    * in many cases won't be able to do a CNAME but can do an ALIAS
    * can't set ALIAS for an EC2 domain name

* DNS TTL
    * caching of the DNS response for the TTL 
    * will use the cached DNS response instead of reaching out to DNS server
    * note: when change record, will have to await for the TTL to expire so the client will check with DNS server again
    * tradeoff between less load on DNS server and how easily to change records
    * Except for ALIAS, TTL is mandatory
        * this is interesting as you can repoint your alias records to new locations without a TTL

#### Routing policies
* can specify multiple values in a DNS record 
    * respond with multiple value in the DNS record
    * a random one is chosen by the client

* all but simple policy can be associated with health checks

* simple
    * route traffic to a single resource
    * not associated with a health check
    * can specify multiple values
* weighted
    * in rt53 can specify weights of resources 
    * Based on the weights assigned, Route 53 randomly selects one record with a probability proportional to its weight.
    * rt53 will return that to the client
    * all handled in rt53 client only sees one record 
    * can be associated with health checks which means rt53 will not return the record if the health checks fail
* latency based records
    * redirect to the source that has the least latency to us
    * latency defined by the traffic between the users and AWS regions
    * can associate with health checks as well
    * How Latency-Based Routing Works
        * Client Query:
            * A client (e.g., a web browser or application) makes a DNS query for a domain (e.g., example.com).
            * This query is handled by the client's recursive DNS resolver (provided by an ISP or corporate network).
        * Resolver Location:
            * Route 53 sees the IP address of the resolver, not the client’s IP.
            * It uses the resolver’s IP address to estimate the client’s geographic location.
        * Latency Evaluation:
            * Route 53 uses pre-computed latency measurements to determine which AWS region provides the lowest latency for that resolver.
            * These measurements are periodically updated by AWS to reflect real-world conditions, including changes in network topology or congestion.
        * Record Selection:
            * Route 53 selects the DNS record for the endpoint (e.g., IP address, ELB, CloudFront distribution) associated with the region that has the lowest latency for the resolver.
            * It returns only one record in response to the query.
* failover policy
    * have primary/secondary resources
    * simple health checks and if the primary fails will route to secondary

* geolocation  policy
        * route 53 uses the ISP or whoever is the clients originating DNS resolver to identify location
        * will respond with a record matching the closest location of the resource
        * have a default fallback if no gelocation match exists

* geoproximity policy
    * similar to geolocation
    * Geoproximity routing is part of Route 53’s traffic flow feature, and you must use a traffic flow policy to configure it.
    * Like geolocation routing, Route 53 uses the resolver's location, which may not always align with the client’s actual location.
    * adds a bias
        * Route traffic to the nearest resource while biasing certain regions for load balancing.
        * a greater bias will send a larger area of traffic to a resource
        * essentially expands the region with a larger bias
        * can send more traffic to the region with bias from 1 to 99
        * can sen less traffic to the region with bias from -1 to -99
* multi-value poicy
    * returns multiple values/resources
    * associated with health check so only valid/healthy responses are returned
    * returns up to 8 values
    * can load balance via DNS but not a substitute for a true LB

* IP based routing
    * similar to geoproximity or geolocation but instead of looking at client and resolvers location it looks at the IP
    * routes based on the CIDR of the client and its resolver
    * allows routing based on specific IP locations, i.e. sending all traffic from a particular ISP to a certain resourcre

#### Traffic flow
* visual editor 
* allows complex decisions trees in routing flows 
* allows bias so that certain regions will have much larger area sending traffic to a resource
* configurations can be saved as a 'Traffic Flow Policy'
    * a single policy can be applid to dfifferent domain names(Hosted Zones)
* supports versioning

#### health checks
    * can add health checks on rt53 
    * note: theres a bunch of health checkers located all around the world
        * health checkers outside of VPC's so can't health check private/on prem

    * create a cloudwatch alarm to monitor a private/internal/on prem resource
        * the health checker can monitor that cloudwatch alarm, i.e. check the alarm itself
    * can specify conditions for pass/fail
        * pass: 200/300 status code
        * pass/fail: based on text in first 5120 bytes of the response 

    * 3 types of hc
        * monitor an endpoint
        * calculated health check, monitor other health checks, 
            * combine a bunch of health checks into one
            * can have up to 256 children into one
            * specify how many of child need to pass to make parent pass
        * cloudwatch alarm health check i.e. can make any thing a health check
            * i.e. database overload, etc.

#### hybrid DNS 
* have both on prem DNS servers AND rt53 dns servers 
    * both will have different domains i.e. aws.org and myonprem.com
    * both of those will not know each other's full listing of DNS zones
    * both can have a generic forwarding domain and will forward those requests to the handling DNS server
    * essentially functions like normal DNS as it forwards request to the resovler to handle it.
    * note: will need to have a 'Resolver Endpoint', which are ENI's on the subnets hosting the servers that are essentially attached to route 53 and allow external requests to be recieved by route 53 or internal requests from route53 to leave the subnet to go to the on prem resolvers
    * VERY IMPORTANT TO KNOW ABOUT INBOUND AND OUTBOUND ENPOINTS and hybrid DNS for exam

* split horizon
    * internal DNS resolution vs External public DNS resolution for the same resource
    * DNS will return different responses based on if the request if from internal networks or external public

#### Resolver rules
    * rules that are set to require forward requests for specific domains to another resolver
        * the rule is the resolvers IP
    * can customize in detail for example send a subdomain to a different resolver than it's parent domain
    * there's a ton of preconfigured rules already for internal AWS stuff
    * if multiple rules match route 53 will choose the most specific match
    * can share these rules across account if you're using AWS Resource Access Manager(RAM)
        * but then manage centrally in one account


#### OTher

* DNSEC- dns security
    * good for protecting from man in the middle attacks
    *  SEcure domain names
    * only works with public zones
* can buy domain from 3rd party and point at rt53 



#### Architecture

* have two replica RDS instances-one active, one as backup, both in internal VPC
    * have either an 
        * API endpoint via lambda/ec2 to do a health check
        * cloudwatch alarm set on RDS
    * can set the rt53 Health check to check these since they're not internal private and can be checked
    * can then trigger a cloud watch alarm on this check which will trigger a lambda to 
        * change the backup to primary
        * change rt53 dns  to point to back up