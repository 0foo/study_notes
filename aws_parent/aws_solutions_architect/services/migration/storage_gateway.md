
* USE CASE: provide NFS/SMB interface for on-prem or VPC hosts
* Also can cache locally either hot cache or entire s3 backend


* File Gateway: each file is a separate S3 object.
  * File path = S3 object key.
  * Metadata stored as object metadata.

* Volume Gateway: block storage backed by S3.
  * Data written as iSCSI block volumes.
  * Snapshots stored in S3 as EBS snapshots.
  * can't recover individual files without restoring entire volume

* Tape Gateway: virtual tapes stored in S3/Glacier.
  * Emulates tape libraries for backup apps.
  * Tapes are stored as virtual tape objects in S3.
  * can't recover individual files without restoring entire volume



### S3 File gateway
* USE CASE: mount S3 as file systems on prem
* can use with any storage class but glacier
* NFS or SMB integration
* can define IAM roles 
* can still define life cycle policy and intelligent tiering like any s3 bucket 
    * since still backed by an s3 bucket
* SMB protocol will allow use of AD for user auth and access control


### FSx File gateway
* discontinued 
* FSx for windows is already mountable natively
* the only advantage is a local cache in on-prem environment to give you low latency access


### Volume gateway
* USE CASE: backup volumes of on premise server
* Block storage using the iSCSI protocol backed by S3
* backed by EBS snapshots for backup/restore ON PREM
* two type:
    1. low latency - has a cache for most recent files on prem
    2. stored volume - entire dataset on premesis, with scheduled backup to s3



### Tape gateway
* USE CASE: backup tape library to the cloud
* backs up using iSCSI interface
* works with leading software vendors
* can store in s3 and/or glacier


### Gateways
* theres a software appliance you can run as a VM
* there's a hardware appliance you can get from AWS also
    * primarily if you don't have virtualization on premesis
* works with all of the gateways
* goes in a rack
* helpful for daily NFS backups in small data centers



### Useful architectures
* can host a gateway on-prem and one in AWS VPC and both attached to same s3 bucket
    * useful for migrating applications to the cloud

* can mount same bucket in differnt locations as a shared file system

* can still use FULL s3 funcitonality with storage gateway   
    * lambda events
    * analytics with: athena, redshift spectrum, EMR
    * cross region replication for backup
    * any other s3 functionality available in AWS
    * backup 
    * lifecycle policies - to move data to lower cost storage

* Read only replicas - can connect it to some server which writes to cloud and enable read only so that anything else mounting that bucket will not works

* versioning
    * can enable versioning for restore of earlier version of data
    * restore entire file system to previous version!
    * will need to trigger a sync locally!!!

* enable s3 object lock
    * WORM - write once read many
    * always creates a new version for any change that way will never lose any data