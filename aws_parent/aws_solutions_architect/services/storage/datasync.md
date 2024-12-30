* use case:
    * syncronize data
    * move large amount of data from one place to another

* move from:    
    * on prem <-> AWS
    * other cloud <-> AWS
    * AWS <-> AWS
    * will sync in either direction

* agent 
    * If on prem or another cloud, will need to install the datasync agent!!!
    * AWS -> AWS no agent needed
    * will give the datasync agent connection info to data sync service 
        * then configure inside of datasync where to send the data from there

* services can sync to in AWS
    * s3 (ANY STORAGE CLASS)
    * EFS
    * FSx

* replication can be hourly, weekly, daily

* File permisssion and metadata are preserved (NFS/POSIX, SMB)

* one agent task can use up to 10 GBps
* can setup a bandwidth limit


* If don't have network bandwidth to sync the data
    * will need to use AWS Snowcone device
    * Snowcone device has the agent preinstalled
    * I.E. sync data to snow cone
    * transport snowcone to AWS sync data from snowcone

* sync between different AWS storage services (s3, EFS, FSx)


* the data is diffed after initial copy is made

* can transfer live data
    * DataSync supports transferring files even when they are being read or written by your applications.
    * During incremental transfers, it only copies changed or new files after the initial transfer, minimizing disruptions.

* transfer options:
    * can have a public VIF directly to datasync via public internet
    * or can go through direct connect private VIF into a VPC and use a VPC private endpoint interface