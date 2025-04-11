
Code -> Build -> Test -> Deploy -> Provision

* code: VCS like github, gitlab, ECR for docker etc.
* Build/Test: code build, jenkins, code build can build/package a new docker image!!
* Deploy/Provision: beanstalk, code deploy/EC2 fleet via cloudformation, ECS
* code pipline orchestrates all of these steps


#### General process
1. Developers push code to a repository
2. Trigger webhook
3. Build server: pulls the code and Builds the code and runs tests on it (code build, jenkins CI)
4. Gives feedback via various channels on if tests pass/fail
5. Deployment server: Once build has passed, Code is deployed (jenkins CD, code deploy, spinnaker)
* NOTE: build server and deploy server can be same or separate hosts


#### Continuous Integration
* code is tested continuously
* allows to deploy more often
* build server can run tests (which can take a long time) instead of dev's having to run on their machines



#### Continuous Delivery
* deploy often and deployments are quick
* instead of one large release every month to 5 small releases per day
* keeps each release safer with smaller surface area for bugs 
* you catch bugs a lot quicker



#### Info
* code pipeline orchestrates ALL of this
* can trigger a lambda when pushing to code commit 
    * lambda can run code 
    * example: scan code for AWS credentials and then trigger IAM to disable that credential
* code pipeline allwos a manual approval stage before deploying
* docker can be used 
    * code build will build/package the docker image then push into Amazon ECR
* Can do cloudformation deploys in cloud pipeline


#### Code pipeline/Github integration
* Code pipeline polls github
* github sends webhook
* Github has code star source connection application which does integrations and will update code pipeline