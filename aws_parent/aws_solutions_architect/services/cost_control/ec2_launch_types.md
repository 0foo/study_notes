### Two types

1. spot instances
    * short workloads
    * transient-can loose them 
    * not reliable

2. on demand instances
    * predictable pricing, reliable, stable


3. reserved
    * minimum 1 year to commit
    * for long workload

4. convertible reserved
    * long workloads with flexible instances


5. dedicated instances
    * no other customers even share your hardware

6. dedicated host
    * book entire physical server
    * control instance placement

7. Savings plan
    * discounts based on long term usage
    * commit to a type of usage: i.e. 10$ per hour for up to 1 to 3 years
    * any usage beyond this is billed at on demand price
    * EC2 savings plan
        * gives like 72% savings (same as standard reserved instance)
        * more flexible, rather than locked into a specific instance on RI you choose an instance family on a region
            * locked to instance family
            * locked to region
            * can be any size
            * any OS
            * dedicated or default tenancy
    * Compute savings plan
        * up to 66%, same as convertible RI
        * not locked to instance family
        * not locked to region
        * can also use in ECS or Fargate
        * OS and tenancy
    * sage maker savings plan
        * up to 64% off
        * only on sagemaker workloads
        
* bare metal instance will allow access to core and sockets
* can define host affinity so instance reboots are kept on same host