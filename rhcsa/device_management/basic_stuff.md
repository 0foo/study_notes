## Devices

* note: hardware initialization and udev is not on the rhcsa exam!


### locations

    * sysfs(/sys) vs devtmpfs(/dev)
        * https://unix.stackexchange.com/questions/236533/sysfs-and-devtmpfs

* /sys directory
    * see directory_structure.md file
 

* /dev directory 
    * see directory)structure.md file
        

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
    * lsscsi
        * lists all scsi devices

### Network socket file locations
* not on the RHCSA just here for edification
* `/proc/net`: Contains files that display information about current network connections, such as TCP, UDP, and raw socket connections. Some relevant files include:
    * `/proc/net/tcp` for active TCP connections.
    * `/proc/net/udp` for active UDP connections.
    * `/proc/net/unix` for active UNIX domain sockets.

* `/var/run` or `/run`: Temporary files, including socket files, for services running on the system are often located here. This includes UNIX domain socket files used by various system services (e.g., MySQL, Docker, PostgreSQL).

* Application-Specific: Some applications create their own socket files in custom locations (e.g., within `/tmp` or `/var/lib`), depending on their specific configurations.
