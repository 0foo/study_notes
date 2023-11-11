## Modules

* see devices/basic_stuff.md for more info


### Locations
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


### Module management


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
