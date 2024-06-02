apiVersion: <always present>
kind: <type of object>
metadata:
  name: my-pod <name of the pod, will be what appears in the `kubectl get`>
  namespace: some-namespace<add your custom defined namespace here>
  labels: <k/v pairs of custom labels to add to the object>
    app: myapp
    test-label-key:test-label-value
  annotations: <k/v pairs of custom annoations to add to the object>
    owner: test-owner-value
    other-annotation-key:other-annotation-value
spec:
  serviceAccountName: my-serviceaccount <a service account>
  securityContext:
    - runAsUser: 2001 # linux user to run as. Does it have to be userid?
    - fsGroup: 3001 # group to run as, does it have to be a groupid?
  volumes:  # this creates a volume
    - name: config-volume # custom defined name of the volume
      configMap:
        name: my-config-map # passes in an existing config map as the volume data
  containers:
  - name: myapp-container # custom name of the container to use
    image: nginx <the containerer image to use. research where it's fetch from(docker hub?)
    command: ['echo'] # runs a custom command on the container upon start
    args: ['This is my custom argument'] # passes custom args to the command
    ports:
    - containerPort: 80 # exposes a container port to the k8's cluster(more steps needed to expose to outside world)
    env:
    - name: MY_VAR  # the custom defined name of the environmental variable to use INSIDE the container
      valueFrom:
        configMapKeyRef:
          name: my-config-map <name of existing config map
          key: myKey  # name of existing key in the key map to map to the parent env var 
    - name: MY_PASSWORD
      valueFrom:
        secretKeyRef:
          name: my-secret # name of a secret map metadata
          key: myKey # name of a key, will assign the value to the env var
    volumeMounts:
      - name: config-volume # maps an existing volume to a location within a container
        mountPath: /etc/config # location of volume>
    resources:  # define resources limits/requests, see notes/docs for notation
      requests:
        memory: "64Mi" 
        cpu: "250m"  # 250 millicpus out of a total of 1000m=1 cpu core 
      limits:
        memory: "128Mi"
        cpu: "500m"

  restartPolicy: OnFailure # automatically restarted if it fails but if completes then won't be restarted
  restartPolicy: Never  # will never be restarted