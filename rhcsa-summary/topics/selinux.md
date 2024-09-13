### Primary commands
* setenforce 1 or 0
* sestatus
* ls -Z
* sudo semanage fcontext -a -t httpd_sys_content_t "/repo-write(/.*)?"
* sudo restorecon -R /repo-write
* sudo chcon -R -t httpd_sys_content_t /repo-write


* sestatus
* /etc/sysconfig/selinux symlink to /etc/selinux/config
    * SELINUX=
    * reboot
* kernel param: selinux=0, enforcing=0
* ls -Z
* semanage fcontext -l 
* /etc/selinux/targeted/contexts/files
* /etc/selinux/targeted/contexts/files/file_contexts.local
* `chcon -v -t <some context>  <somefile>`
* `chcon -v -t httpd_sys_content_t test_file.html`
* `semanage fcontext  -a –t httpd_sys_content_t   “/rhcelab/customwebroot(/.*)?”`
* `restorecon –R –i /rhcelab/customwebroot/`
* `man semanage-fcontext`
* Port labels
    * `semanage port -l | grep http`
    * `semanage port -a -t http_port_t -p tcp 9980`
* `fixfiles -F onboot` creates -> `.autorelabel` which calls -> `restorecon -p -r` 

* `chcon -R --reference=/var/www/html /path/to/target/folder`
    *  sets the SELinux context of /path/to/target/folder (and all files and directories within it, due to the -R flag) to match the context of /var/www/html.
    * quick shortcut
* One easy way to tell which SELinux related configuration has to be done, is through sealert command. This command is used to diagnose SELinux denials and attempts to provide user friendly explanations for a SELinux denial and recommendations for how one might adjust the system to prevent the denial in the future.
    * sealert -a /var/log/audit/audit.log

### More
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




