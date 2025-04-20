* network attached 
* elastic block store
* resizable
* attached to an ZONE (not VPC or region)
    * You cannot attach an EBS volume directly to an EC2 instance in a different AZ. To move an EBS volume across AZs, you need to create a snapshot of the volume and then restore it in the desired AZ.

* can pick an instance that is EBS optimized for maximum throughput if need to heavily use EBS


* EBS volume types
    * gp2/gp3
        * SSD
        * g = general purpose, balance price/performance
    * io1/io2
        * SSD
        * e = extreme performance, low latency, high through put
    * st1   
        * low cost HDD for normal use
    * sc1
        * low cost HDD for cold storage for less frequent access

* Only GP and IO series can be used as boot operation

* EBS vols are charachterize by: 
    * Size
    * Throughput
    * IOPS
    


#### Snapshots
    * incremental- will only backup changes from past snapshot
    * EBS backups will share the same IO as the actual workload/connection to the instance, so may get slowness during backup
    * store in S3, but you won't see t
    * Not necessary to detach volume to do back BUT RECCOMENDED
        * if volume is being used during back up you may get inconsistent state
    * Can copy a snapshot across region

* Snapshot -> AMI
    * can make an AMI out of your snapshot
    * can build an service and then make an AMI out of it 

* * How snapshots work at a data level
    * When restoring from a snapshot, an EBS volume goes through two phases:

    * Provisioning:
        * The volume is created and immediately available for attachment to an EC2 instance.

    * Lazy Loading:
        * As blocks are needed they are fetched from s3 and stored permanantly in EBS


* Warmup: EBS volumes restored from a snapshot will need to be pre-warmed
    * They will need to have all of their blocks loaded from s3 otherwise the default will be to lazy load a block at a time
    * 2 ways:
        * Fast Snapshot Restore: will read all blocks from s3
        * fio/dd commands 


#### Data life cycle manager  DLCM (Automation)
* can automate retention, creation
* can schedule backups/ cross-account, etc.
* use resource tags to identify the resources
    * i.e. prod, dev, test, etc
* NOTE: EVERYTHING HAS TO BE WITHIN DLCM
    * Can't work with one offs or anythign created outside OF DLCM
* Can't be used to manaage instance store backed AMI because it's not on the EBS infrastructure and is on the host machine rack
* DLCM va AWS backup
    * DLCM: creation, retention, deletion of EBS snapshots
    * AWS backup: 
        * a generic backup service for all service in AWS
        *  superset of DLCM, has DLCM plus every other service,

#### Encryption
    * 'Always encrypt new volumes'
        * per region setting to encrypt all of your volumnes in the region
    * by default EBS volumes are NOT encryptied

#### EBS multi-attach
    * for io volumes only
    * can attach same EBS volume to multiple instance in same AZ
    * full read/write for all attached instances to the vol
    * file system not normal XFS or EXT, it's a cluster aware file system


#### Local EC2 instance store
