### Services
*  provides network access to a dynamic set of pods, specified by a selector
    * using target by selector allows the set of pods to expand and contract based on traffic needs and/or failures
*  one purpose is to be load balancers for Kubernetes traffic, internal and external.
*  uses selectors for the targets of it's traffic
*  connections to this IP address on port 80 will be load-balanced across all the pods of this deployment, matching the service’s selector..
*  `kubectl get endpoints <service name>`
     * this is the connection info from service to pods
     * can use it to make sure connectivity
* can port proxy via ports and targetPort 
* service types
    * clusterIP : exposes the service INSIDE the cluster 
        * used for expsing the pods to other pods/services inside the cluster
        * The service will have its own internal IP address (denoted by the type: ClusterIP)
        * note: it's also accessible by cluster DNS despite the name clusterIP
    * NodePort: exposes the service OUTSIDE the cluster on a NODE port
        * only on a single node?
        * used mainly for dev/test purposes
    * LoadBalancer: provision a load balancer EXTERNAL to the app(i.e. an AWS or AZURE load balancer)
        * only works if setup to interact with a cloud platform
    * ExernalName: Maps the service to an external URL, such a database outside of the cluster, or an API
        * doesn't do any internal pod mapping
        * essentially abstraction layer on top of application or entity external to the cluster
