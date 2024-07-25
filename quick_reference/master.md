### Man
* use section 5 for files
* use regular man for commands

## user,groups 
* useradd, usermod, userdel, adduser, /etc/passwd
* groupadd, groupmod, groupdel, gpasswd, /etc/group, make a sudo account: usermod -aG wheel <username>
* passwd, chage, /etc/shadow, visudo
* chown, chmod, umask
* id, whoami, lastlog, su
* set: guid, suid, sticky bit

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

### NFS
* `sudo mount -t nfs servername:/exported/share /mnt/nfs`
* in `/etc/fstab`
    * `servername:/exported/share /mnt/nfs nfs defaults 0 0`

### autofs
* in `/etc/auto.master`
    * define mount point and mount config file-> `/mnt/nfs /etc/auto.nfs`
* in `/etc/auto.nfs`
    * `nfs    -rw,soft    servername:/exported/share`
* can navigate to the folder or ls the folder and it will mount

### File system navigation
* ls,mkdir,cd,pwd,rmdir,cp,rm,ln,file,touch,cat,vi,mv

### firewalld
* firewall-cmd

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


### important systemctl commands
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