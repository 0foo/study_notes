### Know
* make partitions, labels, types, flags on a volume
* view all volumes with filesystems
* view all mounts
* how to verify a mount (3 ways)
* how to create a file system
* how to mount a filesystem both permanantly and persistently 
* how to create a swap partition and VERIFY swap is working, both persistently and temporarily
* `lsblk -pf`
* `parted`
* `mkfs`
* `mount`
* `/etc/fstab` + `systemctl daemon-reload` + `mount -a`
* note: du and df are for filesystems not devices



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