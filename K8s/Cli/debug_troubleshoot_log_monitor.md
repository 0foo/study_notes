### General

### Uber troubleshooting command

`kubectl describe pod testdownload && k get pod testdownload -o yaml && k logs testdownload`

### Troubleshooting/Debugging
* `kubectl get` all pods
* look for status fields for hints
* drill down with a `kubectl describe` on the broken object
    * look into events section!!
* `kubectl logs`
* for services can do a `get/describe` and/or `get endpoints` to trace network connectivity(see cli section)
* be careful of namespaces and nodes 
* Get all events:
    * `kubectl get events`
* get single pod events
    * `k get  events --field-selector=involvedObject.name=pod`
### Fixing pods
* can use `kubectl edit`
    * can directly edit the definition itself
    * when save the file, will automatically/edit & update the pod 
    * note: can't edit certain fields once a pod is running
        * for example: liveness probes
        * have to delete and recreate the pod
        * see next section
            
* For non-fixable while running live objects:
    1. export the spec as yaml file
        * `kubectl get pod <pod> -n <namespace> -o yaml --export`
    2. delete the pod, 
    3. then fix the spec, 
    4 . then recreate the object
        
* Removing a pod from the scope of the ReplicationController comes in handy
when you want to perform actions on a specific pod. For example, you might 
have a bug that causes your pod to start behaving badly after a specific amount 
of time or a specific event.



###  Logging
* Everything a containerized application writes to stdout and stderr is handled and redirected somewhere by a container engine.  
* ensure log rotation on the node so that space doesn't fill up 
* ```
    kubectl logs <pod name> # pod logs
    kubectl logs <pod name> -c <container name> # specific container logs
    ```
* For crashed containers
    * `kubectl logs --previous <pod name> -c <container name>`
 
* `kubectl logs`
    * Can save this out put to a file via normal linux redirect: > 
* containers normal console output goes into something in K8's called the container log
    * i.e. echo will be stored in kubernetes container log
    

    
* Exceptions:
    * The kubelet and container runtime, for example Docker, do not run in containers, the run on the node and log to the node.
        * On machines with systemd, the kubelet and container runtime write to journald. If systemd is not present, they write to .log files in the /var/log directory. System components inside containers always write to the /var/log directory, bypassing the default logging mechanism.
        * logrotate node logs as well
        
* https://kubernetes.io/docs/concepts/cluster-administration/logging/

### Pod Monitoring/Check Resources
* check resources
    * CPU and Memory
    * ```
        kubectl top pods
        kubectl top pods -n <namespace, without will use default namesapce>
        kubectl top pod <podname>
        kubectl top nodes
      ```
      
* To inspect a nodes resources:
    * `kubectl describe node node-name | grep Allocatable -B 7 -A 6`
    * note: this just filters the large output of describe


#### Monitoring
* One of many kubernetes Monitoring apps
```
git clone https://github.com/linuxacademy/metrics-server
kubectl apply -f ~/metrics-server/deploy/1.8+/
kubectl get --raw /apis/metrics.k8s.io/
```

* Prometheus is a k8's monitoring platform


#### Services

* get external service connectivity
    * `kubectl get svc`
    
* get internal service connectivity
    *this is the connection info from service to pods 
    * `kubectl get endpoints <service name>`
     * can use it to make sure connectivity is working
     