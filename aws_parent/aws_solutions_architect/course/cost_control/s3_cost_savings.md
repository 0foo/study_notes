* standard GP
* standard IA
* one zone IA


* Intelligent tiering
    * will move objects between tiers to maximize cost savings
    * have to pay for each object being monitored(but ends up cheaper still)
* glacier instant retrieval
    * allows to retrieve glacier files quickly

* glacier flexible retrieval
* glacier deep archive
    * most savings but a long time to restore the file

* can define s3 lifecycle configuration
    * automatically transition objects between tiers

* compress objects before sending to s3!!


* s3 requestor pays
    * the person requesting the object will pay and not the owner
    * in general bucket owners pay for s3 storage/transfer costs
    * with this requestor pays for cost of transfer (not storage)
    * good for sharing large dataset with thousands of accounts
    * users have to be authenticated with IAM before able to download data
    * be careful of ROLES   
        * if you give cross account access to a role and that's used to query the bucket then you pay!!
