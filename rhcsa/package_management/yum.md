
### To define a link to a new repository 

* you can either add a [repository] section to the /etc/yum.conf file, 
* or to a .repo file in the /etc/yum.repos.d/

* bare minimum yum repofile definition

```
[repository]
name=repository_name
baseurl=repository_url
```


* name: name of repo
* baseurl: protocol prefixed url of repository
* mirrorlist: url for accessing info on mirror server
* gpgcheck/gpgkey: for digital signing of repo
    * gpgkey is used to sign the packages
    * keys for repo's gpg keys are here:
        * /etc/pki/rpm-gpg





### to create the actual repository

* in the folder you're interested in making a repo:
    * add all files you want
    * createrepo --database /mnt/local_repo
    * creates metadata and sqllite file



### using yum

* yum search <keyword of packagename or summary>
    * search in title of the package and package summary


*  yum provides "*/<filename>"
    * searched for a yum package with a filename
    * provides includes directory in search so:
        * will need to specify filename as */ or use full path to filename
* yum whatprovides 
    * exact same command as yum provides
    * `yum whatprovides */semanage*``


* yum info
    * get's info on a package
* yum install -y
* yum remove
* yum repolist
    * show list of repositories you're currently using
* yum list: list package names from repositories
    * yum list available
        * List all available packages
    * yum list installed
        * List all installed packages
    * yum list all
        * List installed and available packages
    * yum list kernel
        * List installed and available kernel packages
    * yum list <packagename>
        * info about available packagename versions and if installed or not
* yum update
    * updates packages
    * will replace old with new package
    * kernel is not replaced, another is added in the kernel folder
* yum history
    * yum history undo <action number>
        * allows undoing an action from yum
        * yum history has all of the action numbers



* repoquery --list package_name
    * list all files available in a package


### yum package groups
    * basically allows managing packages relating to a specific topic
        * webserver with plugins, operating system, security tools, 

    * Three kinds of package groups exist:
        * environment package groups:
            *  describe a type of global configuration containing other package groups: Minimal Install,  Compute Node, Infrastructure Server, GNOME Desktop, etc.
        * top-level package groups:
            * bring a set of package groups belonging to the same domain: Security Tools, Development Tools, System Administration Tools, etc.
        *simple package groups:
            contain packages on a particular topic: web-server, network-file-system-client, etc.
    

    * Also, inside a package group, there are potentially three different categories:
        * mandatory package groups/packages are always installed.
        * default package groups/packages are normally installed except if Xspecified otherwise.
        * optional package groups/packages are only installed on demand.

    * yum groups list
        * environment groups with basic functionality
        * add ids or -v for unique identifier called group id
            * yum groups list ids
            * yum groups list -v
        * group id allows you to install/remove without group command using an at symbol
            * yum install @somegroup
    * yum groups list hidden
        * displays different environment subgroups
    * yum groups info <some group name>
        * gives list of packages in the group
    * yum groups install
    * yum groups remove




### yum module
* set of RPM packages that belong together and all dependencies for a SPECIFIC VERSION
* a stream is a specific version for that package
    * only one stream can be active at a time
* a profile is a set of packages for that module
    * can have default profile, minimal profile, server profile, etc, etc
* two module repositories
    * baseOS
        * provides OS modules
    * Application Stream
        * provides application modules


* yum module list
    * list all modules
* yum module list <modulename>
    * see the streams available for that module
* yum module info <modulename>
    * can get info of specific profiles
* yum module info <modulename>:<version/stream>
    * info on profiles in specific streams
    * yum module info perl:5.26
* yum module enable perl:5.24
    * enable a stream
* yum module install
    *