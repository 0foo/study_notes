### Enumeration


### Cluster enumeration and CLI:
*  
```
kubectl get <item>
kubectl get <item> <item name>
kubectl describe <item> <item name>
kubectl edit <item> <item name>
kubectl delete <item> <item name>  
```

* EX:
* `kubectl describe pod <pod name> -n <namespace> `
* `kubectl get nodes`
* `kubectl get nodes $node_name`
* `kubectl get nodes $node_name -o yaml`
* `kubectl describe node $node_name`


* view logs
    * `kubectl logs <podname>`

* view IP's 
    * `kubectl get pods -o wide`
    * `kubectl get pod <podname> -o yaml | grep ip`


* To get more info about things 
    * `kubectl get <x> -o yaml`
    * `kubectl describe <x>`

* Get wider output for pods: a Pod IP addy, Node, and more.
    * `kubectl get pods -o wide`
    * `kubectl get pod <podname> -o wide`
 
* list all object resources available in cluster
    * `kubectl api-resources -o name`
    * can enumerate cluster capabilities
    * i.e. pods, services, etc.    
    
* persistant watch of the get statement
    * -w flag
    
### Deployment enumeration
* `kubectl get all -A`
    * this gets pods,services, replicasets, deployments in every namespace
    * note will not get configmaps and other things
    * if this is too big, can drill down more precisely with the following commands


    
### Get yaml from existing objects
* `kubectl get deployments ghost -n ghost -o yaml` (can out put to file > file.yaml)


### Gotchas 
* be sure when typing these to use the correct namespace or will get error even if object exists


### Resources

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


### Filtering/Matching
* See `./selectors.md`
    
    
### Services
* get external service connectivity
    * `kubectl get svc`
    
* get internal service connectivity
    *this is the connection info from service to pods 
    * `kubectl get endpoints <service name>`
     * can use it to make sure connectivity is working
     
* `kubectl get endpoints <service name`
    * this is the connection info from service to pods
    * can use it to make sure connectivity

