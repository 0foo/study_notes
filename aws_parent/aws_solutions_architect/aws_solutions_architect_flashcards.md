# AWS Solutions Architect Exam Flashcards


## Compute

* **What is EC2 and what should you know for the exam?**
  * Elastic Compute Cloud. Understand instance types, pricing models (on-demand, reserved, spot), placement groups, autoscaling, EBS attachment, and use cases.
* **What is Lambda and what should you know for the exam?**
  * Serverless compute. Know invocation types (sync/async), event sources (S3, API Gateway, EventBridge, etc.), execution limits, concurrency, cold starts, and deployment with versions/aliases.
* **What is Auto Scaling Group (ASG) and what should you know for the exam?**
  * Automatically adjust EC2 capacity. Learn launch templates, scaling policies (target tracking, step, scheduled), lifecycle hooks, and cooldown periods.
* **What is AWS Batch and what should you know for the exam?**
  * Run batch computing workloads. Understand compute environments, job queues, integration with EventBridge and Step Functions.
* **What is ECS and what should you know for the exam?**
  * Managed container orchestration. Know difference between EC2 and Fargate launch types, task definitions, and service auto-scaling.
* **What is Fargate and what should you know for the exam?**
  * Serverless containers. Understand billing based on vCPU/memory, IAM roles for tasks, and use cases for decoupled services.
* **What is Elastic Beanstalk and what should you know for the exam?**
  * PaaS for applications. Know environment types (web/worker), supported stacks, and deployment policies.
* **What is AWS Outposts and what should you know for the exam?**
  * Extend AWS infrastructure to on-prem. Useful for low-latency workloads and data residency requirements.
* **What is AWS Local Zones and what should you know for the exam?**
  * Run latency-sensitive workloads closer to users. Important for hybrid and edge use cases.

## Storage

* **What is S3 and what should you know for the exam?**
  * Object storage. Understand durability, lifecycle policies, versioning, storage classes (Standard, IA, Glacier), pre-signed URLs, and encryption (SSE-S3, SSE-KMS).
* **What is Amazon EFS and what should you know for the exam?**
  * Managed NFS file system. Good for shared access, scalable throughput, and Linux-based workloads.
* **What is Amazon FSx and what should you know for the exam?**
  * Managed Windows File Server or Lustre. Key for Windows-based applications or high-performance computing.
* **What is AWS Backup and what should you know for the exam?**
  * Central backup management. Know backup vaults, plans, and integration with EFS, EC2, RDS, etc.
* **What is AWS Snow Family and what should you know for the exam?**
  * Physical devices for edge compute or offline data transfer. Know Snowcone, Snowball Edge, and Snowmobile.

## Database

* **What is RDS and what should you know for the exam?**
  * Managed relational DB. Learn Multi-AZ deployments, read replicas, backups, failover, and supported engines (MySQL, PostgreSQL, Oracle, etc.).
* **What is DynamoDB and what should you know for the exam?**
  * NoSQL key-value and document DB. Study provisioned vs on-demand capacity, global tables, DAX caching, and backup/restore.
* **What is Amazon Aurora and what should you know for the exam?**
  * High-performance MySQL/PostgreSQL compatible DB. Understand auto-scaling, serverless, replication, and fault tolerance.
* **What is Timestream and what should you know for the exam?**
  * Time series database. Use cases include IoT and application monitoring. Know storage tiers and query model.
* **What is DocumentDB and what should you know for the exam?**
  * MongoDB-compatible document DB. Managed service for JSON workloads.

## Networking & Content Delivery

* **What is VPC and what should you know for the exam?**
  * Virtual network. Understand subnets, route tables, NAT, gateways, security groups, and NACLs.
* **What is NAT Gateway and what should you know for the exam?**
  * Provides internet access to private subnets. Know cost model and alternatives like NAT instances.
* **What is Route 53 and what should you know for the exam?**
  * Scalable DNS. Study routing policies (simple, weighted, latency, failover, geolocation), health checks, and domain registration.
* **What is Global Accelerator and what should you know for the exam?**
  * Optimizes routing using Anycast IPs. Reduces latency for global applications.
* **What is CloudFront and what should you know for the exam?**
  * CDN for static/dynamic content. Learn origin configurations, signed URLs, and integration with S3 or ALB.
* **What is Elastic Load Balancing (ELB) and what should you know for the exam?**
  * Distributes traffic. Understand differences between ALB, NLB, CLB and their use cases.
* **What is AWS Transit Gateway and what should you know for the exam?**
  * Central hub for connecting VPCs and on-prem networks. Scales better than VPC peering.
* **What is AWS Direct Connect and what should you know for the exam?**
  * Private network link to AWS. Important for high throughput and low latency hybrid environments.

## Security, Identity, & Compliance

* **What is IAM and what should you know for the exam?**
  * Identity and access control. Understand roles, users, groups, policies (inline vs managed), and least privilege principles.
* **What is KMS and what should you know for the exam?**
  * Key Management Service. Use for encrypting data at rest/in transit, envelope encryption, and compliance requirements.
* **What is Secrets Manager and what should you know for the exam?**
  * Store and rotate secrets. Know difference from SSM Parameter Store and integration with RDS/Lambda.
* **What is Parameter Store and what should you know for the exam?**
  * Store config data and secrets. Supports versioning and encryption with KMS.
* **What is Shield and what should you know for the exam?**
  * DDoS protection. Standard is automatic; Advanced provides extra protection and response team.
* **What is AWS WAF and what should you know for the exam?**
  * Web Application Firewall. Protects against common web exploits. Can be attached to ALB, CloudFront, and API Gateway.
* **What is Firewall Manager and what should you know for the exam?**
  * Central management for WAF, Shield, and security groups.
* **What is Amazon Inspector and what should you know for the exam?**
  * Security assessment for EC2, Lambda. Scans for vulnerabilities and network exposure.
* **What is AWS Organizations and what should you know for the exam?**
  * Manage multiple AWS accounts. Know SCPs, consolidated billing, and account structure.
* **What is AWS Control Tower and what should you know for the exam?**
  * Preconfigured environment for setting up secure multi-account structure. Automates guardrails.

## Analytics & Big Data

* **What is Redshift and what should you know for the exam?**
  * Data warehouse. Learn distribution keys, sort keys, spectrum, and concurrency scaling.
* **What is Redshift Spectrum and what should you know for the exam?**
  * Query S3 data from Redshift. Scales compute separately for efficiency.
* **What is Athena and what should you know for the exam?**
  * Serverless querying for S3. Know supported formats, partitioning, and use with Glue Catalog.
* **What is QuickSight and what should you know for the exam?**
  * BI and dashboarding tool. Integrated with many AWS data sources. Understand SPICE engine.
* **What is EMR and what should you know for the exam?**
  * Managed Hadoop/Spark. Study use cases, cluster types, and cost-saving tips.
* **What is Kinesis Data Streams and what should you know for the exam?**
  * Real-time data ingestion. Learn partition keys, shards, and retention.
* **What is Kinesis Analytics (Flink) and what should you know for the exam?**
  * Stream processing with Apache Flink. Analyze real-time data from KDS or MSK.
* **What is Kinesis Firehose and what should you know for the exam?**
  * Ingest and deliver data to S3, Redshift, etc. Supports transformations with Lambda.
* **What is Amazon MSK and what should you know for the exam?**
  * Managed Kafka. Know broker configuration, storage, and consumer group behavior.
* **What is Amazon MQ and what should you know for the exam?**
  * Managed ActiveMQ/RabbitMQ. Used for legacy apps requiring open protocols.

## Application Integration

* **What is SQS and what should you know for the exam?**
  * Fully managed message queues. Know standard vs FIFO, DLQs, visibility timeout, and polling methods.
* **What is SNS and what should you know for the exam?**
  * Pub/sub messaging. Know topics, fan-out patterns, message filtering, and mobile push.
* **What is Step Functions and what should you know for the exam?**
  * Workflow orchestration. Standard vs Express workflows, integration with other AWS services.
* **What is EventBridge and what should you know for the exam?**
  * Event bus for decoupling services. Supports SaaS apps and custom events.
* **What is API Gateway and what should you know for the exam?**
  * Create, publish, and secure APIs. Understand throttling, caching, and usage plans.
* **What is AWS AppConfig and what should you know for the exam?**
  * Feature flag and config rollout. Useful for deploying new configurations safely.

## Developer Tools & DevOps

* **What is CodeDeploy and what should you know for the exam?**
  * Automated deployment service. Supports EC2, Lambda, ECS. Know blue/green and in-place strategies.
* **What is CodePipeline and what should you know for the exam?**
  * CI/CD orchestration. Integrates with CodeBuild, CodeDeploy, GitHub, etc.
* **What is CloudFormation and what should you know for the exam?**
  * IaC for AWS. Learn template syntax, parameters, mappings, conditions, and stack sets.
* **What is X-Ray and what should you know for the exam?**
  * Distributed tracing for debugging. Visualizes service map and latency bottlenecks.
* **What is CloudWatch and what should you know for the exam?**
  * Monitoring and observability. Learn logs, metrics, alarms, dashboards, and log insights.
* **What is CloudTrail and what should you know for the exam?**
  * Audit log of all AWS API calls. Important for security and compliance.

## Management & Governance

* **What is Systems Manager and what should you know for the exam?**
  * Operational management. Know SSM Agent, Patch Manager, Session Manager, and Parameter Store.
* **What is Trusted Advisor and what should you know for the exam?**
  * Gives recommendations on security, cost, performance, and service limits.
* **What is AWS Config and what should you know for the exam?**
  * Tracks configuration changes. Used for compliance auditing and drift detection.
* **What is AWS Budgets and what should you know for the exam?**
  * Create cost/usage alerts. Supports actions like stopping instances.
* **What is AWS Compute Optimizer and what should you know for the exam?**
  * Recommends optimal compute resources based on past usage.
* **What is AWS Cost Explorer and what should you know for the exam?**
  * Analyze and visualize cost and usage data over time.
* **What is AWS Service Catalog and what should you know for the exam?**
  * Manage approved IT products. Enforces governance on deployments.
* **What is AWS Resource Access Manager (RAM) and what should you know for the exam?**
  * Share AWS resources across accounts or within organizations.

## Machine Learning

* **What is SageMaker and what should you know for the exam?**
  * Build, train, and deploy ML models. Understand notebook instances, training jobs, and endpoints.
* **What is Amazon Macie and what should you know for the exam?**
  * Data security service for identifying PII in S3. Uses ML to classify and monitor data.
* **What is Amazon GuardDuty and what should you know for the exam?**
  * Threat detection using VPC flow logs, DNS, and CloudTrail.