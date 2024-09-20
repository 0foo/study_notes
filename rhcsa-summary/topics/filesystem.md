* tips
    * estimate minimum size filesystem can be shrunk: `resize2fs -P /dev/sda1`
    * get block size of the filesystem: `blockdev --getbsz /dev/sdX`
    * can use awk to calculate the total size: `echo | awk "{print 4 * 2}"


* General File system navigation
	* ls,mkdir,cd,pwd,rmdir,cp,rm,ln,file,touch,cat,vi,mv





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


* Create a file system
    * `mkfs -t ext4 /dev/sdXn`

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

* Adjust tunable file system parameters on ext2/ext3/ext4
    * `tune2fs -c 20 /dev/sdXn`

* Change the label on an ext2/ext3/ext4 file system
    * `e2label /dev/sdXn newlabel`

* Locate/print block device attributes
    * `blkid /dev/sdXn`
    * view much info including UUID: `lsblk -f`
    * view UUID's: `blkid`

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


## Files
	* `mkdir directory`
	* `cd directory`
	* `pwd`
	* `rmdir directory`
	* `cp source destination`
	* `rm file`
	* `rm -rf directory`
	* `ls`
	* `ln target linkname`
	* `ln -s target linkname`
	* `cp -R source destination`
	* `cp -a source destination`
	* `cp /etc/hosts /tmp/`
	* `file <filename>`
	* `touch file`
	* `cat > newfile`
	* `vi file`
	* `mkdir directory`
	* `mv item1 item2`
	* `cp item1 item2`
	* `rm file`
	* `rmdir directory`
	* `rm -r directory`
	* `chattr +A file`
	* `chattr +S file`
	* `chattr +a file`
	* `chattr +i file`
	* `chattr +j file`
	* `chattr +t file`
	* `chattr +d file`
	* `chattr +u file`
	* `lsattr -l`
	* `ln -s file1 softlink`
	* `ln file1 hardlink`
	* `ls -h`
	* `ls -a`
	* `ls -l`
	* `ls -lt`
	* `ls -ltr`
	* `ls -R`
