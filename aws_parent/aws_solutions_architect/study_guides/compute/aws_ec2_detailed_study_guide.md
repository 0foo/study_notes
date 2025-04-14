## EC2

Amazon EC2 (Elastic Compute Cloud) provides scalable virtual servers in the cloud. For the AWS Solutions Architect exam, you need to know the following in depth:

### Instance Types
* General Purpose (e.g., t3, t3a, m5) – balanced compute/memory/network
* Compute Optimized (e.g., c5, c6g) – high-performance CPUs
* Memory Optimized (e.g., r5, x1e) – for memory-intensive workloads
* Storage Optimized (e.g., i3, d2) – high disk throughput
* Accelerated Computing (e.g., p3, inf1) – GPU and FPGA for ML/HPC

### Instance Lifecycle States
* Pending – instance is launching
* Running – instance is active
* Stopping/Stopped – can be restarted with same data/volume
* Terminated – permanently deleted

### Pricing Models
* On-Demand – pay by second/hour, no commitment
* Reserved Instances (Standard/Convertible) – 1-3 year terms, significant discount
* Spot Instances – use unused capacity for up to 90% off
* Dedicated Hosts – physical servers for compliance/license-bound workloads
* Savings Plans – flexible pricing model applied across instance families

### EBS (Elastic Block Store)
* Attached volumes for EC2 instances
* Types: gp3, gp2 (SSD), io1/io2 (high-performance), st1/sc1 (HDD)
* Snapshots for backups, cross-region copy, encryption support
* Can be encrypted with KMS
* Root volume deletion behavior configurable

### Placement Groups
* Cluster – same AZ, low latency/high throughput (for tightly coupled apps)
* Spread – separate hardware, high availability (max 7 instances per AZ)
* Partition – separate partitions (useful for large-scale distributed systems)

### AMIs (Amazon Machine Images)
* Templates for launching EC2 instances
* Include OS, packages, data, and launch permissions
* Can be copied across regions
* Public, private, or AWS Marketplace

### Auto Scaling
* Maintain desired number of EC2 instances
* Scaling policies:
  - Target tracking (e.g., keep CPU at 50%)
  - Step scaling (scale based on CloudWatch alarms)
  - Scheduled scaling (scale on a timetable)
* Launch templates used for defining instance config
* Lifecycle hooks allow actions during scale-in/scale-out

### EC2 Metadata & IAM Roles
* Instance metadata (e.g., IP, hostname, IAM role) accessible at: `http://169.254.169.254`
* Roles provide credentials to applications without hardcoding keys
* IAM roles for EC2 should have least-privilege permissions

### EC2 Security
* Use security groups (virtual firewalls) – stateful
* Use key pairs (public/private keys) for SSH access
* Use NACLs (stateless) for subnet-level control
* Terminate protection and root EBS volume delete flag are common exam traps

### Networking
* Elastic IPs – static public IPs for EC2
* ENIs – Elastic Network Interfaces, can be attached/detached
* Use multiple ENIs for high availability or multi-subnet access

### Monitoring & Maintenance
* Use CloudWatch for CPU, disk, and network monitoring
* Use AWS Systems Manager for patching, automation, and access
* Reboot vs stop/start vs terminate – know behavioral differences