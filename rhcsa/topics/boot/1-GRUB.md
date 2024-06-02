## GRUB

### purpose

* Linux bootloader's main task is to find the kernel image (vmlinuz) and the initramfs archive, and to provide command-line options to the kernel – which contain the root partition's name in Linux syntax, such as root=/dev/sda2 or root=UUID=XYZ-ABC.

* note: the bootloader knows nothing about the root partition it just passes as a kernel param

### Grub config load
* Once GRUB fully takes over it loads `grub.cfg`


### Bootfile Locations 
*  `/boot`
* GRUB (rest of it) are several files that are loaded, from /boot/grub (for example: that nice image that appears as a background in GRUB is not stored on the MBR)


### GOAL of GRUB
* GRUB is reponsible for loading kernel and initramfs(or initrd on other distros)

Other Tasks:
    * Select from multiple kernels.
    * Switch between sets of kernel parameters.
    * Provide support for booting different operating systems.


### Grub config file management

* Grub functional config
    * Some times in UEFI systems will have multiple grub.cfg
    * For example on Ubuntu:
        * `/efi/EFI/ubuntu/grub.cfg` is `grub.cfg` is typically only a few lines and points to the main `/grub/grub.cfg`
    ```
        /grub/grub.cfg
        /efi/EFI/ubuntu/grub.cfg
    ```
    * red hat seems to not have this designation
    * many times grub functional config is located in /boot/grub2/grub.cfg
        * DO NOT modify this file, this is the trans-piled grub file

* pre-trans-piled configuration of grub config
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
* grub config files are located at /etc/default/grub and at /etc/grub.d/ 
* edit this file and run a grub transpiler
    * `update-grub` (ubuntu)
    * `grub2-mkconfig -o /boot/grub2/grub.cfg` (red hat)
* this creates and populates files in /boot directory
    * If your system is a BIOS system, the name of the file is /boot/grub2/grub.cfg. 
    * On a UEFI system the file is written to /boot/efi/EFI/redhat
    * the command is grub2-mkconfig
    * BIOS system: grub2-mkconfig -o /boot/grub2/grub.cfg
    * UEFI system: grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg

### Adding new kernel versions
* GRUB 2 picks up new kernels automatically from /boot directory and adds them to the boot menu automatically 
    * nothing has to be added manually


### Install grub to MBR or EFI file system
* `sudo grub-install /dev/sda`
* `sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=grub`
* the generate the config file
    * `sudo grub2-mkconfig -o /boot/grub2/grub.cfg`

