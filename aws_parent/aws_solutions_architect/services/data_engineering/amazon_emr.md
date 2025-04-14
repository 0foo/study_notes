* Elastic MapReduce
* helps create Hadoop clusters to analyze and process vast amounts of data
* move on prem hadoop cluster jobs to AWS
* clusters can be made of hundreds of ec2 to process jobs then shutdown once job is completed
 * auto scale with cloudwatch
 * use case: data proc, machine learning, web indexing, big data
    * anything to process at scale

* EMR launched within VPC in single AZ
    * will get better network performance
    * more volative to be in a single AZ
* EC2 instances are using HDFS for the file system
    * hadoop distributed file system
    * temporary storage
* for long term storage need to use EMRFS
    * has native integration into S3
    * more durable, multi AZ

* apache hive
    * can run this in EMR to integrate/read from Dynamo


* can have long running clusters
* can have transient clusters


#### Cost optimization in EMR
    * master node - orchestrates all the other nodes and is long running
    * core node - run tasks and store data long running
    * task node - just to run tasks, usually spot instances
    * purchasing options
        * on demand - reliable, predictable, won't be terminated
        * reserved - minimum on one year, way cheaper, EMR will automatically use if available
            * good for master node and core nodes
        * spot - less reliable but way cheaper, good for task nodes

#### Instance configuration
* Uniform instance groups: select single instance type and purchasing option(on demand, spot) for each node (has autoscaling)
* Instance fleet: 
    * can specify a mix of instances and on demand and spot 