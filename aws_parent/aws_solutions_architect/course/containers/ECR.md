* store/manage docker on AWS
* public/private images
* fully integrated with ECS
* IAM integration

* vulnerability scanning, image tags, image lifecycle


* ECR is region based!

* ECR supports both cross region/cross account replication
    * if you configure this, you can push image to ECR in one region and it will be replicated to other regions/accounts

* image scanning
    * scan these containers to look for vulnerabilitys
    * manual(user triggered) or automatic(scan on push)
    * two types:
        1. basic scan
            * looks for common vulnerabilities
            * free
        2. enhanced scanning
            * uses amazon inspector($$)
            * looks for operating system and programming lang vulnerabilities
            * costs money
    