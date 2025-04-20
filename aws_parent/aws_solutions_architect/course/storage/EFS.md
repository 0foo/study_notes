* managed Network File System
* note: NFS only works on Linux does NOT work on Windows
* NFS v4.1
* encryption at rest with KMS
* posix files system with standard (linux) file system api
* can attach to more than one EC2 instance
    * can be useful for autoscaling or load balancing etc.

#### Price
* more expensive than EBS
    * EFS: pay per GB used 
        * $0.30 per GB per month (varies by region) USED
    * EBS: pay per GB provisioned
        * $0.08 per GB per month provisioned

#### Scale
* scales automatically, pay per use, no capacity planning
* EFS Scale
    * 1000's of concurrent NFS clients
    * 10GB or more throughput
    * grow to petabyte sizre automatically
    * note throughput grows in size as more space utilized


#### Access
* EFS is region based and the same file system can attach to instances in different Zones
* attaches to one VPC with one mount target ENI per AZ
    * can have multiple AZ with an ENI in each AZ

* can access outside of it's VPC by VPC peering
* can access via on prem via direct connect or VPN

* important: when mounting from on prem MUST USE IPv4 NOT DNS
    * use ENI IP

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
        * Multiple AZ-(11 9s durability across multiple AZs)
        * Higher cost compared to other storage classes due to frequent access optimization.
        * Designed for frequently accessed data with high durability and low latency.
    * IA (infrequent access)
        * A lower-cost storage class for infrequently accessed data.
        * Suitable for data that requires high durability but is accessed less frequently.
        * good for Backup and disaster recovery or archiving
        * Multiple AZ-(11 9s durability across multiple AZs)
        * lower base cost but includes a per-GB retrieval fee when data is accessed.
    * One Zone/One Zone IA
        * same performance but less durability
        * 99.9% (3 9s), as it relies on a single AZ.
        * more affordable
        * Non-critical workloads with low durability requirements.
        * IA option allows reducing costs even further 
    * Amazon EFS offers lifecycle policies to automatically move data between storage classes, optimizing cost
        * i.e. if a file hasn't been accessed in >60 days will move to IA


#### Permissions
* can control access to the files via IAM

* Access Points
    * When multiple applications share the same EFS file system, access points can isolate them by defining separate root directories and POSIX identities.
    * application-specific entry points to an EFS file system
    * configure a specific user ID (UID) and group ID (GID) for applications accessing the file system through the access point.
    * Applications or clients mount the file system using the access point’s unique Access Point ID.
```
    sudo mount -t nfs4 -o nfsvers=4.1 \ fs-12345678.efs.region.amazonaws.com:/access-point-id /mnt
```
    * can also configure a default directory as the root directory 
    * can restrict access for clients using IAM policies
        * in IAM can configure what a client can access on an NFS file system
    * example:
        * can set a client uid/gid as 1001/1001 and only allow access to the /config directory
        * can set different client uid/gid to 1002/1002 and only allow access to /www directory

* File System Policies
    * these are IAM rules the you set ON THE FILE SYSTEM
        * restrict/allow access to other accounts, VPC's, specific IAM users, etc.
        * restrict/allow what these entities can do on the file system as well
    * apply access control rules to the entire EFS file system. 
    * by default it grants full access to all clients
    * They are similar to resource-based policies in AWS 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/EFSAccessRole"
      },
      "Action": [
        "elasticfilesystem:ClientMount",
        "elasticfilesystem:ClientWrite"
      ],
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-west-2"
        }
      }
    }
  ]
}
```

#### Cross Region Replication
* can replicat objects from one EFS file system to another regions EFS file system
* can replicate and setup new FS or replicate to existing FS
* Has RPO/RTO 
* doesn't use the EFS throughput, happens separately
* 