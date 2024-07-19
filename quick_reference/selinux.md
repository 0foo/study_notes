
* Get the current SELinux mode `getenforce`
* Display detailed SELinux status `sestatus`

* Change selinux status 
    * `setenforce 1`
    * `setenforce 0`
    * `sudo vi /etc/selinux/config`  or the symlink: `/etc/sysconfig/selinux`
    * enforcing=0 or selinux=0 


* view the current SELinux context of a resource
    * ls -Z, netstat -Z, ps aux -Z

* view selinux mappings
    * entire database: `semanage fcontext -l`
    * custom defined: `/etc/selinux/targeted/contexts/files/file_contexts.local`

* Temporarily change the SELinux context
    * `chcon -t <type> /path/to/file`

* Permanantly change the SELinux context
    * `semanage fcontext -a -t type '/path/to/directory(/.*)?'`
    * `semanage fcontext -d '/path/to/directory(/.*)?'`
    * `restorecon -Rv /path/to/directory`
    * can run `man semanage-fcontext` and search `/example`to see examples

* Permanantly relabel filesystem to settings in database
    * create file: `.autorelabel` in boot (runs `restorecon -p -r` )
    * `fixfiles -F onboot`  (will create .autorelable for you)
    * `restorecon /path/to/file`
    * `restorecon -R /path/to/directory`

* Booleans (`man booleans`)
    * `getsebool -a`
    * `getsebool httpd_enable_homedirs`
    * `setsebool httpd_enable_homedirs on`
    * `setsebool -P httpd_enable_homedirs on`

* policy modules
    * `semodule -i mymodule.pp`
    * `semodule -l`
    * `semodule -r mymodule`

* logging
    * `ausearch -m avc -ts recent`
    * `aureport -a`
    * `ausearch -c httpd`
    * `ausearch -m avc -ts recent | audit2why`
    * `ausearch -m avc -ts recent | audit2allow -M mymodule`
    * `semodule -i mymodule.pp`
* if no audit daemon:
    * `journalctl -t setroubleshoot`
    * `dmesg | grep -i -e type=1300 -e type=1400`




