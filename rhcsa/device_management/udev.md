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