## EC2 - Deep Dive for AWS Solutions Architect Exam

Amazon EC2 (Elastic Compute Cloud) provides secure, resizable compute capacity in the cloud. It is a foundational AWS service, and understanding its full scope is essential for passing the Solutions Architect exam.

---

### Instance Types
EC2 offers several instance families to support different use cases. Each instance type has a combination of CPU, memory, storage, and networking capacity.

* **General Purpose**: Balanced resources, suitable for a wide range of applications. Examples: `t3`, `t3a`, `m5`.
* **Compute Optimized**: Ideal for compute-bound applications. Examples: `c5`, `c6g`. Use for batch processing, web servers, gaming servers.
* **Memory Optimized**: High RAM-to-vCPU ratio for memory-intensive workloads. Examples: `r5`, `x1e`. Use for in-memory databases, caching.
* **Storage Optimized**: Designed for workloads requiring high sequential read/write access to large datasets on local storage. Examples: `i3`, `d2`.
* **Accelerated Computing**: Use hardware accelerators such as GPUs or FPGAs for ML or HPC. Examples: `p3`, `inf1`.

---

### Instance Lifecycle States
* **Pending**: The instance is starting.
* **Running**: The instance is running and billing has started.
* **Stopping/Stopped**: The instance is shutting down or halted. You are not charged for stopped time (except for storage).
* **Shutting-down/Terminated**: The instance is being or has been deleted.

---

### Pricing Models
* **On-Demand**: Pay for compute capacity by the hour/second with no long-term commitments. Best for short-term, irregular workloads.
* **Reserved Instances**: 1 or 3 year commitment. Can choose standard (up to 72% discount) or convertible (change instance types).
* **Spot Instances**: Use unused capacity at a steep discount (up to 90%), but can be terminated with 2-minute warning.
* **Dedicated Hosts**: Physical servers for use with your account. Useful for license-bound or compliance workloads.
* **Savings Plans**: Flexible alternative to RIs, offering similar discounts with fewer restrictions.

---

### EBS (Elastic Block Store)
EBS provides persistent block storage volumes for EC2 instances.

* **Volume Types**:
  * `gp3/gp2` – general purpose SSDs
  * `io1/io2` – provisioned IOPS SSDs for high-performance applications
  * `st1/sc1` – throughput-optimized and cold HDDs for large, sequential workloads
* **Snapshots**: Point-in-time backups of volumes. Stored in S3. Can be encrypted and copied across regions.
* **Encryption**: Uses AWS KMS keys for data-at-rest encryption.
* **Volume Attachment**: Volumes can be attached to a single EC2 instance in the same AZ. Root volume behavior on termination can be modified.

---

### Placement Groups
Control how instances are placed within underlying hardware:

* **Cluster**: All instances in a single AZ on same rack – low latency/high bandwidth.
* **Spread**: Instances on distinct hardware – high availability; max 7 per AZ.
* **Partition**: Spread across logical partitions – good for HDFS, Kafka, Cassandra.
* **Default**: No placement group (random distribution for best fault tolerance). Your EC2 instances are placed randomly across the AWS infrastructure within the Availability Zone. You only use placement groups when your workload needs specific performance or availability characteristics.
---

### AMIs (Amazon Machine Images)
Templates used to launch EC2 instances.

* Contain OS, software, configurations.
* AMIs can be private, public, or from AWS Marketplace.
* Can be copied across regions and shared between accounts.
* Custom AMIs are useful for pre-configuring application environments.

---

### Auto Scaling
Auto Scaling ensures you always have the right number of EC2 instances.

* **Scaling Policies**:
  * Target tracking – e.g., keep CPU utilization at 50%
  * Step scaling – scale by steps based on CloudWatch alarms
  * Scheduled scaling – define capacity at fixed times
* **Lifecycle Hooks**: Pause instances during scale-out/in to perform custom actions.
* **Cooldowns**: Prevent unnecessary scaling actions by waiting after the last scale action.

---

### Instance Metadata & IAM Roles
* **Metadata**: Access internal instance data from `http://169.254.169.254/latest/meta-data/`
  * Includes instance ID, hostname, IPs, IAM role, etc.
* **IAM Roles**:
  * Assign IAM roles to EC2 to provide temporary credentials.
  * No hardcoded secrets. Used for S3, DynamoDB access, etc.
  * Least privilege principle applies.

---

### EC2 Security
* **Security Groups**: Stateful firewalls at instance level. Control inbound/outbound traffic by port, protocol, and IP.
* **NACLs**: Stateless firewalls at subnet level. Can deny traffic explicitly.
* **Key Pairs**: SSH access controlled with key pairs.
* **Termination Protection**: Prevent accidental termination.
* **Root Volume Deletion**: Can configure to retain root volume when instance is terminated.

---

### Networking
* **Elastic IPs**: Static public IPv4 addresses. One free when associated with running instance.
* **ENIs (Elastic Network Interfaces)**: Virtual NICs. Can move between instances.
* **Multiple ENIs**: Used for high availability or separating traffic across subnets.

---

### Monitoring & Maintenance
* **CloudWatch**: Monitor CPU, disk, and network. Create alarms to automate actions.
* **Systems Manager**: Run commands on EC2 without SSH. Includes Session Manager, Patch Manager, and Automation.
* **Reboot vs Stop/Start vs Terminate**:
  * Reboot: Soft reset, retains data and IP.
  * Stop/Start: New underlying hardware, same data (EBS); public IP may change.
  * Terminate: Deletes instance and attached volumes (if not preserved).