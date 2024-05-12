## GRUB

### BIOS boot
* In a BIOS boot: GRUB is installed in the MBR. 
* The MBR are the first 512 bytes on a disk. 
* The MBR is also used by the partition table of the disk, therefore GRUB itself has somewhat less space than the 512 bytes.
* GRUB sets bootstrap code in the MBR which takes control from BIOS after POST
* Once GRUB takes over it loads `grub.cfg`


### UEFI boot
* UEFI replaces BIOS and is more advanced
* UEFI can read a file system (typically FAT types)
* UEFI has a configuration in its settings to look for a FILE which functions as a bootloader
* in GRUB that's typically 
```
    /grub/x86_64-efi/grub.efi
    /efi/EFI/ubuntu/grubx64.efi
```
* Many times this file system is separate partitions and is mounted into boot directory i.e.: `/dev/nvme0n1p1 on /boot/efi type vfat`
* After this bootloader FILE is loaded it functions as an MBR GRUB bootloader which can then read the config file and start it's configurations


### Grub Config
* Some times in UEFI systems will have two grub.cfg
* For example on Ubuntu:
    * `/efi/EFI/ubuntu/grub.cfg` is `grub.cfg` is typically only a few lines and points to the main `/grub/grub.cfg`
```
    /grub/grub.cfg
    /efi/EFI/ubuntu/grub.cfg
```
* red hat seems to not have this designation


### Bootfile Locations 
* `/boot`
* after the above process:
* GRUB (rest of it) are several files that are loaded, from /boot/grub (for example: that nice image that appears as a background in GRUB is not stored on the MBR)


### GOAL of GRUB
* GRUB is reponsible for loading kernel and initramfs(or initrd on other distros)

Other Tasks:
    * Select from multiple kernels.
    * Switch between sets of kernel parameters.
    * Provide support for booting different operating systems.


### Grub config file management
    * /etc/default/grub file
    * This file is the source for several possible generated files
    * grub file example:
```
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=true
GRUB_TERMINAL_OUTPUT="console"
GRUB_CMDLINE_LINUX="crashkernel=auto resume=/dev/mapper/rhel-swap rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet"
GRUB_DISABLE_RECOVERY="true"
GRUB_ENABLE_BLSCFG=true
```

* GRUB_CMDLINE_LINUX
    * kernel parameters
    * it is a good idea to remove the rhgb and quiet boot options 
        * these make kernel boot quietly
        * remove to see the boot up procedure and progress messages and error messages so you can troubleshoot 
    * man 7 bootparam to see boot parameters

* can view kernel boot command up with params here: `cat /proc/cmdline`


* GRUB_TIMEOUT 
    * This defines the amount of time your server waits for you to access the GRUB 2 boot menu before it continues booting automatically.

### Modify GRUB config
* grub config is located at /etc/default/grub
* edit this file and run a grub maker
    * `update-grub` (ubuntu)
    * `grub2-mkconfig -o /boot/grub2/grub.cfg` (red hat)
* this creates and populates files in /boot directory
    * If your system is a BIOS system, the name of the file is /boot/grub2/grub.cfg. 
    * On a UEFI system the file is written to /boot/efi/EFI/redhat
    * the command is grub2-mkconfig
    * BIOS system: grub2-mkconfig -o /boot/grub2/grub
    * UEFI system: grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg

### Adding new kernel versions
* GRUB 2 picks up new kernels automatically from /boot directory and adds them to the boot menu automatically 
    * nothing has to be added manually




