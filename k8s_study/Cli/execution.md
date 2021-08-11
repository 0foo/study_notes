### Imperitive commands
```
kubectl create -f your-object-config.yaml
kubectl delete -f your-object-config.yaml
kubectl replace -f your-object-config.yaml
```

### Declarative commands
```
kubectl diff -f configs/
kubectl apply -f configs/
```

### Create yaml via cli, for a basic skeleton
* add these params on  `--dry-run -o yaml`

### Generators, run vs create
* run is older than create
* In a pre-1.18 cluster, it was possible to run a Pod and other resources using the kubectl run command.
* With the release of 1.18, things became much clearer as kubectl run is now only used to create a Pod. no more ambiguous flags.
    
    ##### via kubectl create
        * can create a wider vareity of object than run command
        * `kubectl create service clusterip foobar --tcp=80:80`
        
    ##### generators with kubectl run
    * older way
    * `kubectl run nginx --image=nginx:latest --generator=run-pod/v1 --limts="cpu=200m,memory=512Mi"`
    * `kubectl run busybox --image=busybox --dry-run --generator=cronjob/v1beta1  --schedule="*/1 * * * *" -- /bin/sh -c "date; echo hello from kubernetes cluster"`
    * new way
    * `kubectl run www --image=nginx:1.16`
    * If we need to create other resources in an imperative way, we can use the kubectl create command
    * can run container directly from cli
    * ` kubectl run web --image=nginx`

    ##### reference
    * https://medium.com/better-programming/kubernetes-tips-create-pods-with-imperative-commands-in-1-18-62ea6e1ceb32


### Get yaml from existing objects
* `kubectl get deployments ghost --export -n ghost -o yaml > objectfile.yaml`


### Gotchas 
* be sure when typing these to use the correct namespace or will get error even if object exists


### Run shell/command in container

* Run a command in a Container
    * `kubectl exec <pod name> -- <bash command here>`
    * `kubectl exec <pod name> -- curl <secure pod cluster ip address>`
    
* get a shell to a container
    * `kubectl exec -it task-pv-pod -- /bin/bash`
    

### Deployments
* `kubectl set image <>` change a deployment
    * -r  or --record flag
    * will store the changes so that can rollback if needed

*  can create deployment via cli: `kubectl expose deployment web --port=80`
    * also done via .yaml spec file

* `kubectl rollout history deployment/rolling-deployment`
* `kubectl rollout history deployment/rolling-deployment --revision=2`
* `kubectl rollout undo deployment/rolling-deployment`
* `kubectl rollout undo deployment/rolling-deployment --to-revision=1`


* imperitive namespace creation
    * `kubectl create ns <namespace>`
    
    
### Edit running objects
* can in place edit running objects
* `kubectl edit <x> <object name>`
* `kubectl edit deployment <deployment name>`
* better to export the yaml to a file, edit, then apply


* Get the yaml spec from the running in memory k8s cluster
    * `kubectl get pod <pod> -n <namespace> -o yaml --export`
    * only gets the actual yaml defined spec of the pod, ignores the status and other metadata   

* Run a spec file:
    * `kubectl apply -f <filename>`

### Editor
* Be familiar with the editor you want to use. In my case , I used Vi.
* Things you should know and fast in doing

* Find and replace
* Going to exact line
* Deleting the word and line
* Checking the alignment
* Save & exit