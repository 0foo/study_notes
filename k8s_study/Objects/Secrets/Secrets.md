### Secrets:
* can create a secret file
* can set it in spec file with apply
* secrets are stored in etcd, note they are only base64 encoded, which means super easy to crack
    * control access to etcd
* pass it into .spec.containers[].env
    *
       ```
        valueFrom:
            secretKeyRef:
                name: my-secret
                key: myKey
       ``` 

