### Fault injector simulator service

* based on chaos engineering
* randomly generate faults to ensure our architecture is solid
* help find hidden bugs/bottlenecks
* some services supported
    * EC2
    * ECS
    * EKS
    * RDS


* will create a template inside Fault Injector Simulator service
* start the experiment
* monitor with cloudwatch or event bridge
* then stop the experiment
* FIS will output a report 
    * performance
    * observibibily
    * resiliency
    * etc.