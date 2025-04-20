### Types of tags

* custom allocation tags just appear in the billing console
* takes about 24 hours for tags to appear in billing reports

* AWS generated tags
    * starts with prefix aws:
    * not applied to resources created before the activation of these tags so no retroactive tagging
    * extends cost tracking functionality by adding tags to track additional things
        * aws:servicecatalog:provisioningProduct
        * cloudformation stack name
        * createdBy
        * and more



* user defined tags
    * custom tags user create   
    * define with prefix user:
    * can define custom tags like application, team, environment, etc.


### Tag editor
* Find resources to tag
* has a search function where you can target groups of resources
* bulk tag add/update/remove to these resources
* search tag/untagged resources in all aws regions
* 