* content cached at edge
* 200+ locations around globe
* protect against Network and Application layer attacks i.e. DDoS
* Integrate with:
    * AWS Shield
    * AWS WAF
    * Route 53
* can communicate with HTTPS and can expose HTTPS apis
* can use websocket protocol


* Cloudfront - origins
    * where the original data comes from
    * can actually used Cloudfront to load files into S3

    * origins:
        * s3
        * s3 configured as a website
        * AWS media services: media store container and media package endpoint
        * Any custom origin using http, ex: EC2, LB, API GW,any http backend you want (i.e. on prem)
            * must be public so public edge locations can access
            * can specify security group of IP's of only edge locations that can access
            * if want private Ec2, use an LB public

#### Cache location
1. CloudFront Edge Locations:
    * These are the primary locations where CloudFront caches and serves content closest to end-users.
    * If a user requests content that isn’t available in an edge location's cache, CloudFront forwards the request to a Regional Edge Cache.
    * hundreds of these globally

2. Regional Edge Caches:
    * These are larger, centralized caching layers that aggregate requests from multiple edge locations in a geographic region.
    * If the content is cached at the Regional Edge Cache, it is served from there.
    * If the content is not in the Regional Edge Cache, it forwards the request to the origin server.
    * A Regional Edge Cache aggregates requests from CloudFront Edge Locations within a single region. For example, all edge locations in North America will use the North America Regional Edge Cache.
    * If content is cached in the North America Regional Edge Cache, it will only be accessible to edge locations within North America.
    * If the same content is requested from another region (e.g., Europe), and it’s not available in the Europe Regional Edge Cache, the request will go to the origin server unless other caching layers contain it.

3. Origin Server:
    * The origin is the source of the content (e.g., S3, EC2, or on-premises server).
    * The origin delivers the content to the Regional Edge Cache, which then passes it back to the edge location and eventually to the user.



#### Alternatives
* s3 cross region replication - designed for backup not speed(can still work but is worse than Cloudfront)
* api gw edge uses cloudfront but creates and manages it for you
        


#### Access Control
* custom header
    * configure CF to send a custom request header
    * configure ALB to only send requests to instances that contain that header
    * header name + value must be kept secret!
* security groups
    * at a network level can restrict access to origin by using security groups
    * only allow cloudfront IP's to access
* Origin Access Control 
    * OAC allows you to restrict access to your backend origin (e.g., an Amazon S3 bucket or a custom HTTP server) so that it can’t be accessed directly from the internet. 
    * includes a header with an IAM signing of the request that the origin then verifys


#### Origin groups
* have a primary and secondary origin
* if primary returns error code will request from secondary
* note primary and secondary can be different regions

* if do this with s3 buckets, can combine with CRR to replicate cross region

#### Geo restriction
* allow list or block list for countries
* georestriction for copyrighted content
* the "country" is determined using a 3rd party IP data base
* adds a header called
    * CloudFront-Viewer-Country
    * that is what is accessible to origin
    * can add this yourself as well


#### Pricing
* edge locations all around the worl
* cost of data leaving location varies
* less expensive: USA-> most India
* see chart in this folder

#### Price classes
* reduce the number of regions to save money
* see chart in this folder
1. All regions
    * best performance
    * highest cost
2. Class 200
    * most regions but exclude most expensive
3. Class 1000
    * only least expensive regions


#### Cloudfront Signed URLS
* Signed URL
    * client will either visit an API to get a special URL with a time sensitive signature attached or use the aws cli 
    * allows access to non-publicly accessible content that is signed url enabled 
* can restrict by IP, path, date, expiration
* can upload a public/private key pair to cloufront console to generate a signed url
    * differs from s3 which uses the person who signed the url

#### Custom Error PAges
* Return objecgt to viewer when origin returns 4xxx or 5xx status code to CF
* instead of sending the origins error message will send custo error
* can store these custom pages is s3 (not sure if other places as well)