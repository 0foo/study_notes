# AWS Compute Services - Fully Fleshed Study Guide

## EC2
Amazon EC2 (Elastic Compute Cloud) provides resizable virtual machines. You need to know instance types (e.g., general purpose t3, compute-optimized c5, memory-optimized r5), instance lifecycle (pending, running, stopping, etc.), pricing models (on-demand, reserved, spot, dedicated hosts), placement groups (cluster, spread, partition), and how to use Auto Scaling. You also need to understand EBS volume attachment, AMI creation, and EC2 metadata/roles.

## Lambda
AWS Lambda is a serverless compute service that runs code in response to events. You need to know invocation types (synchronous via API Gateway, asynchronous via S3/EventBridge), timeouts (max 15 min), memory allocation (128MB–10GB), concurrency models (provisioned and reserved), cold start behavior, deployment versions and aliases, and integration with VPCs and layers. Know event sources such as S3, DynamoDB Streams, and CloudWatch Logs.

## Auto Scaling Group (ASG)
ASGs automatically manage EC2 fleet size based on demand. You need to know how to use launch templates/configurations, set up scaling policies (target tracking, step, scheduled), lifecycle hooks (pause instance during launch/terminate for custom actions), and cooldown periods to prevent excessive scaling.

## AWS Batch
AWS Batch manages batch computing jobs on AWS. You need to know job definitions, compute environments (Fargate or EC2), job queues, and array/multi-node parallel jobs. Understand how it integrates with EventBridge for scheduling and Step Functions for orchestration. Also know how AWS Batch determines optimal instance types and uses Spot instances for cost savings.

## ECS
Amazon ECS (Elastic Container Service) is a managed container orchestration platform. You need to understand task definitions, services, and clusters. Know the difference between launch types: EC2 (you manage EC2 instances) vs Fargate (AWS manages infra). Understand service discovery, IAM roles for tasks, and autoscaling with CloudWatch metrics.

## Fargate
AWS Fargate is a serverless compute engine for containers. You need to know that it removes the need to manage servers, supports ECS and EKS, is billed by requested vCPU and memory, and integrates with IAM for task roles. Great for decoupled microservices. No direct SSH access to Fargate tasks.

## Elastic Beanstalk
Elastic Beanstalk is a Platform as a Service (PaaS) for deploying web applications. You need to know environment types (web server and worker), supported platforms (Java, Node.js, Python, Docker, etc.), how Beanstalk wraps services like EC2, RDS, ELB, and ASG, and deployment methods (all-at-once, rolling, blue/green).

## AWS Outposts
AWS Outposts brings native AWS services to your on-premises datacenter. You need to know it's used for workloads needing low latency or local data processing. Supports EC2, EBS, RDS, and some container services. Managed from AWS console, monitored via CloudWatch.

## AWS Local Zones
Local Zones extend AWS infrastructure closer to users for ultra-low latency. You need to know that they support services like EC2, EBS, FSx, and Elastic Load Balancing. Ideal for gaming, video editing, real-time ML inference, or hybrid cloud scenarios.
