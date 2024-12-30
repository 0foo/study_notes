* launch 3rd party file systems as FULLY MANAGED service
    * lustre
    * windows file server
    * OpenZFS
    * NetApp ONTAP

* AWS fully manages the infrastructure, scaling, and maintenance, freeing you from managing your own ZFS servers.
* Seamless integration with AWS services like AWS Backup, AWS DataSync, and CloudWatch.


#### FSx for Windows File Server 
* fully managed
* supports SMB and NTFS, Active Directory, ACL's, user quotas
* can also be mounted on EC2 Linux instances
* supports microsoft distributed file system (DFS) namespaces(group files across multiple file systems)
* can use
    * SSD (faster)
    * HDD (cheaper)
* access from on pre using VPN or Direct Connect
* can be multi AZ for high availability
* data backed up daily to S3 for disaster recovery via scripts(no native integration with S3)
* no point in time instant cloning



#### FSx for Lustre
* disributed file system for large scale computing
* lustre = linux cluster
* Machine learning and HPC (high performance computing)
* storage
    * SSD - low latency, small 
    * HDD - thoughput intensive workloads
* seamless native integration with S3
    * can READ/WRITE S3 as a file system
    * can write result of computation back to S3
* no point in time instant cloning

* deployment options
    * scratch file system
        * temporary storage
        * only a single copy of file system, data is not replicated
        * faster: 6 times the performance of persistent FS
        * cheaper
        * uses: short term processing, cheap

    * persistent file system
        * long term storage
        * replicated in same AZ
            * files replaced within minutes
        * use case: long term processing, sensitive data

* data lazy loading
    * When you link an Amazon S3 bucket to an FSx for Lustre file system (using the ImportPath parameter), only the metadata about the files in the S3 bucket is loaded into the Lustre file system.
    * The actual file content is fetched from the S3 bucket only when the file is accessed for the first time (e.g., read or write operations).
    * Once fetched, the file data is cached in the Lustre file system for subsequent access.
    * if have all data in S3 
    * can start data processing right away without the full dataset being brought into lustre
    * only the data currently being processed is brought over to the Lustre FS
    * reduces transfer costs out of S3
    * eseentially lustre is a durable cache

#### FSx for NetApp ONTAP
* compatible with NFS, SMB, iSCSI protocol
* use cases: used for workloads that are already running ONTAP or NFS
* very broad compatibility
    * works with windows, linux, mac, essentially any OS
* autoscaling- storage shrinks/grows automatically
* snapshots, replication, low-cost, compression, can do data de-duplication(find duplicates fo files)
* point in time instant cloning 
    * nice for testing new ideas: can clone an FS and now have a staging file system for a new direction
* main use case: move workloads running on ONTAP to AWS

#### FSx for OpenZFS
* compatible with NFS
* main use case: move workloads running on ZFS to AWS
* broad compatibility (linux, mac, windows)
* snapshot, compression, low cost, (no data deduplication)
* point in time instant cloning
