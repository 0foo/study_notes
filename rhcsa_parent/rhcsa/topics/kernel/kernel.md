
### Kernel data gathering
* dmesg the same as: journalctl -dmesg the same as: journalctl -k
    * shows contents of the kernel ring buffer (KRB)
    * KRB is where kernel keeps log messages
    * note: pass -T to dmesg in order to see time as objective time vs seconds since kernel start
* uname
    * info about the linux kernel
    * -r, relevant kernel version
    * -a, much info about operating system
    * info about cpu
* cat /etc/redhat-relesae
    * info about the redhat version
* hostnamectl status
    * another place to get info on kernal and O.S. version
* view kernel threads with: `ps aux`
    * kernel threads have square brackets around them []


### upgrade kernel

* `yum upgrade kernel` and `yum install kernel`
    * install new kernel alongside old kernel in /boot

* /boot directory
    * keeps the last 4 kernel files installed on system
    * GRUB looks at this and allows selecting

* Step 1: Check the Current Kernel Version
`uname -r`

* Step 2: Update the Repository
`sudo yum update`

* Step 3: Install the New Kernel
`sudo yum install kernel`

* Step 4: Verify the Installation
`rpm -q kernel`

* Step 5: Update the GRUB Configuration
`sudo grub2-mkconfig -o /boot/grub2/grub.cfg`

* Step 6: Reboot the System
`sudo reboot`

* Step 7: Verify the New Kernel
*  After the system reboots, check the kernel version again to ensure that the new kernel is running.
`uname -r`


### Kernel general tasks
* Memory management: Keep track of how much memory is used to store what, and where
* Process management: Determine which processes can use the central processing unit (CPU), when, and for how long
* Device drivers: Act as mediator/interpreter between the hardware and processes
* System calls and security: Receive requests for service from the processes
* https://www.makeuseof.com/how-does-the-linux-kernel-work/


### The core subsystems of linux kernel:
* The Process Scheduler
    * This kernel subsystem is responsible for fairly distributing the CPU time among all the processes running on the system simultaneously.
* The Memory Management Unit (MMU)
    * This kernel sub-unit is responsible for proper distribution of the memory resources among the various processes running on the system. The MMU does more than just simply provide separate virtual address spaces for each of the processes.
* The Virtual File System (VFS)
    * This subsystem is responsible for providing a unified interface to access stored data across different filesystems and physical storage media.
* The Networking Unit
* Inter-Process Communication Unit

### Important Kernel interfaces
* /etc/proc
    * interface with linux kernel
    * many files are human readable
    * contains info about CPU, memory, mounts, 
* /sys
    * kernel interface that exports kernel info about various kernel subsystems and more
    * also called sysfs
    * https://en.wikipedia.org/wiki/Sysfs
    * `mount -t sysfs sysfs /sys`

* /dev
    * interface with devices
    * populated by udev daemon
    * see [devices folder](devices/basic_stuff.md) for more info



### Kernel modules
* kernal used to require re-compile anytime anything new was added
* nowdays it's a a small core kernel and everything else is added/loaded as modules
* a module is any new kernel functionality (not just device drivers)
    * device drivers
    * file system support
    * etc.
* note: module doesn't have to interface with software can be purely software like the process scheduler
* mod files located in /lib/modules


* hardware initialization 
* every piece of hardware has a driver
* drivers are loaded as kernel modules
* many drivers are open source but some hardware manufacturers won't publish open source drivers so have to use closed source
    * closed source drivers opens the doors to bugs
    * the massive linux community can't help fix the bugs in a closed source driver
* a badly performing driver can crash the entire linux kernel as it has top level privileged excution
* tainted kernel is a kernel that contains closed source drivers


### Kernel module management

* lsmod
    * lists all currently loaded kernel modules

* modinfo
    * to find out more about a specific kernal module
    * module alias is another name that can be used to address the module
    * params: parameters that can be set while loading the module

* modprobe/modprobe -r
    * load/unload modules
    * insmod and rmmod are legacy way to load modules
        * does not also load dependencies
    * modprobe -r will give error message if trying to unload a module that's currently in use

* lspci 
    * shows all hardware devices that have been detected on the pci bus
    * pass -k to show co-oresponding kernel modules loaded to match the hardware device

* To load a kernel module using modprobe, follow these steps:
    * Step 1: Identify the Kernel Module
    * Find the name of the kernel module you want to load. For this example, we'll use `example_module`.

    * Step 2: Load the Kernel Module
        * `sudo modprobe example_module`

    * Step 3: Verify the Kernel Module is Loaded
    * Check if the module is loaded by listing all currently loaded modules.
        * `lsmod | grep example_module`

    * Step 4: Check Module Information (Optional)
    * To see detailed information about the loaded module, use:
        * `modinfo example_module`

    * Step 5: Unload the Kernel Module (Optional)
    * If you need to remove the module, use:
        * `sudo modprobe -r example_module`



### List all available modules
* available_modules=$(find /lib/modules/$(uname -r) -type f -name '*.ko' | sed 's/.*\///;s/\.ko//')


### Locations
* mod files located in /lib/modules
* can create files in these dir's to load modules not auto loaded by udev system:
    * /etc/modules-load.d/
    * /usr/lib/modules-load.d/
    * alternative to the udev system
* can specify module parameters when loading modules here
    * /etc/modprobe.d
    * can get a list of available parameters from modinfo
        * ex: some have a debug param that can set to true and will output debug info someplace
        * in /etc/modprobe.d:
            * `options cdrom debug=1`

## The `sysctl` Command

The `sysctl` command in Linux is used to modify kernel parameters at runtime. These parameters can control various aspects of kernel operation and system behavior. The settings can be read from and written to the `/proc/sys` directory.

## Common Usages of the `sysctl` Command

### Displaying Kernel Parameters
* To display all current kernel parameters: `sysctl -a`
* To display a specific kernel parameter, such as the maximum number of open files: `sysctl fs.file-max`
* To temporarily set a kernel parameter, use the `-w` option followed by the parameter and its new value: `sysctl -w net.ipv4.ip_forward=1`
* To make kernel parameter changes permanent, add them to the `/etc/sysctl.conf` file or create a configuration file in the `/etc/sysctl.d/` directory. For example, to enable IP forwarding permanently, you would add the following line to one of these files: `net.ipv4.ip_forward=1`



## Sysctl.conf

* The `sysctl.conf` file is a configuration file in Linux systems used to modify kernel parameters at runtime. These parameters control various aspects of the system’s behavior, such as networking, memory management, and file system performance. The `sysctl.conf` file allows administrators to set these parameters persistently, ensuring that the changes remain effective across system reboots.

* Key Points About `sysctl.conf`:

1. **Location:**
   - The `sysctl.conf` file is typically located at `/etc/sysctl.conf`.

2. **Purpose:**
   - It is used to configure kernel parameters that can be read and modified via the `/proc/sys/` directory. These parameters control system and kernel behavior.

3. **Syntax:**
   - The file consists of lines with the format:
     ```bash
     parameter = value
     ```
   - For example:
     ```bash
     vm.swappiness = 10
     net.ipv4.ip_forward = 1
     ```

4. **Applying Changes:**
   - Changes made to `sysctl.conf` are not automatically applied until the system is rebooted or the `sysctl` command is used to reload the settings.
     ```bash
     sysctl -p /etc/sysctl.conf
     ```

### Example `sysctl.conf` Entries:

1. **Swappiness:**
   ```bash
   vm.swappiness = 10
