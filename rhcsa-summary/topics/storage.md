* `lsblk -af`
* `parted`
* `mkfs`
* `mount`
* `/etc/fstab` + `systemctl daemon-reload` + `mount -a`




* VERIFY FSTAB
    * `mount /mountpoint` - uses fstab file 
    * `findmnt --verify`
    * `mount -a`

* VERIFY PARTED
    * `parted /filesystem`
    * note: this is useful to make sure you made the right size partition


### Parted
* `parted mklabel` makes partition table
* `parted mkpart` makes partition
* `set` (tab through everything)
* ADD a parted flag for la


### SWAP
* `mkswap`
* `swapon /dev/sda`
* `swapon -a`
* (-v for details)


* `udevadm settle`
    * after parted to let all the devices synchronize with new partitions
* `parted /dev/vdb mkpart primary xfs 2048s 1000MB`
* With most disks, a start sector that is a multiple of 2048 is a safe assumption to not get out of alignment error message