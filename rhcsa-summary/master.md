### At start of exam
* setup ssh instead of using VM terminal
* dnf -y install setroubleshoot
* maybe: dnf install screen
* run `mandb &`


### Misc
* create a file: 
  * allocate space, no writing, faster: `fallocate -l 100M`
  * allocate space and write to file, slower`dd if=/dev/zero of=/swapfile bs=1M count=1024 && chmod 600 /swapfile`

* backslash before command \rm will use an unaliased command
* find out if a command is an alias: type <command>
* Always use visudo to edit the sudoers file
* sudo will not run any alias or function even root as it does not include any env context
* get all aliases with `alias` command
* `file` command to tell which type of file it is
* use `zcat` or `zless` to read zipped files!
* math: 
  * integers: `expr 56276 + 73768` (+,-,/ works but have to escape * in this)
  * doubles: `echo "4.2 * 2" | bc` or just use `bc`/ quit or cntrl+d to exit
* `mkdir -p`  will recursive create directories!
* shortcuts:
  * `cntl+c`: sigint: terminate process
  * `cntr+z`: SIGTSTP: pauses and puts in backgroup 
  * `cntrl+d`:EOF - End of File to interactive session, can typically use instead of typing quit or exit
* dollar sign args:
  * $0(name of script file)
  * $1..., - single arguments passed to function
  * $*, $@ - full argument list passed to function
  * $?, - exit status of last command
  * $$ - proc id of the current shell
* `lsof /some/dir/ectory` : find out what procs are using this directory(delve more into sometime)
* binary vs decimal system
  * Binary system (Mebibyte - MiB, Gibibyte - GiB, etc.):
      * 1 MiB = 1,048,576 bytes
      * 1 GiB = 1,073,741,824 bytes

  * Decimal system (Megabyte - MB, Gigabyte - GB, etc.):
      * 1 MB = 1,000,000 bytes
      * 1 GB = 1,000,000,000 bytes

* run endless process: `sha1sum /dev/zero`
* `ls -d [ei]*`
  * pass -d to not descend into subdirectories when ls encounters a directory
  * should be default!

### NFS/AutoFS
* show all remote mounts for a server
* mount an nfs share via cli
* mount an remote fs permanantly in fstab
* mount an remote fs permanantly via autofs
* Configure autofs(chatgpt what is needed for this: this is from exam objective)
* Mount and unmount network file systems using NFS


### Logging
* journald, journalctl, ausearch


### Systemd
* systemctl
    * enable, mask, isolate, get-default/set-default
* /etc/systemd/system/
* list all target units
* list all service units
* Boot systems into different targets manually
* 

### journald
* TBI

### DNF
* example repo files @ /etc/yum/yum.repos.d

### general-networking
* hostnamectl
* resolvers
    * never modify /etc/resolv.conf directly!
    * nmcli connection modify <connection-name> ipv4.dns "<DNS-Server-IP>"  
        * nmcli connection reload 
        * systemctl restart NetworkManager
    * /etc/resolve.conf
    * /etc/hosts

### selinux
* Primary commands
    * `sestatus`
    * `setenforce 1` or `0`
    * `ls -Z`
    * `sudo semanage fcontext -a -t httpd_sys_content_t "/repo-write(/.*)?"`
    * `sudo restorecon -R /repo-write`
    * `sudo chcon -R -t httpd_sys_content_t /repo-write`
    * can run `man semanage-fcontext` and search `/example`to see examples

* selinux booleans
  * getsebool -a
  * getsebool boolean_name
  * setsebool boolean_name on|off
  * sudo setsebool -P boolean_name on|off
  * semanage boolean -l

### bash scripting
* for loop, read command, conditional, test
* Read a file line by line
* pipe to while loop
* text block via while loop


### Find all keyword in all bash scripts on the system
find / -iname "*.sh" -exec fgrep -H -n -A3 -B3 -- "case" {} \; 2>/dev/null | less

### containers
* podman
    * build -t my-apache .
    * run -d -p 8080:80 --name apache-container -v /path/to/local/directory:/path/in/container my-apache
    * ps
    * stop apache-container
    * rm apache-container
    * pull <image>
    * logs <container_id>
    * exec -it <container_id> /bin/bash
    * rmi <image_id>
    * images
    * rm $(ps -a -q)
    * rmi $(images -f "dangling=true" -q)

* setup podman search
    * unqualified-search-registries=["registry.access.redhat.com", "registry.fedoraproject.org", "docker.io"]
    * cat /etc/containers/registries.conf

* Configure a container to start automatically as a systemd service
* /etc/systemd/system/<service-files>

```
[Unit]
Description=<decription>
Want=<wanted-services>

[Service]
Restart=always
ExecStart=/usr/bin/podman start <container-name>
ExecStop=/usr/bin/podman stop -t 2 <container-name>

[Install]
WantedBy=multi-user.target
```





### SYSTEM FLOWS
* Interrupt the boot process in order to gain access to a system
* preserve system journals
* Modify the system bootloader
