## Devices

* note: hardware initialization and udev is not on the rhcsa exam!


### Set run profiles for performance management

* tuned/tuned-adm
    * can set different profiles for a system
    * this will optimize performance for that system type

* check active profile: `sudo tuned-adm active`
* change active profile: `sudo tuned-adm profile laptop-battery-powersave`
* list all profiles: `sudo tuned-adm list`

### locations

* sysfs(/sys) vs devtmpfs(/dev)
    * https://unix.stackexchange.com/questions/236533/sysfs-and-devtmpfs

* /sys directory
    * see directory_structure.md file
 

* /dev directory 
    * see directory structure.md file
        


* in `ls -v /dev` Major/Minor Device Number
    * The major sets the type of the device, usually the driver associated with it. 
    * The minor list the first, second, third, ... device of that type.
    * It is common for a driver to control several devices. the minor number provides a way for the driver to differentiate among them. 
    * There's only one driver per major number and multiple minors are handled by it.
    * i.e. a hard disk will have one major number and the partitions will each have a minor number

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



### Commands for working with devices
    * dd command
    * for all the following commands pass -v for more info
    * lsusb
        * lists all usb devices
    * lspci
        * lists all pci devices
        * pass -k for co-oresponding kernel modules
    * lsscsi
        * lists all scsi devices
    * lscpu
        * Processor details
        * show proc/core hardware info
        * can view the number of cores in system
    * `ls -l /dev`
        * can view most devices in the /dev directory
        * Output:
            * Permissions
            * Owner
            * Group
            * Major Device Number
            * Minor Device Number
            * Timestamp
            * Device Name
    * can view a ton of system info with dmidecode







## BELOW NOT ON RHCSA


### Network socket file locations
* not on the RHCSA just here for edification
* `/proc/net`: Contains files that display information about current network connections, such as TCP, UDP, and raw socket connections. Some relevant files include:
    * `/proc/net/tcp` for active TCP connections.
    * `/proc/net/udp` for active UDP connections.
    * `/proc/net/unix` for active UNIX domain sockets.

* `/var/run` or `/run`: Temporary files, including socket files, for services running on the system are often located here. This includes UNIX domain socket files used by various system services (e.g., MySQL, Docker, PostgreSQL).

* Application-Specific: Some applications create their own socket files in custom locations (e.g., within `/tmp` or `/var/lib`), depending on their specific configurations.


### troubleshooting devices

* not on RHCSA, just here for edification
* finding a device driver co-oresponding to a device
    * https://unix.stackexchange.com/questions/97676/how-to-find-the-driver-module-associated-with-a-device-on-linux


## UDEV

* not on the RHCSA just here for edification
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