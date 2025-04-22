#### All services

* Compute
  * EC2
    * Know instance types (e.g., t3, m5, c6g) and use cases.
    * Understand pricing models: On-Demand, Reserved, Spot, Dedicated Hosts.
    * Know how to attach EBS volumes, create AMIs, and use EC2 User Data.
    * Understand security groups, key pairs, and EC2 metadata/roles (IAM roles).
    * Placement groups (cluster, spread, partition) and their impact on networking.

  * Lambda
    * Understand event-driven architecture and use cases (e.g., S3, API Gateway triggers).
    * Know how concurrency, cold starts, and timeouts work.
    * Deployment using versions and aliases.
    * Permissions via execution roles.
    * Key limits: 15 minutes max runtime, memory up to 10 GB.

  * Auto Scaling Group (ASG)
    * Automatically scales EC2 instances based on demand.
    * Know scaling policies: target tracking, step, and scheduled.
    * Integration with CloudWatch alarms and ELB.
    * Understand launch templates/configurations and lifecycle hooks.

  * AWS Batch
    * Run batch computing jobs without managing infrastructure.
    * Understand job definitions, job queues, and compute environments.
    * Automatically provisions optimal compute resources.
    * Common for genomics, rendering, and simulations.

  * ECS
    * AWS-native container orchestration using EC2 or Fargate.
    * Understand ECS task definitions and service definitions.
    * Integration with ALB, CloudWatch, IAM, and auto scaling.
    * Cluster management if using EC2 launch type.

  * Fargate
    * Serverless compute engine for containers (works with ECS or EKS).
    * No EC2 management — just define CPU/memory per task.
    * Simplifies scaling and deployment of containers.

  * Elastic Beanstalk
    * PaaS to deploy applications (Java, Python, PHP, etc.) with minimal configuration.
    * Automatically handles provisioning, load balancing, scaling, and monitoring.
    * You retain control over underlying resources if needed.

  * AWS Outposts
    * Run AWS infrastructure and services (EC2, EBS, RDS) on-premises.
    * Ideal for low-latency or data residency requirements.
    * Managed and updated by AWS.

  * AWS Local Zones
    * Extend AWS compute/storage closer to users in metro areas.
    * Useful for latency-sensitive apps like media or gaming.
    * Partially managed infrastructure — EC2, EBS, and more are available.

  * AWS App Runner
    * Simplified deployment for web apps from GitHub or container registry.
    * Handles build, deploy, scaling automatically.
    * Good for developers who want to avoid infrastructure management.

  * VMware Cloud on AWS
    * Run VMware-based workloads on AWS infrastructure.
    * Supports vSphere, vSAN, NSX — useful for hybrid cloud migrations.
    * Managed by VMware, billed through AWS.

