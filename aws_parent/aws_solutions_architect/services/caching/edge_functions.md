* execute logic as close to user as possible
* code executed

* use cases: 
    * change the request/response, 
    * validate auth signatures like JWT
    * request filtering
    * A/B testing
    * bot mitigation at edge
    * 


#### Cloudfront edge
* javascript
* can't access external services
* operates at the EDGE baby
* super performant: sub-ms startup times, millions of req/ps
* managed entirely within CloudFront


##### Lambda Edge
* lambda/python
* can access anything
* not as performant: 1000's of rps
* operates at the 'regional edge'  so not as close as the edge
* When you create a Lambda@Edge function and associate it with an Amazon CloudFront distribution, it is automatically replicated to all Regional Edge Caches globally.

#### Types of request response
* viewer req/resp
    * the back and forth between edge function and user
* origin req/resp   
    * the back and forth between origin and edge function

* lambda can handle both origin req/resp and view req/resp
    * client -> viewer req ->  lambda edge function -> origin req -> origin
    * origin -> origin resp -> lambda edge function -> view resp -> client

* Note: cloudfront functions can only handle viewer req/resp
    * client -> viewer req ->  CF edge function  -> origin
    * origin -> CF edge function -> view resp -> client


* can combine cloudfront functions and lambda 
    * cloudfront functions handle viewer req/resp
    * lambda edge funct handles origin req/resp


#### use lambda edge
* when need longer execution time
* when you need network access
* 3rd party api calls
* access other services
* better resources
* larger package size
* 5 seconds of runtime for user req/resp and 30 sec of runtime for origin req/resp
* Note: worse QPS performance
* can use 3rd party libraries (i.e. Aws sdk to access other aws services)
* some use cases
    * if need other aws service
    * if need to access other apis
    * if need file system access
    * if need access to body of http requests
    * if need longer processing times

    * load content based on User Agent
        * i.e. browser get's higher/larger resolution image vs mobile device 

    * use lambda at edge to access dynamo and can access this via client request
        * can also integrate auth into the process inside the lambda 
        * this creates a basic serverless API like API Gateway + lambda but with way less features than API Gateway
        * global/serverless way to do api in AWS

    * modify origin
        * setup
            * have a cloudfront @ edge location in one region
            * have s3 bucket in another origin
            * initial get from origin could take a while as it's cross origin
        * solution:
            * set up cross region replication in s3 to same region as cloudfront 
            * setup a lambda@edge function to modify origin and send the request to the same region origin s3 
        * Note:
            * CloudFront Functions cannot change the origin domain name, origin region, or other origin-related parameters.
            * Interact with the Origin Request Lifecycle: CloudFront Functions don’t have access to the origin request/response lifecycle, so they can’t alter requests after they’ve been routed to the origin.

#### use CF func
* when need max performance
* only have 1ms execution time
* no access to body of request!!

* some use cases:
    * cache key normalization: can alter the headers,query strings,url to create an optimzed cache
    * header modification: insert, modify, delete headers in req/resp
    * URL rewrites/redirects
    * validate JWT's at edge to allow/deny requests to the origin
        * note: there's no integration with other service so have to manage key rotation another way
        * using a lambda would allow integration with other auth services 
