## initramfs

* great article: 
    * https://wiki.gentoo.org/wiki/Initramfs/Guide


### Ultimate Purpose
* get root file system mounted
* To avoid having to hardcode handling for so many special cases into the kernel, an initial boot stage with a temporary root file-system – now dubbed early user space – is used. This root file-system can contain user-space helpers which do the hardware detection, module loading and device discovery necessary to get the real root file-system mounted


### Special Cases that would bloat the kernel
* Special volume type: The root file system may be on a software RAID volume, LVM, NFS (on diskless workstations), or on an encrypted partition. All of these require special preparations to mount.
* Encryption: Users who use an encrypted file system will also have the initramfs ask them for the passphrase before it can mount the file systems.
* Bloat: Kernel is kept small by putting the massive amount of possible drivers in external file system
* Hibernation: Kernel support for hibernation, which suspends the computer to disk by dumping an image of the entire contents of memory to a swap partition or a regular file, then powering off. On next boot, this image has to be made accessible before it can be loaded back into memory. 


### Functionality
* Hardware drivers: Any hardware drivers that the boot process depends on must be loaded. A common arrangement is to pack kernel modules for common storage devices onto the initrd and then invoke a hotplug agent to pull in modules matching the computer's detected hardware.
    * Some distributions use an event-driven hotplug agent such as udev, which invokes helper programs as hardware devices, disk partitions and storage volumes matching certain rules come online. This allows discovery to run in parallel, and to progressively cascade into arbitrary nestings of LVM, RAID or encryption to get at the root file system. 
* Graphics: On systems which display a boot splash screen, the video hardware must be initialized and a user-space helper started to paint animations onto the display in lockstep with the boot process.n

* Network: If the root file system is on NFS, it must then bring up the primary network interface, invoke a DHCP client, with which it can obtain a DHCP lease, extract the name of the NFS share and the address of the NFS server from the lease, and mount the NFS share.
* RAID: If the root file system appears to be on a software RAID device, there is no way of knowing which devices the RAID volume spans; the standard MD utilities must be invoked to scan all available block devices and bring the required ones online.
* LVM: If the root file system appears to be on a logical volume, the LVM utilities must be invoked to scan for and activate the volume group containing it.
* Encryption: If the root file system is on an encrypted block device, the software needs to invoke a helper script to prompt the user to type in a passphrase and/or insert a hardware token (such as a smart card or a USB security dongle), and then create a decryption target with the device mapper.


### How does initramfs find root file system
1.  Often GRUB will pass a kernel parameter with the identifier of the drive with root partition
    * GRUB_CMDLINE_LINUX="root=UUID=1234-5678-90AB-CDEF"
    * GRUB_CMDLINE_LINUX="root=LABEL=my_root_fs"
    * GRUB_CMDLINE_LINUX="root=/dev/sda1"

2. If no kernel parameter is passed will enumerate all the drives and mount them and search for a root file system
    * mounts every volume one by on in a temp mount location while scanning

3. If can't find root file system, will fallback into an emergency shell BASED OUT OF INITRAMFS


### Process (general/high level, may not be complete)
1. Bootloader loads kernel and initramfs into memory
2. Kernel is passed control and initializes hardware and necessary drivers
3. Initramfs is passed control
    1. init(same as systemd except in initramfs) is started
    2. Identify all additional hardware kernel doesn't have drivers built in for(see above)
        * via udev or other methods
    3. the init target is: initrd.target 
4. After the “real” root file system has been found, it is checked for errors and mounted.
5. If this is successful, the initramfs is cleaned and the systemd daemon on the root file system is put into memory and passed control. 


