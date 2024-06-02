### Lables/Annotations/Selectors/Matching

* For deployments
    ```
      spec:
        selector:
            matchLabels:
                app: nginx
  ````
   ```
  spec:
      template:
        metadata:
          labels:
            app: nginx
  ```
* for node targeting

* `selector` does not match template `labels`

### Labels/Selectors
* Labels
    * under the metadata parent node: .metadata.labels
    * useable by selectors via other objects or CLI to identify objects
    * cli flag = --show-labels
    * or there's a labels section in describe
* Selectors
    * provide us a way to select a list of objects based on their labels
    * used by objects to grab other objects and apply functionality
    * used by cli to obtain objects
    * in objects .spec.selector.matchLabels
    * selectors must match ALL of the labels defined
    
### Annotations
* used to store custom metadata about objects
* not intended to be identifying and not usable by selection
* just attach some kind of custom data that you want to record abou the object
* functionless from a k8's perspective
* can view with a `describe`

### Filtering/Increasing output
* --all-namespaces
* -n <namespace>
    * can enter into namespaces
* -o 
    * wide - get wider output for pods: a Pod IP addy, Node, and more.
    * yaml - get yaml of the object
    * name - get name of the object
    
* --show-labels
* -l
    * can filter via labels with this, see below
    * note this is a filter language, see below

* using labels/selectors: -l
    * --show-labels
    * describe has labels section as well
    * -l flag
        * `kubectl get <x> -l <label key value pair>`
        * `kubectl get pods -l app=my-app`
        * `kubectl get pods -l app!=my-app`
        * Select numerous values per label(set based): `kubectl get pods -l 'environment in (development,production)`        
        * Select numerous keys and values for labels(k/v or set based): `kubectl get pods -l app=my-app,environment=production`

* use -L
    * will give you a column for that label key

* add labels/annotatate via CLI
    * `kubectl label pods my-pod new-label=awesome`       
    * `kubectl annotate pods my-pod icon-url=http://goo.gl/XXBTWq`