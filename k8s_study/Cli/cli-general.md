## CLI
* k8's has an elegant and predictable cli

* Two ways to add objects to cluster
    1. imperative
        * directly via cli
    2. declarative
        * use yaml spec files
    * https://www.digitalocean.com/community/tutorials/imperative-vs-declarative-kubernetes-management-a-digitalocean-comic

### Imperative 
* Advantages:
 * Simple, easy to learn and easy to remember.
 * Require only a single step to make changes to the cluster.

* Disadvantages:
 * Do not integrate with change review processes.
 * Do not provide an audit trail associated with changes.
 * Do not provide a source of records except for what is live.
 * Do not provide a template for creating new objects.

### Declarative

* Advantages compared to imperative object config:
    * Changes made directly to live objects are retained, even if they are not merged back into the configuration files.
    * Better support for operating on directories and automatically detecting operation types (create, patch, delete) per-object.

* Disadvantages compared to imperative object configuration:
    * Harder to debug and understand results when they are unexpected.
    * Partial updates using diffs create complex merge and patch operations.


### Running/Viewing objects
* commands:
    * create
    * start,stop,delete
    * edit
        * opens up in a text editor to edit the object spec
    * apply 
        * via file: -f <filename>
        * updates the object from the spec
    * view logs
        * `kubectl logs <podname>`
    * execute command inside a pod
        * exec command with -- and a space
        * `kubectl exec <podname> -- ls /etc/config`
    * exec 
        * run a command on the container
    * get
        * gets a big picture view of all of the objects in that class
    * describe
        * gets detailed information about specific object   

### Cli help

* `kubectl run pod --help`
    * this explains everything needed for that command
    
* `kubectl explain <resource>`
    * this lets you explore the yaml SPEC
    * `kubectl explain pod.spec.containers.env`
    * `kubectl explain pod.spec.volumes`


### Exam tips
### Increase cli efficiency
* `alias k=kubectl`
* configure the text editor you'll be using

### If copy in from internet Paste into notepad first to get weird of odd characters
* when copying from docs:
* The suggestion is that always paste the texts into the notepad first, 
* adjust any indent problems, 
* and then move it to the YAML file in the exam console.

### Speed up delete
* Delete a pod is slow by using command kubectl delete pod <pod name>. It may take up to 10-20 seconds to complete
* `kubectl delete pod my-pod --grace-period=0 --force`