The tasks listed are essential components of managing storage in a Linux environment, specifically related to the RHCSA (Red Hat Certified System Administrator) certification. Here's a detailed explanation of each task:

* Create and remove physical volumes:
   - **Physical Volume (PV):** A physical volume is the base storage unit in LVM (Logical Volume Manager). It can be a hard disk, a partition, or a RAID device.
   - **Create PV:** Use the `pvcreate` command to initialize a disk or partition for use by LVM.
     ```bash
     pvcreate /dev/sdX
     ```
   - **Remove PV:** Use the `pvremove` command to remove LVM metadata from a physical volume.
     ```bash
     pvremove /dev/sdX
     ```

* Assign physical volumes to volume groups:
   - **Volume Group (VG):** A volume group combines multiple physical volumes into a single storage pool.
   - **Create VG:** Use the `vgcreate` command to create a volume group from one or more physical volumes.
     ```bash
     vgcreate myvg /dev/sdX /dev/sdY
     ```
   - **Add PV to VG:** Use the `vgextend` command to add more physical volumes to an existing volume group.
     ```bash
     vgextend myvg /dev/sdZ
     ```

* Create and delete logical volumes:
   - **Logical Volume (LV):** Logical volumes are created from the storage pool provided by volume groups.
   - **Create LV:** Use the `lvcreate` command to create a logical volume.
     ```bash
     lvcreate -n mylv -L 10G myvg
     ```
   - **Delete LV:** Use the `lvremove` command to delete a logical volume.
     ```bash
     lvremove /dev/myvg/mylv
     ```

*  Configure systems to mount file systems at boot by universally unique ID (UUID) or label:
   - **UUID and Label:** UUID is a unique identifier assigned to a filesystem, while a label is a human-readable name.
   - **Get UUID and Label:** Use `blkid` to retrieve UUID and label.
     ```bash
     blkid /dev/sdX1
     ```
   - **Edit `/etc/fstab`:** To mount a filesystem at boot, add an entry to `/etc/fstab` using UUID or label.
     ```bash
     UUID=1234-5678 /mnt/mydata ext4 defaults 0 2
     # or
     LABEL=mydata /mnt/mydata ext4 defaults 0 2
     ```

* Add new partitions and logical volumes, and swap to a system non-destructively:
   - **New Partitions:** Use tools like `fdisk`, `gdisk`, or `parted` to create new partitions without destroying existing data.
     ```bash
     fdisk /dev/sdX
     ```
   - **Add Logical Volumes:** Extend existing volume groups and create new logical volumes.
     ```bash
     vgextend myvg /dev/sdY
     lvcreate -n newlv -L 5G myvg
     ```
   - **Add Swap Space:** Use a partition or a logical volume for swap.
     ```bash
     mkswap /dev/sdX2
     swapon /dev/sdX2
     ```

* Resize Logical Volumes
  * `lvreduce -L -size /dev/vgname/lvname`