* managed Kubernetes cluster 
* k8's open source, ECS is not
* alternative to ECS for container orchestration of containers
* K8's is cloud agnostic, can migrate

* EKS supports 2 launch modes:
    1. ECS - to manage the worker nodes
    2. Fargate - to have serverless 


* EKS worker nodes in private subnets (pods)
* Nodes can be autoscaled
* can setup  load balancers to talk to the web

* Node management: 
    1.  managed node groups
        *  AWS creates/manages nodes for you
        *  support for on demand and spot
        * AWS manages the lifecycle of nodes, including provisioning, patching, and upgrades.
        * You still manage the AMI, Kubernetes versions, and instance configurations.
        * good for if you have custom configurations you need

    2. self managed nodes
        * you manage everythign
        * create nodes and register
        * manage those with ASG
        * can use EKS optimzed AMI
        * also supports on demands 

    3. fargate mode
        * don't even look at nodes
        * AWS handles everything


* data volumes 
    * need to specify a StorageClass manifest in your EKS cluster
    * leverages Container Storage Interface(CSI) driver
    * Support for
        * EBS
        * EFS(only storage that works with fargate)
        * FSx for Lustre
        * FSx for NetApp ONTAP