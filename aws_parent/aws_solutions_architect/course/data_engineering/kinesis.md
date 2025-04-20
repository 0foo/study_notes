* managed "data streaming" service
* ingest a lot of data at scale in real time
* great for:
    * app logs
    * metrics
    * IoT
    * clickstreams

* great for "real time" big data
* great for streamin processing framework
* data is automatically replicated synchronously to 3 AZ
    * highly avail, fault tolerant

* Kinesis is 3 services
    1. Kinesis streams - low latency streaming ingest at scale
    2. Kinesis analytics - real time analytics on streams using SQL
    3. Kinesis data firehose(KDF) - to load streams into s3, redshift, elasticsearch, splunk

* obtain data via streams
* can send to KDF for storage
* can send to KA for analytics
* can send to KA then to KDF 
* etc