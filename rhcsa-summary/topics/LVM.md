### Know
* create, remove, extend, display: physical,logical, and volume groups
* note: go through creating and resizing!!
* `resize2fs/xfs_growfs`
* `pmove` before shrink
* what command to add another volume to a vg?
* increase a logical volume size, BY a given amount(i.e. add 10G) versus TO a given amount(make it 10G total)

### Tips
* `vgdisplay -v` is extremely useful and the only way to get full info about the group
* `lvcreate -L` capital L!! allows specifying storage by bytes
* `-l +100%FREE`: use all available space
* `--resizefs`

### essentials
* command prefixes: `lv`, `pv`, `vg`
* command suffixes : `s`, `display`, `create`, `remove`, `scan`
* can tack on a -`-units h` for marginal help
* `vgdisplay -v` is best way to view  the whole thing
* `lvcreate -L 10G, -l +100%FREE` 
    * -L to indicate megabyte size not extents
    * -l with +100%FREE to take up all the available space in volume group
* `lvresize`, `resize2fs/xfs_growfs`, `--resizefs` will also resize file system
* `vgextend` to extend the volume group with more

### Physical volume
* this literally just configures/formats the volume or partition to be acceptable to LVM
* this is pretty simple
* `pvcreate /dev/sdXn`
* `pvs`, `pvscan`, `pvdisplay`
* `pvremove /dev/sdXn`

### Volume group
* this adds the configured devices to a group to be used by logical volumes
* this is pretty simple as well
* commands
    * `vgcreate`, `vgextend`, `vgreduce`, `vgremove`
    * `vgcreate myvg /dev/sdXn`
    * `vgextend myvg /dev/sdYn`
    * `vgremove myvg`

* viewing
    * `vgdisplay -v` is extremely useful and the only way to get full info about the group
        * can limit by adding a specific volume group at the end
    * `vgs` doesn't have the volumes in the group UNLESS those volumes are mapped to a logical volume

### Logical volume
* create the logical volume to be able to hold data

* view:
    * best command is: `vgdisplay -v` because it gives both lv and vg info

* create:
    * standard form: `lvcreate -L 10G -n mylv myvg`
    * can use `-l +100%FREE` to create with all available space in volume group

*reducing/expanding
    * volume: `lvresize`
    * file system: `resize2fs/xfs_growfs`
    * `pvmove /dev/sdb1`
        * No logical volumes or data will remain on /dev/sdb1.
        * The physical volume (/dev/sdb1) will be empty and unused. 
        * it will still be in volume group and usable though!
    * `vgreduce` will remove from volume group

* reducing:
    * option 1:
        * resize fs:`resize2fs /dev/mapper/some_volume 500M` 
            * does not support changing by an amount have to change to the final amount
        * resize volume to specific amount: `lvresize -L 500M /dev/my_volume_group/my_logical_volume` 
        * resize volume by specific amount: `lvresize -L -500M /dev/my_volume_group/my_logical_volume` 

    * option 2:
        * resize fs and volume to specific amount: `lvresize --resizefs -L 500M /dev/my_volume_group/my_logical_volume` 
        * resize fs and volume by specific amount 500M: `lvresize --resizefs -L -500M /dev/my_volume_group/my_logical_volume`

    * can't shrink xfs file systems, have to reformat!!
    
* expanding
    * extend to specific amount of space: `lvresize --resizefs -L 500M /dev/my_volume_group/my_logical_volume`
    * extend by specific amount of space: `lvresize --resizefs -L +500M /dev/my_volume_group/my_logical_volume`
    * extend to all available vg space: `lvresize --resizefs -l +100%FREE /dev/my_volume_group/my_logical_volume`

* commands:
* `lvs`, `lvscan`, `lvdisplay`
* `lvextend`/`lvreduce` or `lvresize`
* `lvresize -L [+|-][Size] <vgname>/<lvname>`
* `lvextend -L +10G /dev/myvg/mylv` + `resize2fs /dev/myvg/mylv`
* `lvremove /dev/myvg/mylv`