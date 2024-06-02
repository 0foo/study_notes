
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
    
### remote repo management
* `sudo dnf repolist -v`
    * lists all available repos setup locally

* `sudo dnf repoquery`
    * lists every package available in every repo
    * can filter with grep
    * can filter with --repo flag
        * `sudo dnf repoquery --repo "BaseOS"`

* `sudo dnf list`
    * lists all installed and non-installed remote packages available for install
    * the @ sign means it's installed


### local package mangement
* `sudo dnf list installed`
    * lists package name, version, repo installed from
    * @anaconda repo means installed at time of RHEL installation



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