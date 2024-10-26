* tips
    * `man 7 hier` or `man file-hierarchy`
    * estimate minimum size filesystem can be shrunk: `resize2fs -P /dev/sda1`
    * get block size of the filesystem: `blockdev --getbsz /dev/sdX`
    * can use awk to calculate the total size: `echo | awk "{print 4 * 2}"


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

* find out if two files are hard linke
    * `ls -i`  or `stat <filename>`: the two files will have same inode numbers

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

