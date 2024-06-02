## SELinux

### DAC and MAC
* Discretionary Access Control(DAC): standard historical linux access control with chmod, chown, etc.
    * With DAC, files and processes have owners. You can have the user own a file, a group own a file, or other, which can be anyone else. Users have the ability to change permissions on their own files.
    * The root user has full access control with a DAC system. If you have root access, then you can access any other user’s files or do whatever you want on the system. 

* Mandatory Access Control (MAC): Access control done by SELinux
    * overrides DAC, even if DAC sets a permissions MAC can override it if they conflict
    * SELinux policy rules are checked after DAC rules. SELinux policy rules are not used if DAC rules deny access first, which means that no SELinux denial is logged if the traditional DAC rules prevent the access. 

### Security
* DAC rules processed
* MAC rules processed override DAC if conflict
* The default action is deny. If an SELinux policy rule does not exist to allow access, such as for a process opening a file, access is denied. 


### Context (also known as Labels) (also known as type)
* Every process and system resource has a special security label called an SELinux context. 

* Identifier which abstracts away the system-level details and focuses on the security properties of the entity.

* Labels are in the format user:role:type:level (level is optional). 
    * type is typically most important for interactions
    * ends with _t
    * examples:
        * web server: httpd_t
        * /tmp files and directory: tmp_t
        * context for files and directories normally found in webserver folders: httpd_sys_content_t
        * web port: http_port_t

* a rule could allow apache process: httpd_t to access files/directories in httpd_sys_content_t but not tmp_t
    * limits access to a compromosed web server

* to determine what context to add, can look at similar items

* add context
    1. semanage fcontext -a -t httpd_sys_content_t "/mydir(/.*)?"
        * -a flag for add
        * this writes only to policy and not to filesystem
    1. restorecon -R -v /mydir
        * add to filesystem, change is now permanant

* if 



### Examples
* As the previous scheme shows, SELinux allows the Apache process running as httpd_t to access the /var/www/html/ directory and it denies the same process to access the /data/mysql/ directory because there is no allow rule for the httpd_t and mysqld_db_t type contexts. On the other hand, the MariaDB process running as mysqld_t is able to access the /data/mysql/ directory and SELinux also correctly denies the process with the mysqld_t type to access the /var/www/html/ directory labeled as httpd_sys_content_t. 


### Relabel filesystem
* You can force the system to automatically relabel the filesystem by creating an empty file named .autorelabel in the / directory and then rebooting
    * If the system has too many errors, you should reboot while in permissive mode in order for the boot to succeed. 
    *  After everything has been relabeled, set SELinux to enforcing with /etc/selinux/config and reboot, or run setenforce 1. 
* fixfiles -F onboot
    * will create the .autorelable file for you

* Before rebooting the system for relabeling, make sure the system will boot in permissive mode, for example by using the enforcing=0 kernel option. This prevents the system from failing to boot in case the system contains unlabeled files required by systemd before launching the selinux-autorelabel

### Mode

* enabling SELinux requires a reboot of the system because SELinux is so interwoven with the kernel

* enforcing mode vs permissive
    * enforcing mode: enforcing all SELinux policies
    * permissive mode: all SELinux activity is logged but no blocking is done
    * disabled mode: disabl SELinux
    * getenforce
        * check if in enforce or permissive mode
    * setenforce [0 | 1]
        * switch between the two modes
    * persistent set of mode
        * set in: /etc/sysconfig/selinux
        * SELINUX=enforcing
            * disabled, permissive

* do not change the contents of the /etc/sysconfig/selinux file on the exam!!!
    * having selinux enabled is crucial part of exam
* can put selinux in permissive mode setenforce=0 which is not permissive so can reboot


* set these kernel parameters:
    * selinux=0 or 
        * This parameter causes the kernel to not load any part of the SELinux infrastructure.
        * Red Hat does not recommend using the selinux=0 parameter. To debug your system, prefer using permissive mode. 

    * enforcing=0
        * is permissive only
        * i.e. if locked out during changing a modde from diabled => enforcing



* If setting a disabled system to enabled
    * set in permissive first
    * reboot
    * view the SELinux logs to see what errors are thrown
    * fix those
    * set to enforcingx

### Management

* booleans are on/off setting for SELinux
    * getsebool -a 
    

* sestatus -v
    * detailed info about current selinux status
* getenforce
    * returns Enforcing, Permissive, or Disabled

* logfile
    * /var/log/audit/audit/log



* config file
    * /etc/sysconfig/selinux



* SELinux elements
    * Policy: A collection of rules that define which source has access to which target.
    * Source domain: The object that is trying to access a target. Typically a user or a process.
    * Target domain: The thing that a source domain is trying to access. Typically a file or a port.
    * Context: A security label that is used to categorize objects in SELinux.
    * Rule: A specific part of the policy that determines which source domain has which access permissions to which target domain.
    * Labels: Same as a context label, defined to determine which source domain has access to which target domain.


* semanage
    * writes the new context to SELinux, and from there it's applied to the filesystem
* chcon
    * write new context to policy but NOT to the filesystem
    * if a file system is re-labeled you will lose the changes
    * easily overwritten
    * do not use this command


### Logging
* audit messages are logged to the /var/log/audit/audit.log can search with "ausearch" command
    * ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts today

* if auditd not running selinux will log some messages to dmesg
    * dmesg | grep -i -e type=1300 -e type=1400

* if setroubleshoot-server package installed can look in /var/log/messages
    * grep "SELinux is preventing" /var/log/messages

* Access rules are cached in AVC(access vector cache) to speed up rule checking/increase performance
* audit messages are logged to the /var/log/audit/audit.log and they start with the type=AVC string.


    ### References
    * https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_selinux/getting-started-with-selinux_using-selinux