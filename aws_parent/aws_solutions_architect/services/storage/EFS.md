* managed Network File System
* expensive
* pay per GB used vs EBS pay per GB provisioned
* is region based and the same file system can attach to instances in different Zones
* note: NFS only works on Linux does NOT work on Windows
* NFS v4.1
* encryption at rest with KMS
* attaches to one VPC with one mount target ENI per AZ
* posix files system with standard (linux) file system api
* scales automatically, pay per use, no capacity planning
* EFS Scale
    * 1000's of concurrent NFS clients
    * 10GB or more throughput
    * grow to petabyte sizre automatically
    * note throughput grows in size as more space utilized

#### Performance and storage classes

* performance mode
    * General Purpose (default)
        * latency sensitive use cases (i.e. web server)
    * Max I/O 
        * higher latency
        * but high througput
        * big data, media processing
    * throughput mode
        * Bursting Throughput is cost-efficient and works well for workloads with variable throughput needs.
        * Provisioned Throughput is ideal for applications that require predictable and consistently high throughput, regardless of storage size.
            * can set your throughput
            * costs more

#### Storage tiers 
    * standard  
        * (11 9s durability across multiple AZs)
        * Higher cost compared to other storage classes due to frequent access optimization.
        * Designed for frequently accessed data with high durability and low latency.
    * IA (infrequent access)
        * A lower-cost storage class for infrequently accessed data.
        * Suitable for data that requires high durability but is accessed less frequently.
        * good for Backup and disaster recovery or archiving
        *  (11 9s durability across multiple AZs)
        * lower base cost but includes a per-GB retrieval fee when data is accessed.
    * One Zone and One Zone IA
        * same performance but less durability
        * 99.9% (3 9s), as it relies on a single AZ.
        * more affordable
        * Non-critical workloads with low durability requirements.
        * IA option allows reducing costs even further 
    * Amazon EFS offers lifecycle policies to automatically move data between storage classes, optimizing cost: