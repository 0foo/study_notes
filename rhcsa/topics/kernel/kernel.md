
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


### Kernel Module management


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
