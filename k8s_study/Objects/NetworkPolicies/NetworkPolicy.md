### NetworkPolicies
* Like Security Groups from AWS but for K8's
* By default(with no network policy) all pods are allowed to communicate with any other pod and reach out to any available IP
* As soon as a NetworkPolicy applies to a pod(i.e. valid pod selectors)
    * the default will be to blacklist everything
    * the NetworkPolicy of allowed options will be a whitelist
* Note: numerous k8's clusters don't support NetworkPolicies by default(may need to setup canal or cilium)
* ```
    kubectl get networkpolicies
    kubectl describe networkpolicy my-network-policy
      
      ```
    * Spec:
        * The pod selector applies this NetPol to pods and locks them down/blacklist everything from them
        * the policyTypes/ingress/egress opens up per those specifications
         ```
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: my-network-policy
        spec:
          podSelector:  # APPLIES THIS POLICY TO PODS
            matchLabels:
              app: secure-app
          policyTypes:   # WHITELIST
          - Ingress
          - Egress
          ingress:        # WHITELIST
          - from:
            - podSelector:
                matchLabels:
                  allow-access: "true"
            ports:
            - protocol: TCP
              port: 80
          egress:        # WHITELIST
          - to:
            - podSelector:
                matchLabels:
                  allow-access: "true"
            ports:
            - protocol: TCP
              port: 80
        ```