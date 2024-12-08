* types: R(RAM),C(CPU),M(Medium/balance),I(I/O),G(GPU), T2,T3(burstable), T2/T3 unlimited(unlimited burst)


* placement groups
    * by default when launch an instance it's placed randomly 
    * strategies
        * spread: 
            * each instance is on different hardware on different racks with separate power/network
            * can span across different AZ's
            * reduce risk of failure
            * limited to 7 instances per AZ per placement group
            * intended for workloads with critical uptimes: Database nodes, caching layers, or critical services with strict uptime requirements.
        * Partition: spreads across many partitions which are separate racks
            * all the instances are grouped into partitions
            * 7 partitions per AZ
            * EC2 metadata service can give the instance access to which partition they belong to
            * if the instance count is equal to or less than the number of partitions, each partition will host one instance, then it will try to even balance when instances exceed partitions
            * each partition is a groups of racks with dedicated power/networking that aren't shared with other partiitons
            * intended for large-scale distributed systems(hadoop, cassandra, Kafka, etc)
            * sort of a less robust spread strategy
        * cluster
            * all instances on same rack in same AZ 
            * this gives low latency, high bandwidth (10G between instances) 
            * if the rack fails ALL instances fail
            * choose instance type with enhanced networking for the speed
            * types of uses: big data job that needs to complete fast or application that needs low latency
    * can change an instances placement group, (very important to know)
        * have to stop instance
        * use CLI (modify-instance-placemenbt)
        * start instance

* ways to launch instances
    * on demand: short workload, predicatable pricing, reliable
    * spot: 
        * short workloads, cheap, can lose instances (not reliable), 
        * good if app is reslient to failure
        * no discount
    * reserved: 
        * purchase then for minimum of 1 year
        * high discount
        * long workloads
    * convertible reserved
        * long workloads 
        * will allow to convert instance type
        * middle discount
    * dedicate instances
        * no other customer will share your hardware
    * dedicated host
        * books entire physical server
        * great for software licences that operate on a per core basis that might not work on a virtualized instance
        * host affinity so that instance reboots are kept on the same host


* EC2 Graviton processor
    * delivers the best price performance
    * many OS support it NOT WINDOWS
    * Gravitron 2: 40% price improvment over 5th gen x86 instances
    * Graviton 3: 3x better performance 


* Metrics
    * CPU utilization + Credit Usage/Balance
    * Network: Network in.out
    * Status check
        * instance status: status of the VM
        * system status: status of the underlying hardware host
    * Disk
        * read/write for ops/bytes 
    * RAM NOT INCLUDED IN METRICS
        * Have to push from instance to cloudwatch as a custom metric

* EC2 Instance recovery
    * recover instance if the two status checks fail
    * EC2 monitored by Cloudwatch alarm with StatusCheckFailed_System alarm
    * there is an action called "EC2 instance recovery" to recover that is triggered by the cloudwatch alarm
    * this recovery will keep: IP's(private, public, elastic), metadata, placement group
    * cloudwatch can alert an SNS topic to let you know failure/recovery/whatever



#### High performance computing(HPC)
* HPC
    * cloud greatly enables this
    * can build a big multi instance infrastructure and destroy when done
    * limits cost to what we used
    * can expand to as much as have money for and quickly

* AWS direct connect 
    * Direct connect hardline to on prem 
    * allows to move a lot of data into AWS
    * very secure

* Snowball
    * Move Petabytes of data to cloud

* Datasync
    * move large amount of data between on prem and S3, EFS, FSx for Windows

* HPC compute(CPU)
    * computer/network optimized
    * spot instances/spot fleet for cost savings and also autoscaling
    * if instances need to talk to each other, put them in a cluster placement group for speedy connection

* HPC neworking
    * the instance type determines the network speed!
    * attach an ENI to connect the instance to the VPC network(not this is simply an interface and has nothing to do with speed)
    * Instances with ENA or Intel 82599 VF (Virtual Function) support enhanced networking, enabling high-speed, low-latency connections.
    * Elastic network adaptor(ENA) up to 400Gigs
    * ENA used specifically for High Performance Networking
    * alternative to using ENA is using an Intel networking hardware but only up to 10 gigs-LEGACY
    * Elastic Fabric Adaptor
        * Improved enhanced networking fast!
        * great for inter-node comms/tightly coupled workloads
        * uses message passing interface standard(MPI)
        * bypasses the underlying Linux OS to provide low-latency reliable transport
    * EC2 enhanced networking (SR-IOV), higher bandwidth/lower latency


* Be able to differentiate between ENA or EFA or ENI


* HPC storage
    * how to store HPC data
    * attached directly to instance
        * EBS(256,000 iops with io2 block eexpress)
        * instance store: scale to millions of IOPS, linked to EC2 instance on hardware, low latency
    * network storage
        * S3 
        * basic EFS: scales iops based on total size of file system
            * can also use provisioned iops 
        * Amaaon FSx for Lustre
            * HPC optimized distributed file system
            * million of IOPS
            * in backend it's backed by S3

* HPC automation and orchestration
    * AWS Batch
        * supports multi-node parrallel jobs 
        * this enables run single jobs that span multiple instances
        * easily shcedule jovs and launch instance accordingly
    * AWS Parallel Cluster
        * open source cluster management tool to deploy HPC on AWS
        * Configure with text files
        * automate creation of VPC, Subnet, cluster type, and instance types


#### Spot Instance
* get discount up to 90% compared to demand
* define your max spot price(mxp) and while current spot price(csp) < your max spot price(msp) you will get the instance
* hourly CSP varies by capacity and offer
* if CSP is greater than your MSP then you have a 2 minute grace period to stop/terminate your instances
* great for batch jobs, data analysis, failure resistant workloads
* do not use for critical apps or databases because you can lose them quickly

#### Spot Fleets
* allow us to automatically request spot instances with the lowest price
* set of spot instances + optional on demand instances
* will try to meet target capacity with price constraints
* launch from launch pools
* define multiple launch pools and then AWS fleet will choose which one at the moment is best filled
* spot fleet keeps spinning up instances until reaches capacity or max cost
* spot fleet strategies:
    * lowestPrice: launch instances from the pool with lowest price
    * diversified: spot instances distributed amongst all the pools
    * capacityOptimized: pool with optimal capacity for the number of instances
    * priceCapacityOptimized: pools with highest capacity available then select pool with lowest price
        * this is best choice for most workloads