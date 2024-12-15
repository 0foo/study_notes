#### API gateway
* resides in a region but in aws cloud

* limits
    * timeout on any request on API gateway is 29 seconds
        * this means once API GW recieves a request and forwards it to the 'integration' handling the request it will only wait 29 seconds for a response
        * this applies to websockets only in the sense that it waits for the response from the integration for 29 seconds to establish the web socket connection
        * will shut a web socket connection after 10 minutes of inactivity 
    * 10MB max payload size in one request

* deployment stages
    * API changes are save as 'deployment stages'
    * name the stages anything 'dev, test, lemur'
    * stages can be rolled back as history is kept of all changes

* 3 ways to deploy API GW
    * edge optimized 
        * sends requests through Cloudfront Edge in order to reduce latency
        * note: API GW still sits in a single region
        * When you configure an API Gateway as edge-optimized, AWS creates a global CloudFront distribution for your API.
        * This distribution uses CloudFront's network of edge locations around the world.
        * The edge location routes the request over Amazon's private, high-speed global backbone network to the region where the API Gateway is deployed.

    * Regional
        * normal mode, API GW is in a single region 
        * can spin up a Cloudfront distribution seperately to integrat with this
    * private
        * only access within VPC
        * uses a VPC interface endpoint
            * each VPC interface endpoint can access multiple APIs
        * control access with endpoint policy or gateway resource policy
            * can allow cross account access

* caching API responsed
    * reduce number of calls made to backend
    * checks cache first before
    * data in cache has TTL
        * 300ms is default
        * can set TTL from 0(no cacheing) to 3600 seconds(1 hour)
    * caching can be set per method
    * client sending request can invalidate cache with header Cache-Control: max-age=0
    * can flush(invalidate) entire cache if you want
    * cache can be encrypted
    * cacpcaity can be between .5GB to 237GB

* errors
    * 4XX- indicates request sent from client was malformed/bad/not authorized
    * 403- access denied
    * 429-quota exceeded/throttle
    * 5XX- indicats an error on the server side
    * 502-


* security
    * can load SSL certs onto API GW
    * use route 53 to define a CNAME
    * resource policy that controls who can access the API
        * AWS accounts, CIDR ranges, IPs, VPC's
    * IAM execution roles for API GW 
        * to be able to invoke/access AWS services like lambda, s3
    * CORS
        * can enable access from certain domains or from all domains

* authentication(uses authorizers in API gateway)
    * IAM
        * good for private interal use, pass IAM creds in headers
    * Lambda authorizor
        * custom auth logic
        * use lambda to verify custom 3rd party auth(Oauth,SAML)
        * will use the lambda to send a request to a 3rd party the return if auth or not(e.g., Auth0, Firebase, or self-issued JWT tokens)
    * Cognito
        * AWS service that handles users and authorization
        * client authenticates with Cognito and gets a JWT token
        * it passes the token to API gateway which then checks with cognito user pool
        * the user will then be included with the

* logging/monitoring/traces
    * cloudwatch logs/metrics
        * can log full request/responses
        * can send logs to kinesis fire hose
        * metrics per stage and have standard metrics like latency, cachecount, etc
    * xray
        * can get tracing throught the entire API GW to Lambda



* Usage plan and API keys
    * usage plan
        * can define who can access, quota(total how much), throttle/meter(how much in a time period)
        * auth is via API key
        * 429 too many requests error

* throttling limits
    * API Gateway has two levels of throttling:
        * Account-Level Limits:
            * By default, AWS API Gateway limits the number of requests per region per account.
            * Soft limits:
                * 10,000 requests per second (RPS).
                * 5,000 concurrent requests (burst).
                * These can be increased by submitting a request to AWS Support.
        * API-Level Limits:
            * You can set specific rate and burst limits on individual API Gateway stages or methods.
            * Rate limit: Steady-state number of requests per second.
            * Burst limit: Maximum number of requests that can be handled temporarily (short-term spike).


* websocket
    * the web socket stays open with the API Gateway!
    * can trigger lambdas when sending a json to the api gateway!
        * can either use an action key in the json which triggers a route in API gateway or have a generic lambda handler that will trigger other lambdas based on values in the json payload you send it
    * note the lambda will not be aware of the websocket connection, so it will send it's response back to a specific url representing that api gateway connection on that api gateway stage. 
        * wss://abc123xyz.execute-api.us-east-1.amazonaws.com/dev/@connections/{some cnnection id}
```
    # inside the lambda, event is recieved from api gw
    connection_id = event['requestContext']['connectionId']
    domain_name = event['requestContext']['domainName']
    stage = event['requestContext']['stage']
    
    # API Gateway Management API Endpoint
    endpoint = f"https://{domain_name}/{stage}"
    apigateway_management_api = boto3.client('apigatewaymanagementapi', endpoint_url=endpoint)

```
    * can invoke dynamo without using a lambda using AWS service proxy(essentially a mapper)
    * API Gateway supports direct service integrations with DynamoDB through its AWS service proxy feature. This allows API Gateway to directly perform actions like PutItem, GetItem, UpdateItem, or Query on DynamoDB tables.





#### Usages
* versioning
* authorization
* traffic management
    * API Key
    * throttles
* huge scale
* serverless
* req/resp transformations
* OpenAPI spec
    * can generate a client library from that spec in many programming langs
    * allows documentation
* CORS



#### Architecture
* want to upload files through API GW to s3
    * will have a 10MB limit

* want to have an API GW redirect to s3 url
    * can use an lambda to generate an 'signed url'
    * 'signed url' is a url with an AWS signature and upload expiration and file metadata for secure uploads

*  client -> send request -> API GW -> Lambda, which generates a signed url to send back to client
*  client uses signed url -> upload to s3



