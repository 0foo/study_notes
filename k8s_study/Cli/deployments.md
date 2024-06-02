### Deployment CLI managment

* can set certain properties 
    * 
    * record flag records information about the deployment
    * env, image, resources, selector, serviceaccount, subject 
    * hint type `kubectl set` then hit tab to see options
    * on specific container
        * `kubectl set image <deployment name> <container name>=<image name> --record`
    
* view rollout REVISION history
    * view all the revisions
        * `kubectl rollout history deployment/rolling-deployment`
    * view a single revision in detail, including a diff of changes
        * `kubectl rollout history deployment rolling-deployment --revision=2`

* undo a rollout
    * `kubectl rollout undo deployment/rolling-deployment`
    * `kubectl rollout undo deployment/rolling-deployment --to-revision=1`

* pause a rollout
    * `kubectl rollout pause deploy nginx`
    
* can expose a deployment with a service 
    * `kubectl expose deployment web --port=80`
    
* check rollout status
    * `kubectl rollout status deploy nginx`

* can scale a deployment
    * `kubectl scale deployment.v1.apps/nginx-deployment --replicas=10`

* can autoscale deployment 
    * `kubectl autoscale deployment foo --min=2 --max=10 --cpu-percent=80`
    * make sure cluster is setup for it
    * this is based on CPU usage

*  can create service connected to a deployment via cli: 
    * `kubectl expose deployment web --port=80`
    * also can add flag --expose when first create the deployment
    * also can create the service directly and connect via labels

