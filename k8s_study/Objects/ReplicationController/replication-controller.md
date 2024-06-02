### Replica Controller

* legacy, replaced by deployment and replica sets


* The major difference difference between a replication controller and replica set is that the rolling-update command works with Replication Controllers, but won’t work with a Replica Set. 
* This is because Replica Sets are meant to be used as the backend for Deployments. Let’s clean up before we move on.
* Deployments are intended to replace Replication Controllers. When comparing a Deployment vs Replica Set, the former provides  the same replication functions (through Replica Sets) and also the ability to rollout changes and roll them back if necessary. 
* https://www.mirantis.com/blog/kubernetes-replication-controller-replica-set-and-deployments-understanding-replication-options/