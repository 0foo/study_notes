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
