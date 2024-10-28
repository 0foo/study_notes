#### rpm
* `man rpm`
    * can find query options to pair with `rpm -q`
    * `rpm -ql`, `rpm -qc`, `rpm -qi`
* `rpm -q`
* You can extract files from an RPM package file without installing the package with `rpm2cpio` and `cpio`
    * rpm2cpio package-name.rpm | cpio -idmv

#### dnf
* list <pattern>
    * lists installed or availabled(i.e. not installed but available via repo)
* search 
    * searches in name and summary fields ONLY
* provides "*/bin/sh" 
    * Find out which package provides specific file
* install|update|info|remove
* localinstall <path-to-package> - 
    * Install package from rpm file
* list kernel
    * to list all installed and available kernels.

#### repos
* `repoinfo`
    * Show info on currently enabled repositories
* `repolist all`
    * shows all possible repos
* `config-manager --enable rhel-8-server-debug-rpms`
* add a repo with a cli command:
    * `config-manager --add-repo="https://dl.fedoraproject.org/pub/epel/8/Everything/x86_64/"`
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




    config-manager

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