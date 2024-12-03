### Know


### Tips
* can run `man semanage-fcontext` and search `/example`to see examples


### summary
---
* install setroubleshoot-server package;
    * listens for audit messages in /var/log/audit/audit.log and sends a short summary to /var/log/messages.

* troubleshoot
    1. `systemctl status` logs (journalctl -u)
    2. `sealert -a /var/log/audit/audit.log`
    3. `tail /var/log/messages | grep 'SELinux'` 
        * needs setroubleshoot-server installed
        * Run the sealert command if given

* viewing contexts
    * ls -lZ: what things currently are
    * `semanage fcontext -l | grep <some directory>`: what they are supposed to be

* repair
    * run `restorecon` on things that have incorrect context to restore their context
        * `-Rv` flags for recursive and verbose
    * `man semanage-fcontext`  
        * can change the context on a folder 
        * for example if you want an httpd folder outside of traditional location

* file locations
    * `/etc/selinux/config`

* ports
    * `man semanage-port` (list,add,update,delete)

* temporary change context 
    * `man chcon`

### SELinux
-----
getenforce
setenforce
sestatus

* if either of these is disabled selinux is disabled
    * /etc/selinux/config
    * kernel param: selinux=0, enforcing=0
        *  /etc/default/grub
        * also:           grubby --update-kernel ALL --args selinux=0 

 ls -Z
 ps -eZ | grep process_name

/etc/selinux/targeted/contexts/files/file_contexts.local

chcon -R -t httpd_sys_content_t /repo-write
restorecon /path/to/file_or_directory
restorecon -Rv /var/www/html

selinux files: man semanage-fcontext
selinux ports: man semanage-port

getsebool -a
setsebool boolean_name on
setsebool -P boolean_name on (permanant)

### Other troubleshooting 
* `journalctl -t setroubleshoot`: note: may not persist between boots if not configured
* `cat /var/log/audit/audit.log | grep denied`
* `ausearch -m avc -ts recent`: raw search of audit logs(-ts is flag for time recent)
* `sealert -a /var/log/audit/audit.log` : gives human readable selinux info
    * sometimes sealert will have a follow up command to run in output

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
    * `semanage boolean -l`

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


* ports
    * `semanage port -l | grep http`: view
    * `semanage port -a -t http_port_t -p tcp 82`: add (note can use -d or -m instead for delete/modify)



    * backup: 
        * * `ausearch -m avc -ts recent`: raw search of audit logs(-ts is flag for time recent)

