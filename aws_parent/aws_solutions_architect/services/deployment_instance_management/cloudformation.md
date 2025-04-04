* Infrastructure as code
* other services rely on it, for example: beanstalk, SAM, etc.


* Note: these are some facts about it to know.



* Data retention: retain data when CF stack is deleted 
    * by default everything is deleted in CF
    * can define a DeletionPolicy to control what happnes when CF template deleted
        * in CF under the resource itself you add DeletionPolicy attribute
            * DeletionPolicy=retain
                * just simply don't delete it
            * DeletionPolicy=snapshot(can delete,  but take snapshot first)
                * works on anything that can be snapshotted for example: ebs, rds, elasticache, redshift
            * DeletionPolicy=delete
                * default policy, delete the resource
                * if using RDS, the default policy is to snapshot
                * S3 bucket can't be deleted unless empty

* Custom resources: can define cloudformation custom resources
    * backed by a lambda function that can do anything you want (via API calls)
    * anytime CF is run, will invoke that custom resource which will invoke the lambda
    * for things like
        * brand new resources with no CF support, can use lambda to manipulate them
        * an on-prem resource
        * emptying an s3 bucket before deletion
        * fetch an AMI id
        * anything else!!!

     
            

* Stack sets: update all accounts and regions associated with the stack set
    * manage stacks across multiple accounts/regions
    * allows you to deploy the same infrastructure across regions/accounts
    * really useful for security or shared services
    * can enable an auto rollout feature for when an account is added to an organization


* cloudformation drift
    * things become changed outside of cloudformation i.e. manually
    * this is drift
    * how to know: use the service called: cloudformation drift
    * can detect drift at the stack layer or lower

* integration of secrets manager and Cloudformation
    * can create a secret in the cloudformation template with a function call GenerateSecretString
    * that secret is stored in secrets manager
    * that secret is then set in a reference that can be used throughout cloudformation without having to hardcode the secret in the CF template file
    
* import existing resources 
    * can import existing manually created resources into a cloudformation template
    * will need to create a CF template that mirrors currently existing maually created resources
    * use unique identifiers for resources
    * when you add/run that via cloudformation it will not delete the resources first it will simply add them as part of the stack


