### essentials
* command prefixes: `lv`, `pv`, `vg`
* command suffixes : `s`, `display`, `create`, `remove`, `scan`
* can tack on a -`-units h` for marginal help

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
    * `vgs` doesn't have the volumes in the group UNLESS those volumes are mapped to a logical volume

### Logical volume
* this does all the work of creating the logical volume to be able to hold data
* standard form: `lvcreate -L 10G -n mylv myvg`
* `lvs`, `lvscan`, `lvdisplay`
* `lvextend`/`lvreduce` or `lvresize`
* `lvresize -L [+|-][Size] <vgname>/<lvname>`
* `lvextend -L +10G /dev/myvg/mylv` + `resize2fs /dev/myvg/mylv`
* `lvremove /dev/myvg/mylv`



### LVM Non RHCSA related

* non-rhcsa related:
    * `vgscan`  to rescan the system and rebuild the lvm metadatacache, useful if adding/removeing volumes a lot
When a single logical volume (LV) is created in a volume group (VG) that contains several physical volumes (PVs), LVM abstracts the underlying physical storage, allowing the logical volume to span multiple physical volumes without the user needing to worry about the physical layout.

Here's how the writing process works when a single logical volume is backed by multiple physical volumes:

1. Logical Extents and Physical Extents
LVM breaks down the storage space in both logical volumes and physical volumes into chunks called extents.

- Physical Extents (PEs): These are fixed-size chunks on the physical volumes.
- Logical Extents (LEs): These are the chunks on the logical volume that map directly to physical extents.

Both logical extents and physical extents are usually the same size (default is 4 MB), and this size can be customized. When data is written to a logical volume, it is divided into these extents, which are then mapped to physical extents across one or more physical volumes in the volume group.

2. How Data is Distributed
When you create a logical volume, LVM assigns logical extents (LEs) to the logical volume, which are mapped to physical extents (PEs) on one or more physical volumes. The distribution of these extents across the physical volumes depends on the allocation policy used by LVM.

There are three main allocation methods:

- Linear Mapping (Default): 
  Data is written sequentially to physical extents on the first physical volume until it is full. Once the first physical volume is full, LVM continues writing to the next physical volume in the volume group.
  
  This is the default and simplest method, but it does not offer any performance benefits like striping.

- Striped Mapping (Similar to RAID 0):
  Data is striped across multiple physical volumes, meaning that the data is divided into stripes and written alternately to different physical volumes. This can improve performance since reads and writes are spread across multiple devices, allowing parallel access.
  
  This is useful for performance improvements but does not offer redundancy.

  Command for Striping: When creating the logical volume, you specify the number of stripes:
  sudo lvcreate -L 10G -n my_lv -i 2 my_vg
  The -i 2 option indicates 2 stripes (striping across 2 physical volumes).

- Mirrored Mapping (Similar to RAID 1):
  Data is mirrored across two or more physical volumes, meaning that every write operation is duplicated to maintain redundancy. This protects against physical volume failures.
  
  Command for Mirroring: To create a mirrored logical volume:
  sudo lvcreate --type mirror -m 1 -L 10G -n my_lv my_vg
  The -m 1 option creates one mirror (so there are two total copies of the data).

3. Linear Allocation Example (Default Mode):
In the default linear allocation mode, if you have a volume group that consists of two physical volumes /dev/sda1 and /dev/sdb1, and you create a logical volume from this group:

1. Data is written to physical extents on /dev/sda1 until it is full.
2. Once /dev/sda1 is full, data is then written to /dev/sdb1.

4. Striped Allocation Example (Performance Improvement):
In a striped setup (similar to RAID 0), LVM divides the data into chunks (stripes) and writes each stripe alternately across the available physical volumes. If you have /dev/sda1 and /dev/sdb1 in the volume group and create a striped logical volume:

1. Stripe 1 is written to /dev/sda1.
2. Stripe 2 is written to /dev/sdb1.
3. Stripe 3 is written to /dev/sda1, and so on.

This distribution improves performance because both physical volumes can handle read and write requests simultaneously, effectively increasing the throughput.

5. Mirrored Allocation Example (Redundancy):
In a mirrored setup (similar to RAID 1), data is written identically to multiple physical volumes. If you mirror a logical volume across /dev/sda1 and /dev/sdb1, every write operation will be mirrored on both physical volumes:

1. Data written to /dev/sda1 is also written to /dev/sdb1 at the same time.
2. If one of the physical volumes fails, the data remains intact on the other physical volume.

6. How LVM Manages Extents and Allocation
LVM keeps a mapping table that associates logical extents (LEs) with physical extents (PEs). This mapping allows the system to know where the data is physically stored and how it should be read or written. The user interacts with logical volumes, but under the hood, LVM manages where the data actually goes on the physical volumes.

7. Managing Logical Volumes
You can monitor where data is stored and how extents are mapped across physical volumes using the following commands:

- To see the mapping of logical extents to physical extents:
  sudo lvs -o +devices
  This will show you which physical volumes are used by a logical volume.

- To see details of the volume group:
  sudo vgdisplay my_vg

- To see details of the physical volumes:
  sudo pvdisplay