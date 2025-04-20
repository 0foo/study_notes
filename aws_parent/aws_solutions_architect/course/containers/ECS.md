* Run multiple containers on same machine
* Easy service discovery to enhance communication

* Direct integration with ALB and NLB

* Auto Scaling

* run batch processing and scheduled tasks
    * run on demand/reserved/spot instances

* migrate applications to the cloud 
    * dockerize legacy apps running on prem
    * move docker containers to run on ECS

* ECS Cluster
    * logical grouping of ECS instances 
    * AWS runs ECS service on top of these instances

* ECS Service
    * defines how many tasks should run and how they should be run
    * similar to a k8 deployment/replicaSet
    * manages pods and ensures the desired number of replicas are running, handles updates, ensures 

* ECS Task 
    * literally a container
    * Task Definition
        * metadata in JSON form to tell ECS how to run a Docker container
    * instance of a task definition - running a Docker container
    * a run once ephemeral deal
    * Provide details for each container, such as:
        * Container image(s) to use.
        * CPU and memory requirements.
        * Port mappings.
        * Environment variables and secrets.
        * Networking mode and volumes.
    * Containers are created from Task Definitions and run on the EC2 cluster beneath it

* ECS Service
    * A task in it's basic form is a run once ephemeral workload
    * A service is a higher-level abstraction that manages and maintains the desired number of running tasks for long-lived applications
    * A service manages one or more tasks
    * A service defines:
        * Desired task count.
        * Load balancer integration (if needed).
        * Deployment strategy (e.g., rolling updates).
  
* ECS agent
    * run on all ECS cluster instances
    * it is a daemon on the actual instance and communicates with ECS service and the docker runtime on the instance 
    * will spin up containers when instructer
    * will monitor health
    * will report status of the container/s to ECS

* ECS service
    * will listen to the ECS agents on all of the instances and then configure what needs to be configures inside of AWS
    * i.e. Load Balancer/target groups, Cloudwatch, etc

* EC2 foundation
    * When you create an ECS cluster in ECS it:
    * sets up the instance profile 
    * will also install the ECS agent on the EC2 instances in this cluster
    * attaches the correct IAM role to the instances
    * you setup ASG such that it knows it's a part of the cluster and will spin up instances in the ECS subnet attached to the named ECS cluster with the correct ECS IAM role

* ECS IAM roles
    * EC2 instance profile that the containers are on: instance specific calls, logs, etc.
    * ECS Task IAM role: container/task specific calls, aws services, etc.
    * Available to attach to cluster when you create your ECS cluster

* ECS integration with ALB
    * if you run the same container multiple times on one instance will need to expose the service on different ports
    * ECS will assign a dynamic port on the host for each container and registers that ip/port with the target group attached to the service 
    *  called dynamic port mapping
    
* ECS logging
    * The ECS agent communicates directly with CloudWatch Logs for container logs.
    * Task and instance-level metrics are sent to CloudWatch either through the ECS control plane or optional tools like CloudWatch Agent or Container Insights.
    * For detailed logging and metrics, configuration in the task definition or ECS cluster settings is required.

* Can integrate Secrets and Configurations as Environmental variables into Docker containers
    * SSM parameter store
    * secrets manager

* ECS tasks types of networking
    1. none: no network connectivity, no port mappings
    2. bridge: docker default networking
    3. host: use underlying host network interface
    4. awsVpc: every task launched gets it's own ENI and private IP address
        * allows security group, VPC flow log,  monitoring, etc. like any ENI
        * this is default mode for fargate

* ECS TASK autoscaling
    * do not need a ASG, ECS handles scaling up/down the tasks on the instances
    * can trigger based on a variety of metrics in Cloudwatch
    * can also step wise scale and scheduled scale just like in an normal ASG

* ECS EC2 autoscaling
    * If tasks don't have enough resources will need to scale number of EC2 instances
    * ECS integrates with ASGs to handle infrastructure scaling automatically.
    * ECS determines if additional EC2 capacity is required to place new tasks and triggers the ASG to scale.
    * ECS uses a capacity provider to autoscale
    * a capacity provider is to determine how many instances are required to serve the desired number of tasks and scale the number of instances to match that value
    * instead of a CPU or RAM metric the ASG will autoscale to match the number of tasks(containers) needed
        * note: the tasks definition you specify the CPU/Mem a task needs when it's created
    * The capacity provider will calculate the lower bound on the number of instances required based on the number of tasks, taking into account vCPU, memory, ENI, ports, and GPUs of the tasks and the instances
    * there's a tiny algorith that goes into figuring this all out


* ECS spot instances 
    * can use spot instances to back an ASG in ECS
    * good for cost but impact reliablity





    great capacity provider reference:
    https://medium.com/yipitdata-engineering/instance-auto-scaling-using-aws-capacity-providers-9ea7e66e311f