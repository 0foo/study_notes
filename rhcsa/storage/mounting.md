* Mounting
    * allows mounting different devices to directories in the file structures
    * the device is formatted in such a way that now the file system can read the contents on the device

* Multi-mount architecture
    * prevents a single mount from filling up all the space blocking space for potentially critically needed files
    * provides added security. 
        * can mount with mount options such as noexec and nodev

* commonly mounted directories
    * /boot, /var(grows in uncontrolled/dynamice way), /home(security reasons), /usr(can mount as read only so no user access) 


* Commands for managing mounts
    * /proc/mounts directory
        * contains mount data

    * mount
        * overview of all mounted devices
        * same data as /proc/mount
        * also shows kernel interfaces
    * df -Th
        * size info about mounts
    * findmnt
        * tree structure showing relationship between mounts
        * findmnt -A 