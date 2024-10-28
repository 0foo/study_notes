### Essentials/tips
* Always run dnf update after changing dnf repo files

#### rpm
* `man rpm`
    * can find query options to pair with `rpm -q`
    * `rpm -ql`, `rpm -qc`, `rpm -qi`
* `rpm -q`
* You can extract files from an RPM package file without installing the package with `rpm2cpio` and `cpio`
    * rpm2cpio package-name.rpm | cpio -idmv

#### dnf
* search: `list|search|provides|info`
* `update|install|remove`
* list <pattern>
    * lists installed or availabled(i.e. not installed but available via repo)
* search 
    * searches in name and summary fields ONLY
* provides "*/bin/sh" 
    * Find out which package provides specific file
* install|update|info|remove
* list kernel
    * to list all installed and available kernels.

#### repos
* `repoinfo`
    * Show info on currently enabled repositories
* `repolist all`
    * shows all possible repos
* enable/disable repo via cli
    * `man dnf config-manager`
* add a repo with a cli command:
    * `man dnf config-manager`
    * creates the file!!
* `/etc/yum.repos.d/`

#### logging/history
* `/var/log/dnf.rpm.log`
* history list - View dnf history
* history undo <id> - Undo action
* history redo <id> - Redo previous action

#### dnf groups
* groups list - List available package groups   
* group install "<group-name>" - Install package group
* group remove "<group-name>" - Remove package group


### modules
* `dnf module list|info|disable|enable|reset|install`

* there's the default system stream that will run without any other modules enabled
* `dnf module list --installed|--available`
* `dnf module info <module>`: view streams and profiles

* `dnf enable python36:3.6/common`
    * just enables
    * when you enable a module, all packages tagged in that module will use that module during install
    * running `dnf install python` will use this stream and not the system stream
    * to cancel this and go back go default system stream use RESET and not DISABLE
    * if switching streams it's your responsibility to remove the modules provided by the module stream first

* `dnf module reset python36`
    * resets the python module and goes back to the system stream
    * the reverse of `dnf enable`
    * if switching streams it's your responsibility to remove the modules provided by the module stream first

* `dnf module install<name>:<stream>/<profile>`
    * * `dnf module install python36:3.6/common`  : name:stream/profile
    * will install ALL packages in that profile/stream

* `yum module remove postgresql`
    * Removing a module removes all of the packages/dependencies installed by profiles of the currently enabled module stream
    * if switching streams it's your responsibility to remove the modules provided by the module stream first

* config-manager

* /etc/dnf/dnf.conf
* `man 5 dnf.conf`

#### repo's
* `repoinfo`
    * Show info on currently enabled repositories
* `repolist all`
    * shows all possible repos
* `config-manager --enable rhel-8-server-debug-rpms`
* `/etc/yum.repos.d/`


    ```
    [BaseOS_RHEL_9]
    name= RHEL 9 base operating system components
    baseurl=file:///mnt/BaseOS
    enabled=1
    gpgcheck=0zzz
    ```
    ```
    [BaseOS_RHEL_9]
    name= RHEL 9 base operating system components
    baseurl=file:///mnt/BaseOS
    enabled=1
    gpgcheck=1
    gpgkey=http://example.com/remote/repo/RPM-GPG-KEY
    ```
* managing repos
    sudo vi /etc/yum.repos.d/myrepo.rep
    sudo dnf --enablerepo=myrepo install <package>
    sudo dnf --disablerepo=myrepo install <package>
    sudo dnf repolist all - List available repositories
    sudo dnf repoinfo myrepo

* creating a local repo
    sudo createrepo /path/to/local/repo




### Module purpose
