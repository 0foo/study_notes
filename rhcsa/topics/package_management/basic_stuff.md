point of package repositories
* easy to keep updated
* helps with resolving dependencies for a package


* cannot mix repository operating systems
    * i.e. cannot mix centos and redhat or debian, etc

* Cross OS repository: extended packages for enterprise linux (EPEL) repositories 


* have to register red hat to get repository access
    * uses subscription-manager tool

* subscription-manager tool
    * subscription-manager register
    *    allows registering a system
    * subscription-manager list --available
        * see what subscriptions your account is entitled to
    * subscription-manager attach auto
        * attaches a subscription to available repositories
    * subscription-manager consumed
        * see what subscriptions your account has used
    * subscription-manager unregister
        * unregister a system from a subscription to free up license


* have to register and attach system 
* after register and attach entitlement certificates written to these directories
    * /etc/pki
    * /etc/pki/product
        * idicate which products installed on this system
    * /etc/pki/consumer
        * indicate identify redhat account to which system is registered
    * /etc/pki/entitlement
        * info about which subscriptions are attched to this system


* configuring custom repos
    * main yum config file is /etc/yum.conf
    * repos stored in: /etc/yum.repos.d directory
        * can change this is /etc/yum.conf
    * create a file that ends with extension .repo
    * can add more than one repository in a file
