#### Kubernetes meaning
* Kubernetes (“koo-burr-NET-eez”) is the no-doubt-mangled conventional pronunciation of a Greek word, κυβερνήτης, meaning “helmsman” or “pilot.” 
* https://www.geekwire.com/2016/ever-come-kooky-kubernetes-name-heptio/

#### Namespaces
* without a namespace, 
    * the object will be in the default namespace
    * with a namespace, will not see the object in the basic `kubectl get pods`!!!
    * will have to add the namespace in the `get` call AND ALL calls for that object
        * without the namespace specified k8's will act like the object doesn't exist
* can add a namespace in the `metadata` section in the spec.yaml file
    * see `my-pod-namespace.yaml`
    * .metadata.namespace
* uses: 
    * organizing appplications running the same cluster
    * multiple teams 
Commands:
    create a namespace:
    * kubectl create ns <namespace name>
    specify a namespace in a get:
    * kubectl get pods -n my-ns
 
#### State management in K8's
* k8s tries to make the status match the deployment spec
* spec 
    * desired state of that object
* status
    * the current state of the object
* can see spec and status via `kubectl describe` commands

### Vocab
* Node: The actual server hardware that a k8's daemon is running on
* Pod: A collection of containers that serve a purpose that run on a Node
* Container: the actual singlar unit of work/container that is running
* ton more objects

### Networking
* Each Pod is assigned a unique IP address for each address family. 
* Every container in a Pod shares the network namespace, including the IP address and network ports. 
* Inside a Pod (and only then), the containers that belong to the Pod can communicate with one another using localhost.

### SecurityContext
* pods run all containers as root by default
* security groups effectively change the user/group of the running the pod 
* can set the pod as a user and group without root access
* interactions between container and node
* defines the containers user/group running on the node
    * if the container doesn't have the permissions then things like volume mounts will mount but the files will deny access
    * i.e. chmod and chown a location on the node for a user that is different than the security context's defined user for the pod
        * the pod won't have access
* Note: Pod status will be `Error` if have issues with permissions of any mounted files

### Resource Requirements
* k8's allows us to specify the resource requirements of a container in the pod spec
* memory/cpu 
* defined in terms of:
    * resource requests 
        * the amount of resources on the node requested/necessary to run a container
        * pod will only run on a node that has enough resources to run it
        * K8s's typically kills container if not enough resources as defined in resources are available 
        * k8s kills a container if the container passes its defined limit, i.e. uses to many resources
    * limits
        * maximum value for the resource usage of a container on a node
        * if goes above limit, container will be killed 
* specified under the `container` root key 
    * .spec.containers[].resources
* notation is here
    * https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/#meaning-of-memory
* cpu limits are percentage of a cpu core. 1000 millicpus = 1 cpu core. 
    * so 250m is 1 quarter of a cpu core.
* doing a describe on a container will also show this.
* can see the limits/requests via `kubectl describe`
* CPU consumption specificed in CPU millicores or cores: 500m is 500 millicores.
* Memory can be Mi, Gi


#### RestartPolicy
* .spec.restartPolicy
* restartPolicy field with possible values Always, OnFailure, and Never. 
* The default value is Always.
* The restartPolicy applies to all containers in the Pod.


#### Service account:
* service accounts allows the pod to access the kubernetes API
* some pods need acces to k8's cluster
* .spec.serviceAccountName: <account name>
* `kubectl create serviceaccount <some service account name>`
    * creates a service account
* on CKAD don't need to know how to configure service accounts inside of the k8's cluster


### Multi Container Pods
* Pods with more than one container that all work together as a single unit
* Mostly have containers separate in their own pods but certain cases it's good to have multi-container pods
* .spec.containers[] accepts multiple container definition
* multi-container pod design patterns: 
    * sidecar 
        * has main container and side car container
        * side car container enhance the functionality of the main container in some way
        * ex: a side car that syncs files from github to a webserver every two minutes
        * cron job containers are a good example of this
        
    * ambassador
        * i.e. a web server
        * capturing and translating network traffic
        * network traffic goes to ambassador first then to the main container
        * ambassador listens on a custom port then forwards traffic to a legacy application container hardcoded on a different port
    
    * adapter
        * i.e. a proxy server that 
        * changing the output from the main container
        * data/traffic leaves the main container and goes to the adapter first which transforms the output from the main container
        
        
* containers in same pod interact with one another via:
    * shared network
        * it's as if the containers were all on the same host
        * can use localhost to access other containers i.e. localhost:1234
        * note: containers in same pod can communicate with each other by default
            * no need to expose it or anything.
        * share a port range i.e. only one container may bind a single port
    * shared storage volumes
        * can mount the same volume to two different containers
        * one container outputting to volume and other reading or vice versa
    * Shared Process Namespace
        * allows the two containers to signal each other's processes
        * to enable have to add a flag to pod spec:
            *shareProcessNamespace: true
            
### Probes
* Customize how kubernetes determines the status of your container

* Liveness Probe
    * indicates whether container is running properly
    * governs when cluster automatically starts/stops container
    * .spec.containers[].livenessProbe:
        * exec.command
            * runs a command in the container
        * initialDelaySeconds: 5
            * waits X number of seconds before running the command specificed in .exec.command
            * incase you need to delay the inital start of the liveness probe
        * periodSeconds: 5
            * runs the probe every five seconds
    
* Readiness Probe
    * detects whether pod is ready to recieve requests
    * i.e. if the container takes some time to start up 
    * .spec.containers[].readinessProbe:
        * httpGet:
            * makes an http request to the pod on port 80 at path of /
            * path: /
            * port: 80
        * initialDelaySeconds
        * periodSeconds
           
* Some common ways for Probes to detect the container status:
    * run a command  
    * send an http request
  



### Command is NOT executed within a shell
* WRONG: 
```
  containers:
    - name: busybox
      image: busybox
      command: ["while true; do date; sleep 1;done"]

```
* CORRECT:
```
apiVersion: v1
kind: Pod
metadata:
  name: tip1-pod
spec:
  containers:
    - name: busybox
      image: busybox
      commands: ["sh", "-c"]
      args: ["while true; do date; sleep 1;done"]
```


### Set multiline value in ConfigMap
* Use | or |-
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: tip2-configmap
data:
  NGINX_CONFIG: |-
    server {
      listen 80;
    }
```