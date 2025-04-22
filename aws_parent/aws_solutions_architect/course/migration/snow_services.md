* USE CASE 1: move large amounts of data
    * portable device to collect data at the edge and bring back into AWS
    * will recieve a device in the mail, you load, then ship back to AWS
    * secure
    * workaround for large datasets or slow connections
        * petabytes
    * rule of thumb -> if take longer than 1 week then use snowball

* USE CASE 2: process large amounts of data on the edge
    * truck on road, ship at sea, mining station underground, etc.
    * no or limited access to internet/compute power
    * snowball device has hundreds of gigs of ram and over 100 cpus
    * can run ec2 instance or lambda functions at the edge
    * preprocess data, machine learning, transcode media

### Improve transfer performance for snowfamily devices
* perform multiple write operations at one time - from multiple terminals
* transfer small files in batches - zip up small files together until at least 1MB
* don't perform operations on file during transfer
* reduce local network use
* eliminate uneccesary hops, plug directly to computer
* data transfer rate:
    * via file interface: 25 - 40 MB/s
    * via S3 adaptor for snowball: 250MB - 400MB /s
    

### Can integrate snowball and DMS
    * large data migrations may have TB to PB of data
    * Steps:
        1. use AWS SCT to extract data locally and move to an snowball edge device
        2. ship back to AWS
        3. AWS will load data into s3 
        4. DMS kicks in, takes the files from S3 and moves them to target data store
    * if use CDC (change data capture) any updates happening in on prem data source will be replicated over to the destination data store

