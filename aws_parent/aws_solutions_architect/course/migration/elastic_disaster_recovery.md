* AWS Elastic Disaster Recovery (AWS DRS)

  * What It Is:
    * Lets you quickly recover on-premises or cloud-based servers to AWS during a disaster

  * Key Features:
    * Continuous replication using lightweight agents
    * Low RTO (minutes) and RPO (seconds)
    * Non-disruptive testing of recovery plans
    * Automated orchestration to launch EC2 recovery instances
    * Supports Windows and Linux

  * Use Cases:
    * Disaster recovery for:
      * On-premises servers
      * EC2 instances across regions/accounts
      * VMware, Hyper-V, physical servers

  * Workflow Overview:
    * Install agent on source machines
    * Data continuously replicates to AWS
    * Failover event triggers recovery in minutes
    * Option to fail back to original site
