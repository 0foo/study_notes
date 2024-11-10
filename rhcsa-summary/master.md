### At start of exam
* setup ssh instead of using VM terminal
* `dnf -y install setroubleshoot policycoreutils-python policycoreutils setroubleshoot-server`
* run `mandb &`


### things to make permanant
* firewall-cmd --permanant
* setsebool -P

### To remember
* use `pgrep -f` instead of plain `pgrep` for searching patterns, plain pgrep just searches the command name!


* anytime change a config file restart that daemon
  * can search systemctl list-units | grep <service name>
  * can try to vefify it's working by looking at `journalctl -u <service>`

* if change any unit files or fstab
  * `systemctl daemon-reload`

* always test fstab changes with `mount -a`

* after editing or adding a nmcli connection 
  * if autoconnect is not equal to yes have to down/up the interface
    * nmcli con down enp0s8
    * nmcli con up enp0s8


* Always run `dnf update` after changing dnf repo files!!

* After changing a network connection with nmcli RELOAD: `nmcli connection reload`
  * can also restart network manager 
    * `systemctl restart NetworkManager`
  
* when editing firewalld rules with `--permanant` flag need to run:  `firewall-cmd --reload`

* after changes to partitions either add or remove: `partprobe`

* when deleting partition: `umount` first

* no need to restart anything if update: `/etc/hosts`

### TBD
* VERIFY FSTAB
    * `findmnt --verify /mountpoint`: RUN EVERYTIME!!!
    * `mount /mountpoint` - uses fstab file 
    * `mount -a`

* VERIFY PARTED
    * `parted /filesystem`
    * note: this is useful to make sure you made the right size partition

* verify swap: `swapon` with no param's

* test NFS mounts by mounted with plain `mount -t nfs` command before adding to fstab or auto.master/auto.nfs

* always use .d folders instead of modifying to original config file
  * i.e. yum.repos.d, 

### To practice a little more
* bash scripting
* selinux: 
  * chcon(wiped when reboot or relabeled) vs semanage + restorecon!(permanant!)
  * cat /etc/selinux/targeted/files/file_contexts.local
  * `man semanage-port`
  * `man semanage-fcontext`
* at time
* firewall-cmd more advanced stuff
* dnf modules and groups
* what does /etc/login.defs do for password

### to remember
* autofs  indirect mount uses &!!!
* timedatectl to set timezone and set-ntp tru
* /etc/login.defs, #/etc/passwd /etc/group /etc/shadow /etc/gshadow
*  /sbin/nologin
* rpmkey -K
* at time defintions
* install a module stream and profile i.e. postgres stream 10
* /etc/sysconfig/network-scripts/
* password aging-chage
* umask in /etc/login.defs and /etc/profile
* `chmod a=rwx permu_file1`: assign to all ugo at once!
* how to run commands without entering container, also from a stopped container
* in repo file can use a file repo with: `	 baseurl = file:///mnt/AppStream `

### Userful man pages
* `man less`: for controls in less
* `man grep`  
  * for regex and glob and special classes i.e. [[:space:]]
  * for grep flags
* `man bash`: all the shell expansions
* `man semanage-port`
* `man semanage-fcontext`
* cli based nmcli connection paramters: `man nmcli-examples`
* file based nmcli connection parameters: `man nm-settings-ifcfg-rh`

### Useful directories/files
* `~/.config/systemd/user` vs `/etc/systemd/system`
* `/etc/sysconfig/network-scripts/`
* `/etc/selinux/targeted/files/file_contexts.local`
* `/etc/login.defs`
* `~/.config/containers/registries.conf` vs `/etc/containers/registries.conf`
* `/etc/yum.repo.d`

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
* get a date in the future: `date -d "+180 days" +%F`
* math: 
  * `bc`
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
* run endless process: `sha1sum /dev/zero` or   `yes > /dev/null`
* `ls -d [ei]*`
  * pass -d to not descend into subdirectories when ls encounters a directory
  * should be default!
* `uptime`: system load average
























### Navigating man, less, etc.
* m
