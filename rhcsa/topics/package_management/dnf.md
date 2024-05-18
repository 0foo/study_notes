### DNF
* built on top of RPM's and also handles dependencies
* dnf invokes the rpm utility in the background and can perform numerous operations on individual packages or package groups
    * such as listing, querying, installing, and removing them.
* yum is old version of this and has been removed and everything yum related is simply symlinked to co-oresponding DNF files
* main dnf config file is /etc/dnf/dnf.conf
    * old /etc/yum.conf is symlinked from this
        * best: Specifies whether to install (or upgrade to) the latest available version
        * clean_requirements_on_remove: Defines whether to remove dependencies during a package removal process that are no longer in use
        * debuglevel: Sets the level between 1 (minimum) and 10 (maximum) at which the debug is to be recorded in the logfile. Default is 2. 
            * A value of 0 disables this feature.
        * gpgcheck: Indicates whether to check the GPG signature for package authenticity. Default is 1 (enabled).
        * installonly_limit: Specifies a count of packages that can be installed concurrently. Default is 3.
        * keepcache: Defines whether to store the package and header cache following a successful installation. Default is 0 (disabled).
        * logdir: Sets the directory location to store the log files. Default is /var/log.
        * obsoletes: Checks and removes any obsolete dependant packages during installs and updates. Default is 1(enabled)
    * for more conf directives run: `man 5 dnf.conf`


### Repo files
* a repo is a remote package storage location

* repos stored in: /etc/yum.repos.d directory
        * can change this is /etc/yum.conf

* create a file that ends with extension .repo
* can add more than one repository in a file

* you can either add a [repository] section to the /etc/yum.conf file, 
* or to a .repo file in the /etc/yum.repos.d/

* Each repository definition file must have a unique ID, a description, and a baseurl directive defined at a minimum;

```
[unique ID]
name=rdescription
baseurl=repository_url
```

* example repo file
```
[BaseOS_RHEL_9]
name= RHEL 9 base operating system components
baseurl=file:///mnt/BaseOS
enabled=1
gpgcheck=0
```

* []: inside the brackets is a unique key indentifier for the repository
* name: description
* baseurl: protocol prefixed url of repository: http(s)://, ftp://, file://(for local)
* mirrorlist: url for accessing info on mirror server
* gpgcheck/gpgkey: for digital signing of repo
    * gpgkey is used to sign the packages
    * keys for repo's gpg keys are here:
        * /etc/pki/rpm-gpg
* enabled: if repo is enabled or not



### to create the actual repository

* in the folder you're interested in making a repo:
    * add all files you want
    * createrepo --database /mnt/local_repo
    * creates metadata and sqllite file



### remote repo management
* `sudo dnf repolist -v`
    * lists all available repos setup locally

* `sudo dnf repoquery`
    * lists every package available in every repo
    * can filter with grep
    * can filter with --repo flag
        * `sudo dnf repoquery --repo "BaseOS"`
    * can pass in a package name
        * `sudo dnf repoquery cifs-utils`

* `sudo dnf list`
    * lists all installed and non-installed remote packages available for install
    * the @ sign means it's installed

* `sudo dnf list wget`
    * This command will check if the wget package is available in the configured repositories and provide details about it if found.
    * If not found will not return any info 
    * If wget is installed, it will show the installed version. 
    * If it's available but not installed, it will list it as available for installation. 
    * If wget is not found in the repositories, the command will not return any information.

* `sudo dnf info <some package name>`
    * displays info about a package
    * will display info even if not installed or installed

### local package mangement
* `sudo dnf list installed`
    * lists package name, version, repo installed from
    * @anaconda repo means installed at time of RHEL installation
    * can further filter by passing a name
        * `sudo dnf list installed gnome*`

* `sudo dnf check-update`
    * lists all packages installed that can be updated
    * does not do any updates, just lists
    * shows the current installed package plus package in the repos
    * nice to compare the two and see what to update

* `sudo dnf update`
    * updates all installed packages
    * pass -y for no prompt

* `sudo dnf update <somepackagename>`
    * updates a specific package
    * will fail if not already installed

* `sudo dnf install <somepackage>`
    * installs a package from repos
    * if package is already installed will update it to latest version
    * -y for no prompt
    * installs dependencies from remote repos

* `sudo dnf localinstall <rpm file name>`
    * installs a package from an rpm filex
    * installs dependencies if they are present in the local directory or prompts for manual installation if dependencies are missing.


* `sudo dnf remove <some package name>`
    * removes a package from the local system if no other packages are depending on it
    * If other packages depend on <package-name>, DNF will typically prevent its removal and prompt you with a message indicating that removing <package-name> would break dependencies of other installed packages.
    * You can choose to proceed with the removal, which would then also remove those dependent packages. 
    * will removes of of removed packages dependencies IF those dependencies NOT BEING USED by other packages
