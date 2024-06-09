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



### Storage
* Logical Block Addressing
    * abstracts away cylinders and heads and just allows accessing the harddrive in contiguous linear storage units
    * block size
    * block number 
    * find your block size: `lsblk -o NAME,PHY-SeC`
    * dd uses this with it's -bs(blocksize) paramter


* CHS is an earlier form of hard disk addressing. It stands for:
    * C: cylinder, the valid range is between 0 and 1023 cylinders.
    * H: Head, the valid range is between 0 and 254 heads (formerly 0-15).
    * S: Sector, the valid range is between 1 and 63 sectors.




### Partition table
* view partition table info with: `parted -l` 
* can view type of partition table mbr or gpt with `parted -l`
    * msdos == MBR

* manipulate the partition table
    * parted
    * gdisk
    * fdisk
    * https://unix.stackexchange.com/questions/104238/fdisk-vs-parted

* MBR partition table limitations
    * only on drives <2TB
    * only up to 4 partitions

* protective MBR
    * the very first LBA(logical block address, typically 0-512 bytes) on a GPT, LBA 0, contains legacy MBR information. 
    * The GPT boot header takes the next LBA, at LBA 1(513-1025). In this manner, we provide a recognizable MBR for older disk applications, and ensure the GPT won’t accidentally be overwritten. This is known as the Protective MBR, for just these reasons.

1. **Capacity and Size Limitations**:
   - MBR: MBR partitioning scheme supports up to 2 TB (terabytes) of storage space and up to four primary partitions. To overcome this limitation, users often create extended partitions, which can contain multiple logical partitions.
   - GPT: GPT partitioning scheme supports significantly larger storage capacities, up to 9.4 zettabytes (ZB), and allows for up to 128 partitions by default. It does not have the limitations of MBR, making it suitable for modern large-capacity storage devices.

2. **Partitioning Structure**:
   - MBR: MBR uses a traditional partitioning scheme where the partition table is located in the first sector (the MBR sector) of the storage device. It employs a 32-bit addressing scheme and utilizes partition types like primary, extended, and logical partitions.
   - GPT: GPT uses a more modern partitioning scheme based on GUIDs (Globally Unique Identifiers). It stores partition information in multiple locations across the disk, including a primary partition table header and backup partition table header at the beginning and end of the disk, respectively. This redundancy enhances data integrity and reliability.

3. **Boot Process**:
   - MBR: MBR includes a small program called the boot loader in its first sector, which is executed by the BIOS firmware during the boot process. The boot loader loads and executes the operating system's bootloader from the active partition.
   - GPT: GPT systems use UEFI (Unified Extensible Firmware Interface) firmware instead of BIOS. UEFI firmware can directly read and boot from GPT partitions without the need for a separate boot loader in the MBR. This enables faster and more efficient booting, as well as support for features like Secure Boot.

4. **Partitioning and Data Structures**:
   - MBR: MBR uses a simple partition table format with a maximum of four entries, each describing a partition's starting and ending sectors, type, and boot flag.
   - GPT: GPT utilizes a more robust partition table format with a 64-byte partition entry for each partition, including attributes such as partition type GUID, partition GUID, starting and ending LBA (logical block address), partition name, and other metadata. This structure supports advanced features like data redundancy and partition GUIDs for improved identification.