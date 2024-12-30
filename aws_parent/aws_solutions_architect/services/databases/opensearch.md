* Amazon opensearch(Elastic Search is the old name)
* Kibana is now open search dashboard
* Managed version of OpenSearch(open source project, fork of ElasticSearch)
* two modes 
    * managed cluster(see concepts.md for what this means)
    * serverless cluster

* use cases
    * log analytics
    * monitoring )
    * security analytics
    * clickstream analytics
    * indexing


* opensearch + opensearch dashboards + Logstash
    * opensearch provides seach/indexing capability

* opensearch dashboard (used to be Kibana)
    * real time dashboards on top of OpenSearch data
    * alternative to cloudwatch dashboards
* * 
Logstash    
    * log ingestion mechanism
    * requires the logstash agent
    * alternative to cloudwatch logs

* once data in opensearch can create own API to search items, hosted on an EC2 instance
* once items are searched, can link to the actual record in DynamoDB table

#### Architecture
* All data sent to Dynamo/Kinesis can be sent to OpenSearch
* data source -> dynamo -> dynamo stream -> lambda -> opensearch 
* data source -> kinesis data stream -> kinesis fire hose -> opensearch
* can search data in opensearch and then link to the data in dynamo

* cloudwatch logs -> subscription filter -> lambda -> opensearch
* cloudwatch logs -> subscription filter -> kinesis firehose -> opensearch

