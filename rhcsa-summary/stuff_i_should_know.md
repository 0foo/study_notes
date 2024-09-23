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
* add, remove, modify, search for a user: 
* add, remove, modify, search for a group
* add/remove user from a group
* view all groups a user is in
* view id's of user 
* change password for users/root
* set password age


### performance profiles
* change, view current, list all profiles, list reccomended

## compression
* compress/uncompress files 
* create archive of file
* know tar command parameter order of source and destination !!

### scheduled
* at
    * know how to create at's
    * view all at's
    * remove an at

* cron
    * create/view cronjobs for root and users
    * resources:
        * cat /etc/crontab to view format of cron and 
        * can view files in /etc/cron.* for examples
        * man 5 crontab
    * note: don't need username if using a user crontab
    * logfile in /var/log: either syslog or cron

### ssh 
* serverside: install/enable sshd on a server and open firewall and allow rootlogins
* userside: create a key, get key on remote server (2 ways), login via ssh
* Note: apt packages: ubuntu uses ssh/rhel uses sshd



### time
* RTC is 'real time clock' which is the systemclock

* chrony
    * add ntp servers
        * remember after updating chrony.conf to restart
        * 0.us.pool.ntp.org
    * verify ntp servers
        * chronyc -N sources

* timedatectl
    * verify ntp is active
    * enable/disable ntp with timedatectl
    * view/change timezone 
        * timedatectl and symlink in /etc/localtime


### firewalld
* view all active zones
* list everything on all zones
* add a service to a zone and make it permanant
* remove a service from a zone
* add a network interface to a zone
* tip: reload firewall after using a command with --permanant flag!!!
* this is necessary because the --permanent option applies changes to the persistent configuration, but they do not take effect immediately. 


### Shutdown/reboot
* how to shutdown and how to shutdown with reboot
* shutdown -r now
* shutdown -h now


### processes
* search processes
* kill processes
* set process priority
* set process niceness
* view default proc info with ps plus additional info with -O flag
* find the most memory or cpu or nice or other resource intensive process(i.e. sorting)
* adjust process scheduling priority/policy 
* adjust process nice value or new/running process

### scp
* scp <remote-user>@<host/ip>:/remote/path/to/source /local/path/destination
* scp /loca/path/source <remote-user>@<host/ip>:/remote/path/to/destination


### systemd
* switch systems into different targets temporarily
* boot systems into different targets
* view current target 
* view all targets possible

### File system
* basic volume creation
    * List, create, delete partitions on MBR and GPT disks
    * set the partition type flag for lvm (set 1 lvm on) (note: pvcreate does this)
    * List all bare metal volumes
    * Create and remove physical volumes
    * Assign physical volumes to volume groups
    * Create and delete logical volumes
    * format a volume with file system
    * Create, mount, unmount, and use vfat, ext4, and xfs file systems

* basic file system creation
    * create filesystem on a volume
    * mount file system to a directory
    * Configure systems to mount file systems at boot by universally unique ID (UUID) or label

* shrink/expand ext4 and xfs filesystem: : Different commands!!
* shrink/expand lvm volumes

* swap
    * Add/remove swap to a system non-destructively

* extras: wipe a volume with shred or dd


### NFS/AutoFS
* view all remote nfs shares of a server
* mount a server via cli and via fstab
* use autofs to mount a remote nfs share



### access/permissions
* Configure superuser access
* Create and configure set-GID directories for collaboration(EXAM OBJECTIVE)
* Diagnose and correct file permission problems
