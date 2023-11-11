## Boot 


* The kernel and initramfs is stored in the /boot directory
    * This directory is read by GRUB and must be formatted in a format GRUB can read
    * https://unix.stackexchange.com/questions/175728/what-file-system-should-a-grub-2-boot-partition-use
    * Note: many people format /boot with ext2,3,or 4 no matter what format the main file system is using
    * Also if the main file system is encrypted will need to have a seperate unencrypted partition for GRUB/initramfs





### Boot high level examination
1. BIOS has control
    1.  POST 
        * hardware testing
    1. identify boot device
        * there's a boot device hierarchy set in the BIOS and the default boot device is indicated there
        * NOTE: can typically hit a hotkey to bring up a menu to set boot device manually to override 
    1. BIOS looks in MBR of boot device for boot loader and passed control to that
1. Bootloader takes control
    * GRUB on linux
    * GRUB looks at it's configuration/or the UI selection menu 
    * Grub will then put together kernel params + kernel + initramfs file system
1. Kernel + initramfs take control
    1. purpose: to locate/identify the root OS
    1. creates a fully operational OS in RAM
    1. loads funtionality needed to access the root file system
    1. loads /sbin/init and udev in initramfs RAM file system which do work of setting up system to identify root FS
    1. /sbin/init is really just systemd but with different terminology in initramfs
    1. /sbin/init runs initrd.target to load the units that make up a minimal OS
    1. After the “real” root file system has been identified: it is checked for errors and mounted.
    1. If this is successful, the initramfs is cleaned and the systemd daemon on the root file system is executed. 
1. systemd on host storage hardware takes control
    1. runs default.target
    1. login screen
    1. note: login screen presented in parallel with other units loading, so login does not mean it's fully  operational
    1. once default.target loaded fully, system is operation




