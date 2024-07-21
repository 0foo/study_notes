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



