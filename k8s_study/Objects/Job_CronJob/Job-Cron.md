### Jobs/CronJobs
* used to reliably execute a workload until it completes
* as opposed to pods which continue to run constantly
* will creeate one or more pods which will enter completed state after running the job
* part of batch api, 
    * apiVersion: batch/v1
* backoffLimit: 4 => how many times job will attempt to run if it fails
* restartPolicy: Never (never attemp to resart)
* restartPolicy: OnFailure (automatically restart if fails, but if complets wont be restarted)
* CronJob-run job workload periodically, according to a schedule
    * .spec.schedule: "*/1 * * * *"
    * `kubectl get cronjobs`
            * LAST SCHEDULE is the last time it ran, other fields are self explanatory
    * will allow you to see the scheduling info for the cronjob
* .spec.backOffLimit: how many times the job will attempt to run if it fails
