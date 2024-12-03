### Know
* `df` vs `du`
* General File system navigation and CRUD of files/directorys
* find out where a files manpages are
* get general info about files (5 different commands)
* view all block devices
* list open files attached to a mount
* not complete yet
* find out if two files are hard links of each other
* create/remove filesystem
* make/activate/remove swap
* resize filesystem
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


### simple facts
    * `man 7 hier` or `man file-hierarchy`
    * estimate minimum size filesystem can be shrunk: `resize2fs -P /dev/sda1`
    * get block size of the filesystem: `blockdev --getbsz /dev/sdX`
    * can use awk to calculate the total size: `echo | awk "{print 4 * 2}"
    * `lsblk -pf`
    * `man lsof`



### 
* do not forget to run systemctl daemon-reload after editing /etc/fstab. 



* `lsof` command lists all open files and the process accessing them in the provided directory.
    * good for figuring out why filesystem is blocked from unmounting
    * just do `man lsof` and look at examples

* General File system navigation
	* ls,mkdir,cd,pwd,rmdir,cp,rm,ln,file,touch,cat,vi,mv

* find out where a file and is manpages are located with `whereis` 
* get info about files: `type`, `stat`, `file`, `whereis`, `which`

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

* find out if two files are hard links of each other
    * `stat <filename>`: the two files will have same inode numbers 

* Create a file system
    * `mkfs -t ext4 /dev/sdXn`


* remove file system:
	* `sudo wipefs -a /dev/sdXn`


* Mount a file system
    * `mount /dev/sdXn /mnt`
    * `umount /mnt`
    * `sudo mount -L test_lvm_fs /mnt/test`
    * `vim /etc/fstab`

* Create swap space
    * `mkswap /dev/sdXn`
    * `swapon /dev/sdXn`
    * `swapoff /dev/sdXn`

* Check and repair file system
    * ext: `e2fsck /dev/sdXn`
    * xfs: `xfs_repair /dev/sdXn`

* Resize file system
    * ext: `resize2fs /dev/sdXn <size>`
    * xfs: `xfs_growfs /mnt/mountpoint`


### Swap
1. partition based:
	* `mkswap /dev/some_volume`
	* `swapon /dev/some_volume`
	* view: `swapon` or totals: `free -h`
		* lvm volumes will be reported as: `/dev/dm-<something>` 
			* can coorelate this to lv's by: `ls -l /dev/mapper`
	* don't forget to add to fstab
    * mkswap adds a swap signature
    * add to fstab and systemctl daemon-reload
    * Use `swapon` with the device as a parameter
    * use `swapon -a` to activate all the swap spaces listed in `/etc/fstab`


2. file based:
	* `mkswap /swapfile`
	* `chmod 600 /swapfile`
	* `swapon /swapfile`
	* don't forget to add to fstab and systemctl daemon-reload


* Priority
    * By default, the system uses swap spaces in series, meaning that the kernel uses the first activated swap space until it is full, then it starts using the second swap space.
    * To set the priority, use the pri= option in /etc/fstab. The kernel uses the swap space with the highest priority first. The default priority is -2
    * When swap spaces have the same priority, the kernel writes to them in a round-robin fashion.
    * can view priority with `swapon`

## Non rhcsa
* Adjust tunable file system parameters on ext2/ext3/ext4
    * `tune2fs -c 20 /dev/sdXn`

* Change the label on an ext2/ext3/ext4 file system
    * `e2label /dev/sdXn newlabel`

* Locate/print block device attributes
    * `blkid /dev/sdXn`
    * view much info including UUID: `lsblk -f`
    * view UUID's: `blkid`

* Fully Cleaning a drive
	* Overwrite with random data: `sudo dd if=/dev/urandom of=/dev/sdX bs=1M`
	* Overwrite with zeros: `sudo dd if=/dev/zero of=/dev/sdX bs=1M`
	* `sudo shred -v -n 3 /dev/sdX` (verbose overwrites 3 times)
	* can shred single file: `shred -u filename`

## Files
`mkdir`
`cd`
`pwd`
`rmdir`
`cp`
`rm`
`ls`
`ln`
`touch`
`cat`
`vi`
`mv`
`chattr`
`lsattr`

* `find`
    * always quote find searches
        * `find / -name "*.txt"`
        * `find /etc -name '*pass*'`
    * sensitive search by default
        * insensitive search is -iname
    * search by user and group:
        * -user and -group 
        * -uid and -gid
        * `find . -perm 777`
        * + and - are more than/less than
        * `find / -size 10M` or `find -size +10M` or  `find -size -10M`
        * `find / -mmin 120` or  `find / -mmin -120`: modification time
        * `-type f|d|l|b` 
            * b is block device (good for /dev directory)
        * `-links +1` :hard link count
    
* Find all keyword in all bash scripts on the system*
  * `find / -iname "*.sh" -exec fgrep -H -n -A3 -B3 -- "case" {} \; 2>/dev/null | less`


    * to defuck:
    A numeric permission preceded by / matches files that have at least one bit of user, group, or other for that permission set. A file with permissions r--r--r-- does not match /222, but one with rw-r--r-- does. A - sign before a permission means that all three instances of that bit must be on, so neither of the previous examples would match, but something like rw-rw-rw-> would.