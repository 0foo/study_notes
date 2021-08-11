### Config Map

#### CLI

* create a 
    * `kubectl create configmap test --dry-run=client  -o yaml > cm.yaml`


* k/v store of configuration data that you need to pass into pods/containers

* can pass in two ways
    1. Set as environment vars in the containers of a pod
        * via env section of spec file
    2. Pass as a volume
        * if passed in as volume mount, each TOP LEVEL key will be added as a FILE in your mount point
        * so if your mount point is `/etc/config` and you mount a config map there will be one file per TOP LEVEL KEY
            * i.e. cat /etc/config/MY-CONFIG-KEY  returns my-config-value
            * i.e. cat /etc/config/MY-CONFIG-KEY-2  returns my-config-value-2
    * in .spec.containers[].env:
        ```
          valueFrom:
            configMapKeyRef:
              name: my-config-map
              key: myKey
        ```        

* can specify an entire FILE as a config map
    * If the following is mounted as a volume, there will be a file named candy.cfg at the mount point.
    ```
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: candy-service-config
    data:
      candy.cfg: |-
        candy.peppermint.power=100000000
        candy.nougat-armor.strength=10
    ```