## SELinux


### General
* essentially a white listing tool
* apparmor is another MAC but is a blacklisting tool


### DAC vs. MAC
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



### SELinux modes
* three modes: enforcing, persmissive, disabled
    * enforcing mode: enforcing all SELinux policies
    * permissive mode: all SELinux activity is logged but no blocking is done
    * disabled mode: selinux not enabled, will not load selinux libraries on boot

* commands
    * view modes/status:
        * `sestatus` or `getenforce`
    * set mode:
        * setenforce [0 | 1]
            * switch between the two modes
                * 0 is permissive
                * 1 is enforcing
                * can't disable with this
            * this will be lost at reboot!!!
    * persistent set of status/mode
        * set in: /etc/sysconfig/selinux
        * SELINUX=enforcing
            * enforcing, disabled, permissive
        * requires reboot for this to take effect!!!


* HUGE TIP: If setting a disabled system to enabled
    * set in permissive first
    * reboot
    * view the SELinux logs to see what errors are thrown
    * fix those
    * set to enforcing


* to change modes via kernel parameter, set these kernel parameters:
    * selinux=0 or 
        * This parameter causes the kernel to not load any part of the SELinux infrastructure.
        * Red Hat does not recommend using the selinux=0 parameter. To debug your system, prefer using permissive mode. 

    * enforcing=0
        * is permissive only
        * i.e. if locked out during changing a modde from diabled => enforcing



### Context (also known as Labels) (also known as type)
* Every system resource(file, port, process etc.) has a label called an SELinux context. 
* On most file systems, SELinux labels are stored as extended attributes. This is not always the case though - some file systems do not support extended attributes. In these cases, all files on the file system get assigned the same context, usually provided through the mount option of the file system. 


* can view with -Z flag:
    * ls -alZ
    * netstat -tulanepZ
    * ps aux -Z
    * seinfo --portcon=80

* Labels are in the format `user:role:type:level` (level is optional). 
    * example: `system_u:system_r:syslogd_t:s0`
    * type is typically most important for interactions
    * ends with _t
    * examples:
        * web server: httpd_t
        * /tmp files and directory: tmp_t
        * context for files and directories normally found in webserver folders: httpd_sys_content_t
        * web port: http_port_t

* theres a huge database of mappings of file locations to contexts so when a file is created this database is consulted with the files location and the context for that location is applied to the new file
    * can view in `/etc/selinux/targeted/contexts/files`
    * can view with: `semanage fcontext -l`
    * Note: Many of these are defaul

* if you move a file it will still have the context from it's original location

* new processes, new files, etc. all inherit context's from their parents

* chcon
    * `chcon -v -t <some context>  <somefile>`
    * `chcon -v -t httpd_sys_content_t test_file.html`
    * write new context to selinux database but does NOT write to the filesystem which is persistent
    * if a file system is re-labeled you will lose the changes
    * easily overwritten
    * do not use this command


* semanage
    * ex: `semanage fcontext  -a –t httpd_sys_content_t   “/rhcelab/customwebroot(/.*)?”`
    * will add the permanant labels(contexts) to the label database for this directory
    * need to run restorecon afterwards because semanage just writes the policy and this will write to files
        * `restorecon –R –i /rhcelab/customwebroot/`
    * Any contexts added through the semanage command are placed in `/etc/selinux/targeted/contexts/files/file_contexts.local` file

* can use `man semanage-fcontext` to see these commands and type /example


* The most difficult part of setting file type context is finding right context. And the easiest solution of this problem is looking in default document root. For example, to find out the right context for web server we looked in the default document root of web server (/var/www/html). 
    * SELinux stores all contexts in /etc/selinux/targeted/contexts directory.
    * And the easiest solution of this problem is looking in default document root. For example, to find out the right context for web server we looked in the default document root of web server (/var/www/html).
        * run `ls -laZ` in the default directory for the application


* Port labels
    * `semanage port -l | grep http`
    * `semanage port -a -t http_port_t -p tcp 9980`

### There are policies(rules) that map contexts(i.e. labels) to other contexts(i.e. labels)
* a policy(rule) could allow apache process with label httpd_t to access files/directories with label httpd_sys_content_t but not tmp_t
    * limits access to a compromosed web server



* Here's a simplified example of an SELinux policy file snippet:

```te
module mymodule 1.0;

require {
    type httpd_t;
    type httpd_sys_content_t;
    class file { read write };
}

# Allow httpd_t processes to read and write to files labeled with httpd_sys_content_t
allow httpd_t httpd_sys_content_t:file { read write };

```
* Typically the SOURCES aren't installed.
* SELinux policy source files, such as the example module, are typically located in:

- `/etc/selinux/targeted/src/policy/` (if the policy sources are installed).

* Individual policy modules can also be loaded and managed using tools like `semodule`, which operates on compiled modules in:

- `/etc/selinux/targeted/modules/active/modules/`.


* add a policy with: `selocal -a "allow nsh_t nsh_t:memprotect mmap_zero;" -Lb`

* When the enhancements are frequent, it is better to create a SELinux policy module ourselves that contains the rule(s) and load it:

```bash
root #vim mynsh.te

policy_module(mynsh, 1.0)

gen_require(`
  type nsh_t;
')

allow nsh_t nsh_t:memprotect mmap_zero;

root #make -f /usr/share/selinux/strict/include/Makefile mynsh.pp
root #semodule -i mynsh.pp
```


### Relabel filesystem
* You can force the system to automatically relabel the filesystem by creating an empty file named .autorelabel in the / directory and then rebooting

* can also: `fixfiles -F onboot`
    * will create the .autorelabel file for you

* If the system has too many errors, you should reboot while in permissive mode in order for the boot to succeed. 
* After everything has been relabeled, set SELinux to enforcing with /etc/selinux/config and reboot, or run setenforce 1. 

* Before rebooting the system for relabeling, make sure the system will boot in permissive mode, for example by using the enforcing=0 kernel option. This prevents the system from failing to boot in case the system contains unlabeled files required by systemd before launching the selinux-autorelabel

* As for fixfiles, it's a wrapper for restorecon.
* When /.autorelabel is present, the init script runs `restorecon -p -r` 

* restorecon
    * will map all file labels(contexts) to their default settings in selinux database defined in `/etc/selinux/targeted/contexts`
    * this is persistent NOT temporary


### Booleans
* TBD


### Logging
* SELinux messages can be stored on several locations for examples: -
    * If auditd daemon is running, SELinux will log the messages in /var/log/audit/audit.log file.
        * query with audit log tool ausearch
        * `ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts recent`
            * -m flag is an OR operation and will return entries matching any of those types
            * -ts is time flag
    * In case auditd is running, but there are no matches in the output of ausearch, check messages provided by the systemd Journal:
        * `journalctl -t setroubleshoot`
    * If SELinux is active and the Audit daemon is **not** running on your system, then search for certain SELinux messages in:
        1.  the output of the dmesg command: `dmesg | grep -i -e type=1300 -e type=1400`
        2. the rsyslog daemon to log the messages in /var/log/messages.
        3. the log journal: `journalctl -t setroubleshoot`

* SELinux logs each activity in /var/log/audit/audit.log file with a type=AVC (Access Vector Cache) tag. To view all SELinux messages on screen we can use following command:
        * `ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts recent`


* can install: `yum -y install setroubleshoot-server`
    * After reboot whenever an SELinux message is written in audit.log file, a simplified human version of same message is also written in /var/log/messages.


### Logging part 2
* journalctl and dmesg will typically heavily format SELinux errors in the logs to make them blaringly obvious, and tools like setroubleshoot and audit2allow make it very easy to identify possible fixes or to ask SELinux "please permenantly allow the thing you just blocked".

* Here's what a common SELinux error might be :
    * `journalctl -t setroubleshoot --since=14:20`

```
-- Logs begin at Fri 2016-01-15 01:17:17 UTC, end at Thu 2016-02-18 14:25:21 UTC. --
Feb 18 14:24:24 setroubleshoot[866]: SELinux is preventing httpd from append access on the file
error_log. For complete SELinux messages. run sealert -l e9d8fa2e-3608-4ffa-9e72-31a1b85e460b
```

* You then literally do the thing the log instructs....

* `sealert -l e9d8fa2e-3608-4ffa-9e72-31a1b85e460b`
```SELinux is preventing httpd from open access on the file /var/log/httpd/error_log.

***** Plugin restorecon (99.5 confidence) suggests   **************************

If you want to fix the label.
    `/var/log/httpd/error.log default label should be httpd_log_t.`
    Then you can run restorecon.
    Do
    `# /sbin/restorecon -v /var/log/httpd/error_log`
```
* And it tells you exactly how to fix it. 
* Very often there is a seboolean that you can simply toggle to fix the problem, or if that fails an option for audit2allow:

`sealert -l 4ae65592-42a8-4141-8977-fdef20ee84aa`
SELinux is preventing plugin-containe from using the dac_override capability.
*****  Plugin mozplugger (87.7 confidence) suggests   ************************
If you want to use the plugin package
Then you must turn off SELinux controls on the Firefox plugins. Do
* `setsebool -P unconfined_mozilla_plugin_transition 0`

*****  Plugin dac_override (12.1 confidence) suggests   **********************
If you want to help identify if domain needs this access or you have a file with the wrong permissions on your stem
Then turn on full auditing to get path information about the offending file and generate the error again.
Do

Turn on full auditing
* `auditctl -w /etc/shadow -p w`
Try to recreate AVC. Then execute
* `ausearch -m avc -ts recent`
````
    If you see PATH record check ownership/permissions on file, and fix it, otherwise report as a bugzilla.

    *****  Plugin catchall (1.66 confidence) suggests   **************************
    If you believe that plugin-containe should have the dac_override capability by default.
    Then you should report this as a bug.
    You can generate a local policy module to allow this access.
    Do
    allow this access for now by executing:
    * `ausearch -c 'plugin-containe' --raw | audit2allow -M my-plugincontaine`
    * `semodule -X 300 -i my-plugincontaine.pp`
```

* via this aweseome reddit thread: [link](https://old.reddit.com/r/linuxadmin/comments/lwwgyv/why_its_time_to_stop_setting_selinux_to/)
----




### TBD
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



### Mode

* enabling SELinux requires a reboot of the system because SELinux is so interwoven with the kernel



* do not change the contents of the /etc/sysconfig/selinux file on the exam!!!
    * having selinux enabled is crucial part of exam
* can put selinux in permissive mode setenforce=0 which is not permissive so can reboot



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


    * https://www.computernetworkingnotes.com/linux-tutorials/selinux-explained-with-examples-in-easy-language.html