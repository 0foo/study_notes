### PersistentVolume
* TBD
    
### PersistentVolumeClaim
* TBD

### Volume
* spec.volumes

```
- name: vol1
  emptyDir: {}

- name: config-volume
  configMap:
    name: my-config-map


```


### Storage
* containers internal storage ephemeral by default
    * when that container is deleted that storage is gone

* Kubernetes is designed to manage stateless containers
    * pods/containers should be easily deletable and replacable
    * since data inside container is gone when container deleted need external storage to container lifecycle

* State persistence: maintaining data outside and potentially beyond the lifecycle of a container
* PersistentVolume and PersistentVolumeClaims provide easy way to implement/consume storage resources in the context 
    of complex production environment that has numerous storage solutions
    * can abstract out s3, google cloud, EBS, etc. with a PersistenVolume object
    
* a Node represents CPU and Memory resources while a PV represents Storage resources

* PersistentVolume represents a storage resource


* StorageClass: 
    * defines categories of storage
    * ex: fast, slow, manual
    
* accessModes:
    * determine what read/write modes can access the volume
    * how many pods/read, write/etc.
    * ex: ReadWriteOnce
    
        
* storageSystem<-->PersistentVolume<-->PersistentVolumeClaim<-->Pod

* Volume
    * Volumes exists outside the lifetime of the container and aren't ephemeral
    * mounts volumes to specific container
    * setup inside of the pod spec-> .spec.volumes
    * assigned to container/s via -> .spec.containers.volumeMounts[]
    * types of volume:
        * .spec.volumes.emptyDir volume
            * can add an emptyDir to numerous containers who all now share volume
            * in below spec file the two containers share the my-volume storage at /tmp/storage
        * ```
            apiVersion: v1
            kind: Pod
            metadata:
              name: volume-pod
            spec:
              containers:
                  - image: busybox
                    name: busybox
                    command: ["/bin/sh", "-c", "while true; do sleep 3600; done"]
                    volumeMounts:
                    - mountPath: /tmp/storage
                      name: my-volume         
                  - image: busybox
                    name: busybox
                    command: ["/bin/sh", "-c", "while true; do sleep 3600; done"]
                    volumeMounts:
                    - mountPath: /tmp/storage
                      name: my-volume
              volumes:
                - name: my-volume
                  emptyDir: {}
        ```

* Two ways PVs may be provisioned: statically or dynamically
    * static: via statically provisioned PV/PVC
    * dynamic: via StorageClasses
    
* AccessModes
    * ReadWriteOnce -- the volume can be mounted as read-write by a single node
    * ReadOnlyMany -- the volume can be mounted read-only by many nodes
    * ReadWriteMany -- the volume can be mounted as read-write by many nodes


* Steps
    1. create PV `kubectl apply`
        * `kubectl get pv <pv name>`
            * look for status of available
    2. create PVC `kubectl apply`
        * `kubectl get pvc`
        * `kubectl get pv`
            * look for status of bound on both
    3. Add the PVC to the Pod
    
    
* PersistentVolume
    * this sets up the storage ON THE STORAGE SIDE
    * location of the storage on the storage provider or local host
    * types:
        * hostPath PersistentVolume. 
            * Kubernetes supports hostPath for development and testing on a single-node cluster.
            * In a production cluster, you would not use hostPath. 
                Instead a cluster administrator would provision a network resource like a 
                Google Compute Engine persistent disk, an NFS share, or an Amazon Elastic Block Store volume.
    * `kubectl get pv <pv name>`
        * can see if status is Available
    * https://kubernetes.io/docs/concepts/storage/persistent-volumes/
                
* PersistentVolumeClaim
    * PVC is Abstraction between the user(Pod) and the PersistentVolume
    * bind PVC to PV
        * PVC's automatically bind to a PV that has compatible:
            * StorageClassName
            * accessModes
            * enough space to provide the requested amount
        * Can bind to PV before bind to Pod
            * `kubectl get pv`
            * can check if bound to PV
            
    * bind to pod
        * spec.volumes.persistentVolumeClaim
        * instead of volume version: .spec.volumes.emptyDir
        * note: the pod doesn't know about the PV just the PVC

* Retention
    * The reclaim policy for a PersistentVolume tells the cluster what to do with the volume after it has been released of its claim
    * Currently, volumes can either be Retained, Recycled, or Deleted.
    * Reclaim: 
        * When the PersistentVolumeClaim is deleted, the PersistentVolume still exists and the volume is considered "released". 
        * But it is not yet available for another claim because the previous claimant's data remains on the volume. 
        * admin must manually follow steps to reclaim
    * Delete:
        * deletion removes both the PersistentVolume object from Kubernetes, as well as the associated storage asset in the external infrastructure, 
          such as an AWS EBS, GCE PD, Azure Disk, or Cinder volume.
    * Recycle:
        * If supported by the underlying volume plugin, the Recycle reclaim policy performs a basic scrub (rm -rf /thevolume/*) on the volume and makes it available again for a new claim.



* StorageClass
    Volumes that were dynamically provisioned inherit the reclaim policy of their StorageClass, which defaults to Delete
    