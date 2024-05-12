### RPM's


* was the package installer used previous to yum 
* works on single package at a time
* will not resolve dependencies
    * have to manage/install dependencies yourself
    * sometimes have to install entire chains of dependencies
* yum command considers all dependencies and rpm command no longer needed for package installation
* to install a package
    * modern way: yum install <packagename>
        * resolves dependencies
        * yum localinstall is legacy version of this command
    * old way: rpm -Uvh <packagename>
        * does not resolve dependencies

* two package databases are maintained, yum and rpm
    * if install package with yum, rpm database will be updated
    * if install package with rpm, yum database will NOT be updated
    * so always install via yum and no longer use RPM for package installation

* rpm filename
    * <packagename>-<version>-<subversion>-<redhat version this package was targetted for>-<platform package creatd for>
    * ex: autofs-5.0.7-40.el7.x86_64.rpm

* rpm command is great for querying packages still

* rpm -qa
    * list all installed packages
    * similar to yum list installed


* rpm -q flag queries the rpm database
    * queries packages already installed on system
    * rpm -q<flag> <packagename>
        * -qi 
            * list info about package
        * -ql
            * list all files in package
        * -qd
            * get all documentation files
        * -qc 
            * get all configuration files
        * -qR
            * get all package dependencies
        * -V   
            * which parts of package have changed since installation
* rpm -Va 
    * verifies all installed packages and shows which parts have been changed since install
    * easy way to do a package integrity check
         

* Can point rpm to a file on the file system to see what packages it was installed with
    * rpm -qf <filename>
    * rpm -qf /bin/ls


* rpm -qp flag queries a package file
    * rpm -qp <package>
    * used to look at package files before installation
    * need to use complete filename
    * rpm -qp --scripts
        * queries the package for any scripts
        * useful to find out if the package about to install contains any scripts 
    * only woks on package files, does not look at repositories

* repoquery 
    * allows querying the package in the repos
    * part of yum-utils package
    * similar flags as rpm 
    * no --scripts flag, have to download the package file first

* yumdownloader
    * in yum-utils package
    * allows downloading just the package file from the repos

