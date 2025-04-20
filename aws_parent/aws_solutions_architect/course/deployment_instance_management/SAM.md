* framework for developing serverless applications
* all the code in yaml
* can create all kinds of resources for developing an application
* can also help you run all of these resources
* SAM uses code deploy internally to deploy lambda functions with traffic shifting - VERY IMPORTANT TO KNOW
* uses cloudformation in the backend

* SEE CICD SAM architecture diagram in the architectures folder

* codepipeline + codecommit + code build -> cloudformation + deployable lambda zip file with depdencies etc.

* code build
    * It builds the Lambda code.
    * It generates a deployable CloudFormation template via the SAM packaging process.

* SAM + Cloudformation is then run to deploy this and create resources

* code deploy then traffic shifts from v1 to v2 of the lambda

