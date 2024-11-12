### At start of exam
* setup ssh instead of using VM terminal
* `dnf install -y policycore* setrouble*`
  * shortcut for: `dnf -y install setroubleshoot policycoreutils-python policycoreutils setroubleshoot-server`
* run `mandb &`



#### Know
* how to search processes and kill process
* what do when change a service config file
* what do when change unit file
* what do when change fstab
* how to verify fstab
* what do after editing fstab and adding swap
* what do when edit nmcli connection
* what do when edit repo files
* what do when editing firewall-cmd rules
* what do after editing partitions
* what do at start of exam(3)
* how to read from file into while loop
* how to script multiline output to file in cli
* how to verify a parted change
* how to verify swap
* how to test nfs mounts before adding to fstab
* two places to change umask
* what file to set password complexity
* what file to set password age
* what is directory of user systemd service definitions
* what man page give yum.repos.d config options?!
* what is the name of the parameter to put a yum repo url or file location?
* what man page will give the command to create yum repo files with cli?
* two places to change umask for entire system and two places for single user umask set

### password management
* `pwquality.conf` and `login.defs`


### selinux
* `man semanage-port`
* `man semanage-fcontext`
* `file_contexts.local`
* `dnf install -y policycore* setrouble*`
* `grep SELinux /var/log/messages` or  can grep the service you're looking for i.e. httpd
* `sealert -a /var/log/audit/audit.log`


### network manager
`man nmcli-examples`
`man -K BOOTPROTO`


### sudoers
```
%sys ALL = NETWORKING, SOFTWARE, SERVICES, STORAGE, DELEGATING, PROCESSES, LOCATE, DRIVERS
%wheel	ALL=(ALL)	ALL
%wheel	ALL=(ALL)	NOPASSWD: ALL
```

### crontab
sudo crontab -u alex -e
By default, cron jobs do not send output to the terminal. To see the output, you could redirect it to a file or email.


### autofs
  * timeout in auto.master: `/mnt/auto /etc/auto.shares --timeout=120`
  * readonly in auto.shares: `somedir -fstype=nfs,ro 192.168.14.132:/export/public`
    * CAN ONLY HAVE SINGLE DIRECTORY HERE UNLESS USE /- IN PARENT FILE
    * don't forget & for * 192.168.1.4:/srv/share/&
  * verify autofs options with: mount command


### yum
* `man yum.conf`: for yum.repos.d configuration
* `man dnf config-manager`: for creating yum repos via cli!!!
* Always run `dnf update` after changing dnf repo files!!
* in repo file can use a file repo with: `	 baseurl = file:///mnt/AppStream `
* 
```
[somerepo]
name = Some repo
baseurl = some url starting with http(s):// or file:///mnt/AppStream
enabled = 0
```

### bash scripting
```
while IFS=":" read user uid group ; do
echo "Creating user $user..."
useradd -b /mnt/autofs_home -G $group -u $uid -M $user
done < userlist.txt
```
```
cat <<EOF > test.txt
some stuff
stuff
EOF
```



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

* After changing a network connection with nmcli:
  * nmcli conn down <connection_name>
    nmcli conn up <connection_name>

* when editing firewalld rules with `--permanant` flag need to run:  `firewall-cmd --reload`

* after changes to partitions either add or remove: `partprobe`

* when deleting partition: `umount` first

* no need to restart anything if update: `/etc/hosts`

* remember `chmod +x` on scripts!!!

* remember to open firewall/check for any web services

* activate all swap: `swapon -a`

* read input from file: `while IFS=":" read key value; do echo "$key $value"; done < test.txt`

```
while IFS=":" read user uid group ; do
echo "Creating user $user..."
useradd -b /mnt/autofs_home -G $group -u $uid -M $user
done < userlist.txt
```



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
* `/etc/security/pwquality.conf`!!! && `/etc/login.defs` && `PASS_MAX_DAYS   60`
* two places to change umask for entire system and two places for single user umask set

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
* umask in /etc/login.defs and /etc/profile!!!
* `chmod a=rwx permu_file1`: assign to all ugo at once!
* how to run commands without entering container, also from a stopped container
* in repo file can use a file repo with: `	 baseurl = file:///mnt/AppStream `
* Create a bash script that shows total count of the supplied arguments , value of the first argument, PID of the script and all the supplied arguments
* be careful of 1GiB and 1GB with parted!!!!
* extent size is defined in vgcreate with -s flag!!!
* lowercase -l is extent amount vs upper case -L is size in bytes
* the size of a volume is specified by the partition size!!!
* always open firewall for web services
* bash string comparison is = i.e. "x"="y" is 1 "x"="x" is 0 and use echo $? to see output of test

### Userful man pages
* `man less`: for controls in less
* `man grep`  
  * for regex and glob and special classes i.e. [[:space:]]
  * for grep flags
* `man bash`: all the shell expansions
* `man semanage-port`
* `man semanage-fcontext`
* cli based nmcli connection paramters: `man nmcli-examples`
* file based nmcli connection parameters: `man nm-settings-ifcfg-rh` or `man -K BOOTPROTO`

### Useful directories/files
* `~/.config/systemd/user` vs `/etc/systemd/system`
* `/etc/sysconfig/network-scripts/`
* `/etc/selinux/targeted/files/file_contexts.local`
* `/etc/login.defs`
* `~/.config/containers/registries.conf` vs `/etc/containers/registries.conf`
* `/etc/yum.repo.d`
* `/etc/selinux/config`
* `/etc/default/grub`

### Misc
* create empty file of specific length: 
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















### Navigating man, less, etc.
* m
