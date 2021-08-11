### Pods:
* Runs a single set of containers
* Good for one-off dev purposes
* Rarely used directly in production
* No state monitoring, no replicas, etc.
* In kubernetes Pods are the smallest deployable units. 
* Every time we create a kubernetes object like Deployments, replica-sets, statefulsets, daemonsets it creates pod.
* run commands in containers and pass args:
    * .spec.containers[].command
    * .spec.containers[].args
    
   ```
    containers:
      - name: myapp-container
        image: busybox
        command: ['echo']
        args: ['This is my custom argument']
    
    ```
* open ports to cluster on the container
    * by default ports only available to other containers in the Pod
    * with this will open to other pods in cluster and if configured to the world
    * .spec.containers[].ports[].containerPort

* 