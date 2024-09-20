dnf
    list <pattern> - List packages matching pattern
    repoinfo - Show info on used repositories
    info <package> - Show info for specific package
    install <package> - Install specific package
    localinstall <path-to-package> - Install package from rpm file
    remove <package> - Remove specific package
    provides "*/bin/sh" - Find out which package provides specific file
    groups list - List available package groups
    group install "<group-name>" - Install package group
    group remove "<group-name>" - Remove package group
    history list - View dnf history
    history undo <id> - Undo action
    history redo <id> - Redo previous action
    config-manager

* /etc/dnf/dnf.conf
* `man 5 dnf.conf`

* repo's
    * /etc/yum.repos.d 

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