# AWS Solutions Architect Study Guide


## Compute

* **EC2**: Elastic Compute Cloud. Understand instance types, pricing models (on-demand, reserved, spot), placement groups, autoscaling, EBS attachment, and use cases.
* **Lambda**: Serverless compute. Know invocation types (sync/async), event sources (S3, API Gateway, EventBridge, etc.), execution limits, concurrency, cold starts, and deployment with versions/aliases.
* **Auto Scaling Group (ASG)**: Automatically adjust EC2 capacity. Learn launch templates, scaling policies (target tracking, step, scheduled), lifecycle hooks, and cooldown periods.
* **AWS Batch**: Run batch computing workloads. Understand compute environments, job queues, integration with EventBridge and Step Functions.
* **ECS**: Managed container orchestration. Know difference between EC2 and Fargate launch types, task definitions, and service auto-scaling.
* **Fargate**: Serverless containers. Understand billing based on vCPU/memory, IAM roles for tasks, and use cases for decoupled services.
* **Elastic Beanstalk**: PaaS for applications. Know environment types (web/worker), supported stacks, and deployment policies.
* **AWS Outposts**: Extend AWS infrastructure to on-prem. Useful for low-latency workloads and data residency requirements.
* **AWS Local Zones**: Run latency-sensitive workloads closer to users. Important for hybrid and edge use cases.

## Storage

* **S3**: Object storage. Understand durability, lifecycle policies, versioning, storage classes (Standard, IA, Glacier), pre-signed URLs, and encryption (SSE-S3, SSE-KMS).
* **Amazon EFS**: Managed NFS file system. Good for shared access, scalable throughput, and Linux-based workloads.
* **Amazon FSx**: Managed Windows File Server or Lustre. Key for Windows-based applications or high-performance computing.
* **AWS Backup**: Central backup management. Know backup vaults, plans, and integration with EFS, EC2, RDS, etc.
* **AWS Snow Family**: Physical devices for edge compute or offline data transfer. Know Snowcone, Snowball Edge, and Snowmobile.

## Database

* **RDS**: Managed relational DB. Learn Multi-AZ deployments, read replicas, backups, failover, and supported engines (MySQL, PostgreSQL, Oracle, etc.).
* **DynamoDB**: NoSQL key-value and document DB. Study provisioned vs on-demand capacity, global tables, DAX caching, and backup/restore.
* **Amazon Aurora**: High-performance MySQL/PostgreSQL compatible DB. Understand auto-scaling, serverless, replication, and fault tolerance.
* **Timestream**: Time series database. Use cases include IoT and application monitoring. Know storage tiers and query model.
* **DocumentDB**: MongoDB-compatible document DB. Managed service for JSON workloads.

## Networking & Content Delivery

* **VPC**: Virtual network. Understand subnets, route tables, NAT, gateways, security groups, and NACLs.
* **NAT Gateway**: Provides internet access to private subnets. Know cost model and alternatives like NAT instances.
* **Route 53**: Scalable DNS. Study routing policies (simple, weighted, latency, failover, geolocation), health checks, and domain registration.
* **Global Accelerator**: Optimizes routing using Anycast IPs. Reduces latency for global applications.
* **CloudFront**: CDN for static/dynamic content. Learn origin configurations, signed URLs, and integration with S3 or ALB.
* **Elastic Load Balancing (ELB)**: Distributes traffic. Understand differences between ALB, NLB, CLB and their use cases.
* **AWS Transit Gateway**: Central hub for connecting VPCs and on-prem networks. Scales better than VPC peering.
* **AWS Direct Connect**: Private network link to AWS. Important for high throughput and low latency hybrid environments.

## Security, Identity, & Compliance

* **IAM**: Identity and access control. Understand roles, users, groups, policies (inline vs managed), and least privilege principles.
* **KMS**: Key Management Service. Use for encrypting data at rest/in transit, envelope encryption, and compliance requirements.
* **Secrets Manager**: Store and rotate secrets. Know difference from SSM Parameter Store and integration with RDS/Lambda.
* **Parameter Store**: Store config data and secrets. Supports versioning and encryption with KMS.
* **Shield**: DDoS protection. Standard is automatic; Advanced provides extra protection and response team.
* **AWS WAF**: Web Application Firewall. Protects against common web exploits. Can be attached to ALB, CloudFront, and API Gateway.
* **Firewall Manager**: Central management for WAF, Shield, and security groups.
* **Amazon Inspector**: Security assessment for EC2, Lambda. Scans for vulnerabilities and network exposure.
* **AWS Organizations**: Manage multiple AWS accounts. Know SCPs, consolidated billing, and account structure.
* **AWS Control Tower**: Preconfigured environment for setting up secure multi-account structure. Automates guardrails.

## Analytics & Big Data

* **Redshift**: Data warehouse. Learn distribution keys, sort keys, spectrum, and concurrency scaling.
* **Redshift Spectrum**: Query S3 data from Redshift. Scales compute separately for efficiency.
* **Athena**: Serverless querying for S3. Know supported formats, partitioning, and use with Glue Catalog.
* **QuickSight**: BI and dashboarding tool. Integrated with many AWS data sources. Understand SPICE engine.
* **EMR**: Managed Hadoop/Spark. Study use cases, cluster types, and cost-saving tips.
* **Kinesis Data Streams**: Real-time data ingestion. Learn partition keys, shards, and retention.
* **Kinesis Analytics (Flink)**: Stream processing with Apache Flink. Analyze real-time data from KDS or MSK.
* **Kinesis Firehose**: Ingest and deliver data to S3, Redshift, etc. Supports transformations with Lambda.
* **Amazon MSK**: Managed Kafka. Know broker configuration, storage, and consumer group behavior.
* **Amazon MQ**: Managed ActiveMQ/RabbitMQ. Used for legacy apps requiring open protocols.

## Application Integration

* **SQS**: Fully managed message queues. Know standard vs FIFO, DLQs, visibility timeout, and polling methods.
* **SNS**: Pub/sub messaging. Know topics, fan-out patterns, message filtering, and mobile push.
* **Step Functions**: Workflow orchestration. Standard vs Express workflows, integration with other AWS services.
* **EventBridge**: Event bus for decoupling services. Supports SaaS apps and custom events.
* **API Gateway**: Create, publish, and secure APIs. Understand throttling, caching, and usage plans.
* **AWS AppConfig**: Feature flag and config rollout. Useful for deploying new configurations safely.

## Developer Tools & DevOps

* **CodeDeploy**: Automated deployment service. Supports EC2, Lambda, ECS. Know blue/green and in-place strategies.
* **CodePipeline**: CI/CD orchestration. Integrates with CodeBuild, CodeDeploy, GitHub, etc.
* **CloudFormation**: IaC for AWS. Learn template syntax, parameters, mappings, conditions, and stack sets.
* **X-Ray**: Distributed tracing for debugging. Visualizes service map and latency bottlenecks.
* **CloudWatch**: Monitoring and observability. Learn logs, metrics, alarms, dashboards, and log insights.
* **CloudTrail**: Audit log of all AWS API calls. Important for security and compliance.

## Management & Governance

* **Systems Manager**: Operational management. Know SSM Agent, Patch Manager, Session Manager, and Parameter Store.
* **Trusted Advisor**: Gives recommendations on security, cost, performance, and service limits.
* **AWS Config**: Tracks configuration changes. Used for compliance auditing and drift detection.
* **AWS Budgets**: Create cost/usage alerts. Supports actions like stopping instances.
* **AWS Compute Optimizer**: Recommends optimal compute resources based on past usage.
* **AWS Cost Explorer**: Analyze and visualize cost and usage data over time.
* **AWS Service Catalog**: Manage approved IT products. Enforces governance on deployments.
* **AWS Resource Access Manager (RAM)**: Share AWS resources across accounts or within organizations.

## Machine Learning

* **SageMaker**: Build, train, and deploy ML models. Understand notebook instances, training jobs, and endpoints.
* **Amazon Macie**: Data security service for identifying PII in S3. Uses ML to classify and monitor data.
* **Amazon GuardDuty**: Threat detection using VPC flow logs, DNS, and CloudTrail.