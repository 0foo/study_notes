### Deployment
* NOTE: in yaml file-> apiVersion: apps/v1
* .spec.replicas=number of pods
* .spec.template=template pod descriptor which defines pods to be created
* .spec.selector=deploymnet will manage all pods whose lables match this selector
* combines/wrapper around ReplicaSets and Pods and also the ability to deploy
* will create pods and replicasets
* Higher level functionality, Creates pods as part of the deployment, with additional functionality
    * you can see the pods it creates with `kubctl get pods` and see the deployment with `kubectl get deployments`
* Runs a set of identical pods
* Monitors the state of each pod, updating as necessary
* Under the hood creates ReplicaSet
    *  ReplicaSet constantly monitors the list of running pods and makes sure the running 
    number of pods matching a certain specification always matches the desired number.
    * When using a Deployment, the actual pods are created and managed by the Deployment’s ReplicaSets, not by the Deployment directly
* In spec file at least one of the .spec.selector.matchLabels.{} must match one .spec.template.metadata.labels.{}: 
    * ```
      spec:
        selector:
            matchLabels:
                app: nginx
  ````
    * ```
  spec:
      template:
        metadata:
          labels:
            app: nginx
  ```
    * `selector` does not match template `labels`
  

### Updating Deployment/Rolling updates/rollback
* gradually update a deployment to a new container via updating certain pods at a time
* can quickly return to a previous state for recovery, if issues

* when update number of replicas, Deployment object sends that down to the replica set and more or less are done with no rollback

* when update the actual spec, i.e. change containers or parameters or something
    * Deployment creates a new replica set with size zero 
    * then  Then, the size of that replica set is progressively increased, while decreasing the size of the other replica set.
    * update a deployment to new version by gradually updating replicas so there's no downtime
    * spins up new pods and when those pods are ready will start to shut down old pods

* has readiness probes
    * A readiness probe is a test that we add to a container specification. It’s a binary test, that can only say “IT WORKS” or “IT DOESN’T,” and will get executed at regular intervals. (By default, every 10 seconds.)
    * Kubernetes uses the result of that test to know if the container and the pod that it’s a part of are ready to receive traffic. When we roll out a new version, Kubernetes will wait for the new pod to mark itself as “ready” before moving on to the next one.
    * If a pod never reaches the ready state because the readiness probe keeps failing, Kubernetes will never move on to the next. The deployment stops, and our application keeps running with the old version until we address the issue.
    * If there is no readiness probe, then the container is considered as ready, as long as it could be started. So make sure that you define a readiness probe if you want to leverage that feature!
* Rolling between replica sets
    * see: https://semaphoreci.com/blog/kubernetes-deployment
* MaxUnavailable
    * Setting MaxUnavailable to 0 means, “do not shutdown any old pod before a new one is up and ready to serve traffic“.
* MaxSurge 
    * Setting MaxSurge to 100% means, “immediately start all the new pods“, implying that we have enough spare capacity on our cluster, and that we want to go as fast as possible.
* The default values for both parameters(MaxSurge and MaxUnavailable) are 25%, meaning that when updating a deployment of size 100, 25 new pods are immediately created, while 25 old pods are shutdown
*  When we edit the deployment and trigger a rolling update, a new replica set is created with same labels. This replica set will create pods, whose labels will include (among others) run=web. As such, these pods will receive connections automatically.
*  This means that during a rollout, the deployment doesn’t reconfigure or inform the load balancer that pods are started and stopped. It happens automatically through the selector of the service associated to the load balancer.

* Deployment creates ReplicaSet creates Pods
* Good for dev
* Good for production
* You can rollout and rollback your changes using deployment
* Monitors the state of each pod
* Best suitable for production
* Supports rolling updates

* References: 
    * https://semaphoreci.com/blog/kubernetes-deployment
    * https://thenewstack.io/kubernetes-deployments-work/




  