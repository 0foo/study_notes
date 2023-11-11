## Kernel 

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
/sys
    * kernel interface that exports kernel info about various kernel subsystems and more
    * also called sysfs
    * https://en.wikipedia.org/wiki/Sysfs
    * `mount -t sysfs sysfs /sys`

/dev
    * interface with devices
    * populated by udev daemon
    * see [devices folder](devices/basic_stuff.md) for more info

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


### Kernel modules
* kernal used to require re-compile anytime anything new was added
* nowdays it's a a small core kernel and everything else is added/loaded as modules
* a module is any new kernel functionality (not just device drivers)
    * device drivers
    * file system support
    * etc.
* note: module doesn't have to interface with software can be purely software like the process scheduler


### Kernel tasks (not complete)

* hardware initialization 
* every piece of hardware has a driver
* drivers are loaded as kernel modules
* many drivers are open source but some hardware manufacturers won't publish open source drivers so have to use closed source
    * closed source drivers opens the doors to bugs
    * the massive linux community can't help fix the bugs in a closed source driver
* a badly performing driver can crash the entire linux kernel as it has top level privileged excution
* tainted kernel is a kernel that contains closed source drivers



### upgrade kernel

* `yum upgrade kernel` and `yum install kernel`
    * install new kernel alongside old kernel in /boot

* /boot directory
    * keeps the last 4 kernel files installed on system
    * GRUB looks at this and allows selecting
