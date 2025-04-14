# AWS Solutions Architect Exam Flashcards (Rewritten with Direct Facts)


## Compute

* **What is EC2 and what do you need to know for the exam?**
  * EC2 provides resizable compute capacity. You need to know instance families (e.g., t3, m5, c5), pricing models (on-demand, reserved, spot), security groups, EBS volumes, placement groups, and auto-scaling setup.
* **What is Lambda and what do you need to know for the exam?**
  * Lambda runs code without provisioning servers. You need to know memory/timeout limits, concurrency (reserved/provisioned), supported runtimes, event sources (e.g., S3, API Gateway), and cold start implications.
* **What is Auto Scaling Group (ASG) and what do you need to know for the exam?**
  * ASGs manage EC2 scaling. You need to know how to configure launch templates, scaling policies (target tracking, step), lifecycle hooks, and health checks.

## Storage

* **What is S3 and what do you need to know for the exam?**
  * S3 is object storage. You need to know storage classes (Standard, IA, Glacier), lifecycle rules, bucket policies vs ACLs, pre-signed URLs, server-side encryption options (SSE-S3, SSE-KMS), and versioning.
* **What is Amazon EFS and what do you need to know for the exam?**
  * EFS is a scalable file system. You need to know it's NFS-based, supports concurrent EC2 access, and has throughput/performance modes (burst, provisioned).

## Database

* **What is RDS and what do you need to know for the exam?**
  * RDS is a managed relational database. You need to know supported engines (MySQL, PostgreSQL, etc.), Multi-AZ vs read replicas, backup retention, failover behavior, and pricing tiers.
* **What is DynamoDB and what do you need to know for the exam?**
  * DynamoDB is a NoSQL key-value store. You need to know table structure (partition/sort keys), capacity modes (provisioned vs on-demand), DAX caching, global tables, and TTL.

## Networking

* **What is VPC and what do you need to know for the exam?**
  * VPC is your virtual network. You need to know CIDR blocks, subnets (public/private), routing tables, IGWs, NAT Gateways, security groups vs NACLs, and peering.
* **What is Route 53 and what do you need to know for the exam?**
  * Route 53 is a DNS service. You need to know record types (A, CNAME, Alias), routing policies (simple, weighted, latency, geolocation), and health checks.