## initramfs
*  provides a temporary root filesystem during the boot process and is customizable to include drivers, modules, and scripts necessary for booting the main filesystem
* essentially an entire operating system loaded completely in RAM
* has all of the modules/hardware drivers to intitialize the system
* has full udev
* has systemd called init though

### Kernel + intraramfs

3. Kernel + initramfs take control
    1. purpose: to locate/identify the root OS
    1. creates a fully operational OS in RAM
    1. loads funtionality needed to access the root file system
    1. loads /sbin/init and udev in initramfs RAM file system which do work of setting up system to identify root FS
    1. /sbin/init is really just systemd but with different terminology in initramfs
    1. /sbin/init runs initrd.target to load the units that make up a minimal OS
    1. After the “real” root file system has been identified: it is checked for errors and mounted.
    1. If this is successful, the initramfs is cleaned and the systemd daemon on the root file system is executed. 

4. systemd on host storage hardware takes control
    1. runs default.target
    1. login screen
    1. note: login screen presented in parallel with other units loading, so login does not mean it's fully  operational
    1. once default.target loaded fully, system is operation

* The kernel and initramfs is stored in the /boot directory
    * This directory is read by GRUB and must be formatted in a format GRUB can read
    * https://unix.stackexchange.com/questions/175728/what-file-system-should-a-grub-2-boot-partition-use
    * Note: many people format /boot with ext2,3,or 4 no matter what format the main file system is using
    * Also if the main file system is encrypted will need to have a seperate unencrypted partition for GRUB/initramfs

### Files
* typically in /boot partition
* named either initramfs or initrd depending on distribution
* The intraramfs has a filename containing the kernel version that it cooresponds to
* initramfs is highly customizable to get it the drivers/modules/functionality it needs to mount the root filesystem from wherever it is stored

### Goal
* essentially exists to get the root file system mounted which has all the host OS files available
* this is needed because there's alot of different storage hardware and alot of different ways for a root drive to be mounted which GRUB doesn't have space to understand and it also isn't a bootloader or kernel's responsibility to do system initialization tasks from the file system.
    * RAID, LVM, Network Mount, Encrypted file systems, etc.
* External storage drives which root partitions live require hardware drivers, and block files to access, and other configuration
* RAM and CPU are all available at boot time and kernel can manage RAM with no additional drivers needed, so an OS is built in RAM
    * This full mini OS in RAM is used to configure and set up the hardware devices to be able to configure/acces the devices which contain root file system

### Function of init(systemd on initramfs)
* Loading Kernel Modules
    * Depending on your hardware configuration, special drivers may be needed to access the hardware components of your computer (the most important component being your hard disk). To access the final root file system, the kernel needs to load the proper file system drivers. 
* Providing Block Special Files i.e. /dev file's for drive access
    * The kernel generates device events depending on loaded modules. udev handles these events and generates the required special block files on a RAM file system in /dev. Without those special files, the file system and other devices would not be accessible. 
* Managing RAID and LVM Setups
    * If you configured your system to hold the root file system under RAID or LVM, init on initramfs sets up LVM or RAID to enable access to the root file system later. 
* Managing the Network Configuration
    * If you configured your system to use a network-mounted root file system (mounted via NFS), init must make sure that the proper network drivers are loaded and that they are set up to allow access to the root file system.
    * If the file system resides on a network block device like iSCSI or SAN, the connection to the storage server is also set up by init on initramfs. SUSE Linux Enterprise Server supports booting from a secondary iSCSI target if the primary target is not available. For more details regarding configuration of the booting iSCSI target refer to Section 14.3.1, “Using YaST for the iSCSI Initiator Configuration”. 

### Process (general/high level, may not be complete)

1. init(same as systemd except in initramfs) is started
1. udev started
1. initrd.target 
1. After the “real” root file system has been found, it is checked for errors and mounted.
1. If this is successful, the initramfs is cleaned and the systemd daemon on the root file system is executed. 


### Dracut
* Dracut is a tool used to create the initramfs image. 
* It's a modular, scriptable utility that allows for a lot of customization and flexibility. Dracut is designed to have modules that can be added or removed depending on the specific needs of the system, which makes it very powerful for handling different hardware configurations or boot requirements.
* dracut with no parameters will create an initramfs file system for the currently loaded kernel
* can specify parameters in files below to customize running dracut command
    * note: cli parameters will override the config file param's

### Dracut files
* /etc/dracut.conf 
    * is used as the master configuration file.
    * can specify options for building initramfs
* /usr/lib/dracut/dracut.conf.d/*.conf
    *  contains the system default configuration files.
* /etc/dracut.conf.d 
    * contains custom dracut configuration files.



### Historical Context and Usage

    * Historical Root: The initrd (initial ramdisk) is an older technology that involves loading a complete disk image into memory at boot time. It was used to provide an early userspace environment where necessary drivers and scripts could run to mount the real root filesystem.
    * Evolution to initramfs: initramfs was introduced to replace initrd because it is more flexible and integrated directly with the kernel, allowing the kernel to unpack the initramfs archive into a ramfs (RAM filesystem) at boot time. Unlike initrd, which was a separate file system image loaded into a memory disk, initramfs becomes part of the kernel's memory usage from the start.
    * Despite the differences, the filename initrd is still used in many distributions to refer to what is technically an initramfs:
    * Ubuntu and Debian: These distributions commonly name their initramfs files as initrd.img-<kernel-version>, reflecting the older terminology.
    * Generic Naming: Other distributions might also use names like initrd-<kernel-version>.img for files that are technically initramfs archives.


### CHAT GPT summary
* Even if GRUB supports your filesystem directly, there are still compelling reasons for using an initramfs. While GRUB's ability to read various filesystems is crucial for loading the kernel and initramfs files themselves, the role of initramfs goes beyond what GRUB is designed to handle. Here’s why initramfs remains essential:

1. Early Userspace Environment

    * initramfs provides a controlled, user-space environment before the actual root filesystem is mounted. This environment is crucial for performing a variety of initial setup and configuration tasks that are beyond the scope of GRUB, which is fundamentally a bootloader, not a system initializer.

2. Driver Availability

    * Dynamic Module Loading: Many modern Linux systems require specific drivers that are not built into the kernel image but need to be loaded dynamically to access the hardware, particularly at boot. For example, systems with special storage configurations (like LVM, encrypted filesystems, or advanced RAID setups) require additional modules to access the root filesystem. initramfs can contain these necessary modules and load them early in the boot process.
    
    * Hardware Initialization: Some systems may require complex hardware initialization that the kernel needs to handle but can only do so once specific drivers or firmware are loaded, which can be provided by initramfs.

3. Complex Storage Configurations

    * Mounting the Root Filesystem: For systems using non-standard root filesystems that require additional processing (like decryption or network mounts), initramfs can run the necessary tools to prepare these filesystems before handing off control to the main kernel.
    * Essential Tools and Scripts: initramfs often includes a variety of tools and scripts that facilitate the configuration and setup of the environment necessary to mount the root filesystem properly.

4. Pre-Root Filesystem Utilities

    * Pivotal for Repairs and Diagnostics: If the root filesystem is damaged or otherwise unbootable, initramfs can provide a minimal environment with tools to diagnose and repair filesystem issues. This is often accessible through recovery modes that boot into initramfs directly.
    * Custom Scripts and Early Setup: Some system configurations require running custom scripts before the root filesystem is mounted. initramfs is ideal for such tasks, allowing administrators to configure network interfaces, set up hostname, or load additional kernel parameters.

5. Flexibility and Customization

    * Tailoring Boot Process: Systems that need to perform specific actions during bootup, such as configuring kernel parameters dynamically, adjusting system settings based on detected hardware, or managing sophisticated security measures, rely on the flexibility provided by initramfs.

    * Fallback and Security Features: initramfs supports fallback mechanisms and can include features like drop to a rescue shell if the boot process fails at certain stages.

* Conclusion
    * Even though GRUB is capable of loading the kernel from a supported filesystem, the kernel alone often cannot handle all the preliminary actions required for modern computing environments directly. initramfs fills this gap by acting as a bridge between the bootloader (GRUB) and the fully initialized operating system. It ensures that all prerequisites for a successful boot and system operation are met, particularly in complex or specialized hardware configurations.