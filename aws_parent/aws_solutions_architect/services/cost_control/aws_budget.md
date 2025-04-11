* create a budget and set alarms when cost exceeds budget
* 4 types of budgets
    1. cost
    2. usage
    3. reservation
    4. savings plans

* for reserved instances (RI)
    * track utilization
    * supports EC2, elasticache, RDS, Redshift

* define up to 5 notifications per budget

* budgets are very granular
* can define a budget by: service, linked account tag, purchase option, instance type, region, availability zone, api operation

* same otions as COST EXPLORER!

* budget action
    * run an action when the budget exceed threshhold
    1. Apply IAM policy to a user,group, or IAM role to restrict from doing anything
    2. Apply service control policy to an organizational unit to restrict what an account can do
    3. Stop EC2 or RDS instances
    * can happen automatically or require a workflow approval to ensure some human says yes

* Example:  If have a root OU with a dev OU inside of it that needs resources in the root OU. 
    * if the budget alarm threshold is triggered, can apply an SCP to the dev OU to restrict their access to the root OU resource


* centralized budget management
    * see architecture section
* decentralized budget managemetn
    * see architecture section

