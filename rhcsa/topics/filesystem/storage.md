### Storage
* find your block size: `lsblk -o NAME,PHY-SeC`
* dd command
    * The dd tool is super useful for converting and copying data. It reads input from a file or data stream and writes it to a file or data stream. 
    * $ dd if=/home/pete/backup.img of=/dev/sdb bs=1024 
        * if=file - Input file, read from a file instead of standard input
        * of=file - Output file, write to a file instead of standard output
        * bs=bytes - Block size, it reads and writes this many bytes of data at a time. You can use different size metrics by        denoting the size with a k for kilobyte, m for megabyte, etc, so 1024 bytes is 1k
        * count=number - Number of blocks to copy.
* lsusb
    * lists all usb devices
* lspci
    * lists all pci devices
* lsscsi
    * lists all scsi devices


### Partition table
* partition table: parted, gdisk, fdisk
    * view partition table: parted -l



### Mounts
* Commands for managing mounts
    * View mounts
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
    * mount 

