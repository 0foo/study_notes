### Misc
* create a file `fallocate -l 100M`

### text wrangling
```
cat <<EOF > file.txt
This is line 1.
This is line 2.
This is line 3.
EOF
```

### ssh
* host an ssh session
    * add key to authorized_hosts on the account .ssh folder
* access an ssh session
    * ssh_keygen
    * `ssh-copy-id`
    * ssh with account creds


### Man
* use section 5 for files
* use regular man for commands
* man -K
    * searches for a keyword
    * -w is case sensitive
* catman
    * updates all manual pages
* catman && man -K

## user,groups 
* useradd, usermod, userdel, adduser, /etc/passwd
* groupadd, groupmod, groupdel, gpasswd, /etc/group, make a sudo account: usermod -aG wheel <username>
* passwd, chage, /etc/shadow, visudo
* chown, chmod, umask
* id, whoami, lastlog, su
* set: guid, suid, sticky bit
* getent: literally just cat's /etc/passwd and /etc/group

## compression
* tar, xz/unxz, bzip2/bunzip2, gzip/gunzip, zip/unzip

###  File system/Storage managment
* mkfs
* mount,umount
* mkswap,swapon,swapoff
* e2fsck,xfs_repair
* resize2fs, xfs_growfs
* tune2fs
* e2label /dev/sdXn new_label
* xfs_admin -L new_label /dev/sdXn1
* blkid,lsblk, df -h, mount
* in /etc/fstab: UUID=1234-5678 /mnt/mydata ext4 defaults 0 2

* tips
    * estimate minimum size filesystem can be shrunk: `resize2fs -P /dev/sda1`
    * get block size of the filesystem: `blockdev --getbsz /dev/sdX`
    * can use awk to calculate the total size: `echo | awk "{print 4 * 2}"



### NFS

* host an nfs share
```
sudo yum install nfs-utils -y   # For RHEL/CentOS
sudo mkdir -p /srv/nfs/shared
sudo chown nobody:nogroup /srv/nfs/shared   # Adjust as needed for your security requirements
sudo chmod 755 /srv/nfs/shared
sudo nano /etc/exports
/srv/nfs/shared 192.168.1.0/24(rw,sync,no_subtree_check)
sudo exportfs -r   (or exportfs -a ??)
sudo systemctl start nfs-server
sudo systemctl enable nfs-server
firewall-cmd --add-service=mountd --add-service=rpc-bind --add-service=mountd --zone=public --permanent
sudo firewall-cmd --reload
verify: showmount -e localhost
verify: exportfs 
```

* access NFS share
    * `showmount -e <remote nfs server>`
    * `sudo mount -t nfs servername:/exported/share /mnt/nfs`
    * in `/etc/fstab`
        * `servername:/exported/share /mnt/nfs nfs defaults 0 0`

### autofs
* `dnf install autofs`
* in `/etc/auto.master`
    * define mount point and mount config file-> `/mnt /etc/auto.nfs`
* in `/etc/auto.nfs`
    * `nfs    -rw,soft    servername:/exported/share`
    * will mount at /mnt/nfs, (first field in both files)
* `systemctl [reload|restart] autofs`
* can navigate to the folder or ls the folder and it will mount
* note: if no file system type declared in config files, then nfs is the default

### File system navigation
* ls,mkdir,cd,pwd,rmdir,cp,rm,ln,file,touch,cat,vi,mv

### firewalld
* firewall-cmd
* https://github.com/jdelgit/rhcsa-notes/blob/master/07.%20Manage%20Basic%20Networking.md#restrict-network-access-using-firewall-cmdfirewall

### Logging
* journalctl, ausearch

### Swap
1. create a new partition or a new lvm or new file
    * lvcreate
    * parted
    * dd if=/dev/zero of=/swapfile bs=1M count=1024 && chmod 600 /swapfile
2. mkswap
3. swapon/swapoff
* need to add to fstab to make persistent after reboot: /dev/sdX1 none swap sw 0 0
* can remove by swapoff then delete file or partition
* swapon --show (or -s)
* free -h
* important note: for lvm swap may be reported with swapon --show as a mapped drive with the name dm-<something> 
    * can coorelate this to lv's by: `ls -l /dev/mapper`

### Shutdown/reboot
* shutdown -r now
* shutdown -h now

### Processes
* kill
* ps aux, ps -ef, ps fax (tree)
* `nice -n 19 sleep 50` / `renice -n 10 -p 1` / `ps -eo pid,comm,ni`
* pgrep/pkill (both are regex, use pgrep first)
* top/htop
* kill / 

### process priority
* chrt -r <priority> <command>
* chrt -r -p 5 1234
* `nice\renice`
* `nice -n 19 sleep 500 &`
* `renice -n 10 -p 1234`

### performance profiles
* sudo tuned-adm list
* sudo tuned-adm active
* sudo tuned-adm profile <profile>
* tuned-adm recommend
* sudo tuned-adm profile laptop-battery-powersave


### journald
* journalctl

* Flags:
    * -f: Follow new log entries
    * -b: View logs for the current boot
    * -b -1: View logs for a specific boot
    * --since "2023-07-11 10:00:00" --until "2023-07-11 11:00:00": Filter by time
    * -p err: Filter by priority
    * -u sshd.service: Filter by service
    * _UID=1000: Filter by user
    * -r: Show logs in reverse order
    * -n 50: Limit the number of displayed entries
    * > /path/to/output.log: Export logs to a file
    * -k: Show kernel messages
    * _PID=1: Query specific fields
    * --since "15 minutes ago": View system logs from the last 15 minutes
    * -u nginx.service --since "2023-07-11" --until "2023-07-12": Check logs related to a service crash
    * -f -p warn: Monitor logs in real-time with specific priority
    * -x: Show explanations for log entries

### scp
* scp <remote-user>@<host/ip>:/remote/path/to/source /local/path/destination
* scp /loca/path/source <remote-user>@<host/ip>:/remote/path/to/destination



### at
*  at <runtime> at> <command-to-run> at> <EOT>
*  at <time> -f <script-filename>
* atq
* atrm <#job>


### cron
* crontab -e
    * <time> <script-path>
    * Edit user-specific cron

* user vs root crontabs
    * crontab -u <user> -e
    * crontab -l / sudo crontab -l

```
/etc/
 ├── cron.d  
 ├── cron.daily  
 ├── cron.deny  
 ├── cron.hourly   
 ├── cron.monthly  
 ├── crontab 
 └── cron.weekly

```

* reading cron configuraion
    * do a `man /etc/crontab` to get a printout of all the cron settings
    * the key to remember is that * asterisk is every single item in that period
    * so by adding a number you will limit/filter the periodicity


### systemd service files
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


### Systemctl
* enable/disable
* reload
* restart
* start/stop
* status
* systemctl cat <service name>
    * view service file
* systemctl edit <service name>
    * edit service file
* systemctl list-dependencies <service>
* mask/unmask
    * makes it completely impossible to start a service either manually or automatically
    * note disable just stops it from starting at boot but can be started manually
* isolate
* get-default/set-default
* systemctl list-units --type target




### Time

* timedatectl
    * set-time
    * list-timezones
    * set-timezone
    * Display system time
* `/etc/systemd/timesyncd.conf`
* timedatectl set-ntp 1 or sudo timedatectl set-ntp true
    * switch on NTP use
    * it does this via chrony daemon
* force ntp update by restarting systemd service
    * `sudo systemctl restart systemd-timesyncd`



* chrony 
    * install with dnf
    * start with systemd: chronyd
    * verify:
        * chronyc sources -v (to check the sources Chrony is using)
        * chronyc tracking 
    * add to chrony.conf file
    ```
    /etc/chrony.conf
    server ntp1.example.com iburst
    server ntp2.example.com iburst
    ```
* ntp
    * install with dnf
    * start with systemd: ntpd
    * add to /etc/ntp.conf file
    ```
    server ntp1.example.com iburst
    server ntp2.example.com iburst
    ```
* don't forget to add to firewall
sudo firewall-cmd --add-service=ntp --permanent
sudo firewall-cmd --reload


### DNF
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

### basic networking
* nmcli 
    * connection [ show | up | up <connection name> | down <connection name> ]
    * device [ status | show | show <device>  | delete ]
* create new connection:
    * nmcli connection add  con-name <connection-name> ifname <interface> type <ethernet/wireless>  
* Use ipv6 and gw6 if configuring IPv6 otherwise same command
* nmcli connection modify <connection-name> <setting> <value> 
    * then take it down and up again!
* disable dhcp: nmcli connection modify <connection-name> ipv4.method manual 

* make a connection autoconnect when it detects
    * nmcli connection modify <connection-name> connection.autoconnect yes

* con create
    * con-name
    * ifname
    * type
    * ipv4.method
    * ipv4.address


### hostname
* hostnamectl

### resolvers
* never modify /etc/resolv.conf directly!
* nmcli connection modify <connection-name> ipv4.dns "<DNS-Server-IP>"  
    * nmcli connection reload 
    * systemctl restart NetworkManager
* /etc/resolve.conf
* /etc/hosts


### selinux
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

### selinux booleans
* getsebool -a
* getsebool boolean_name
* setsebool boolean_name on|off
* sudo setsebool -P boolean_name on|off
* semanage boolean -l


### bash scripting

* for loop, read command, conditional, test


```
# Read a file line by line
while read line; do
    echo "$line"
done < input_file.txt
```

```
if [ "$str1" = "$str2" ]; then
  echo "Strings are equal."
else
  echo "Strings are not equal."
fi

# double brackets allow regex/pattern matching
if [[ "$str" == hello* ]]; then
  echo "String starts with 'hello'."
else
  echo "String does not start with 'hello'."
fi
```

* pipe to while loop
```
ls | while read file; do
  echo "File: $file"
done
```
* note: the while loop is in a subshell so subshell free version:
```
count=0
while read line; do
  echo "Processing: $line"
  count=$((count + 1))
done < <(ls)
```

```
IFS=$'\n'; for i in $(ls -d1 */); do echo "$here/$i"; cd "$here/$i"; ls; cd $here; done;
```

```
for i in $(ls); do echo "LOCATION: $here/$i"; test -d "$here/$i" && cd "$here/$i"; ls; cd ~; done;
```

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




### useful
* `file` command to tell which type of file it is
* `tar -cvzf tar-file-name.tar.gz  the-file-to-compress`
* 