## Devices

* note: hardware initialization and udev is not on the rhcsa exam!


### locations

    * sysfs(/sys) vs devtmpfs(/dev)
        * https://unix.stackexchange.com/questions/236533/sysfs-and-devtmpfs

* sys directory
    * used to view information and manage the device
    * contains all the information for all devices on your system, such as the manufacturer and model, where the device is plugged in, the state of the device, the hierarchy of devices and more. 
    * The files you see here aren't device nodes, so you don't really interact with devices from the /sys directory, rather you are managing devices. 
    * Note: in many cases you CAN interact with the device though
    * kernel docs here:
        * https://www.kernel.org/doc/Documentation/filesystems/sysfs.txt


* dev directory
    * Full of device files/nodes for devices attached to the system
    * Device files/nodes are abstractions of standard devices that applications interact with via I/O system calls.
    * Userspace applications can use these device nodes to interface with the systems hardware, 
        * For example, the X server will "listen to" /dev/input/mice so that it can relate the user's mouse movements to moving the visual mouse pointer. 
     * Note: some hardware interfaces not in /dev, typically for legacy reasons and the code is too involved to change now
        * network interfaces not in /dev
            * these were historically considered not amenable to file style communication
                * can't use simple read() write() calls to communicate like most file style hardware devices
                * networking communicates in packets vs bytes and has connections/streams which come and go frequently
                * connections require more than simple file name passed to read()
            * network applications are more complex than file accessing applications
            * network sockets are files though
        * video
            * x-server writes to video adaptor memory directly
            * if communicated with kernel system calls each time need to change video memory would be too slow 
        * https://unix.stackexchange.com/questions/23199/why-are-network-interfaces-not-in-dev-like-other-devices
        * https://askubuntu.com/questions/306594/why-do-ethernet-devices-not-show-up-in-dev
    * /dev directory is populated by udev daemon
        

* udev
    * managed with udevadm command
    * udevadm info --query=all --name=/dev/sda
    * udevadm monitoru
    * can view udev database

    * udev general process:
        1. udevd daemon is running on the system and it listens for messages from the kernel about devices connected to the system.
        1. udevd sees the event and if it has a specifically formatted identifier will pass it to modprobe which has a mapper of identifiers to drivers and will load that module automatcially
        * https://documentation.suse.com/sles/12-SP5/html/SLES-all/cha-udev.html#sec-udev-drivers

        2. udevd will also look at rules defined in /etc/udev/rules.d or /usr/lib/udev/rules.d to run custom events
        3. udevd will pass info to modprobe which will load the device driver
            * ex: adding permissions, nameing a specific device, adding a symlink in /dev to communicate with the device
    * udevd will then use information in sysfs (i.e. /sys directory) to create the device files/nodes matching the systems hardware in /dev
    * general udev flow explained here:
        * https://unix.stackexchange.com/questions/330186/where-does-modprobe-load-a-driver-that-udev-requests
    * depending on those rules it will most likely create device nodes and symbolic links for the devices. 
    * Can write custom udev rules if needed
        * https://www.reactivated.net/writing_udev_rules.html
     * udevd rules specified in:
        * /usr/lib/udev/rules.d
            * system udev rules
        * /etc/udev/rules.d
            * custom udev rules by users
    * https://unix.stackexchange.com/questions/756092/whats-the-reason-to-add-a-symlink-to-dev-directory/756094#756094

* can view most devices in the /dev directory
* `ls -l /dev`
    * Output:
        * Permissions
        * Owner
        * Group
        * Major Device Number
        * Minor Device Number
        * Timestamp
        * Device Name

* Major/Minor Device Number
    * The major sets the type of the device, usually the driver associated with it. 
    * The minor list the first, second, third, ... device of that type.
    *  It is common for a driver to control several devices. the minor number provides a way for the driver to differentiate among them. 
    * There's only one driver per major number and multiple minors are handled by it.
    * i.e. a hard disk will have one major number and the partitions will each have a minor number

* finding a device driver co-oresponding to a device
    * https://unix.stackexchange.com/questions/97676/how-to-find-the-driver-module-associated-with-a-device-on-linux

* device types
    * c - character
        * communicate directly with hardware each time send a series of character with write()
        * (not always this simple but that's the theory)
        * see /dev/random or /dev/null

    * b - block
        * communicates a block at a time with hardware
        * buffering involved
        * A block special file is normally distinguished from a character special file by providing access to the device in a manner such that the hardware characteristics of the device are not visible
        * note: many devices could be accessed in a character or block way but it's up to the device driver
        * the data is typically organized into files on a block device

    * p - pipe
        * Named pipes allow two or more processes to communicate with each other, these are similar to character devices, but instead of having output sent to a device, it's sent to another process. 
    * s - socket
        * Socket devices facilitate communication between processes, similar to pipe devices but they can communicate with many processes at once.


### Device information gathering
* for all the following commands pass -v for more info
* lsusb
    * lists all usb devices
* lspci
    * lists all pci devices
* lsscsi
    * lists all scsi devices


### Commands for working with devices
    * dd command
        * The dd tool is super useful for converting and copying data. It reads input from a file or data stream and writes it to a file or data stream. 
        * $ dd if=/home/pete/backup.img of=/dev/sdb bs=1024 
            * if=file - Input file, read from a file instead of standard input
            * of=file - Output file, write to a file instead of standard output
            * bs=bytes - Block size, it reads and writes this many bytes of data at a time. You can use different size metrics by        denoting the size with a k for kilobyte, m for megabyte, etc, so 1024 bytes is 1k
            * count=number - Number of blocks to copy.