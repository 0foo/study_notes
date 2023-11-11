## initramfs


* essentially an entire operating system loaded completely in RAM
* has all of the modules/hardware drivers
* has full udev
* has systemd called init though




### Goal
* essentially exists to get the root file system mounted which has all the host OS files available
* this is tricky because there's alot of different hardware and alot of different ways for a root drive to be mounted
    * RAID, LVM, Network Mount, etc.
* External storage drives which root partitions live require hardware drivers, and block files to access, and other configuration
* RAM and CPU are all available at boot time so an OS is built in RAM
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
* dracut with no parameters will create an initramfs file system for the currently loaded kernel
* can specify parameters in files below to customize running dracut command
    * note: cli parameters will override the config file param's

### Dracut files
* /usr/lib/dracut/dracut.conf.d/*.conf
    *  contains the system default configuration files.
* /etc/dracut.conf.d 
    * contains custom dracut configuration files.
* /etc/dracut.conf 
    * is used as the master configuration file.
    * can specify options for building initramfs
