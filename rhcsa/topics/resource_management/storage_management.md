## Storage
* find your block size: `lsblk -o NAME,PHY-SeC`


* dd command
    * The dd tool is super useful for converting and copying data. It reads input from a file or data stream and writes it to a file or data stream. 
    * $ dd if=/home/pete/backup.img of=/dev/sdb bs=1024 
        * if=file - Input file, read from a file instead of standard input
        * of=file - Output file, write to a file instead of standard output
        * bs=bytes - Block size, it reads and writes this many bytes of data at a time. You can use different size metrics by        denoting the size with a k for kilobyte, m for megabyte, etc, so 1024 bytes is 1k
        * count=number - Number of blocks to copy.
        * default block size on most OS's is 512, on newer drives being released it's being upgraded to 4096(also called 4k sectors)


* lsusb
    * lists all usb devices
* lspci
    * lists all pci devices
* lsscsi
    * lists all scsi devices


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



## Mounts
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




## Partition table
* view partition table info with:
    * `parted -l` 
    * `lsblk` (can pass -f to view file systems)
    * `gdisk -l <some /dev device>`
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




## Swap

   Working with swap space is a critical part of managing memory in a Linux system, and it's an essential topic for the RHCSA (Red Hat Certified System Administrator) exam. Here's what you need to know:

**1. Understanding Swap Space:**
   - **Purpose:** Swap space is used when the physical RAM (Random Access Memory) is full. Inactive pages in memory are moved to the swap area to free up RAM for other processes.
   - **Types of Swap:** Swap can be a dedicated swap partition or a swap file.

**2. Creating and Enabling Swap Space:**
* There are two separate ways to enable swap space
  1. **Creating a Swap Partition:**
     - Use a partitioning tool like `fdisk`, `parted`, or `gdisk` to create a new partition of type `Linux swap` (type `82` in `fdisk`).
     - Initialize the partition as swap space using `mkswap`.
       ```bash
       mkswap /dev/sdX1
       ```
     - Enable the swap partition.
       ```bash
       swapon /dev/sdX1
       ```
  2. **Creating a Swap File:**
     - Create an empty file using `dd` or `fallocate`.
       ```bash
       dd if=/dev/zero of=/swapfile bs=1M count=1024
       # or
       fallocate -l 1G /swapfile
       ```
     - Set the correct permissions for the swap file.
       ```bash
       chmod 600 /swapfile
       ```
     - Initialize the file as swap space.
       ```bash
       mkswap /swapfile
       ```
     - Enable the swap file.
       ```bash
       swapon /swapfile
       ```

**3. Making Swap Space Persistent:**
   - To ensure the swap space is available after a reboot, add an entry to `/etc/fstab`.
     ```bash
     /dev/sdX1 none swap sw 0 0
     # or
     /swapfile none swap sw 0 0
     ```

**4. Managing Swap Space:**
   - **Disabling Swap:**
     - To temporarily disable swap space, use the `swapoff` command.
       ```bash
       swapoff /dev/sdX1
       # or
       swapoff /swapfile
       ```
   - **Removing Swap Space:**
     - To permanently remove a swap partition or file, disable it and then remove its entry from `/etc/fstab`.
     - For a swap file, also delete the file.
       ```bash
       rm /swapfile
       ```

**5. Monitoring Swap Usage:**
   - View locations on storage medium where swap is originating from
        * `swapon -s` 
   - Use commands like `swapon -s`, `free -m`, or `vmstat` to check the status and usage of swap space.
     ```bash
     swapon -s
     free -m
     vmstat
     ```

**6. Swapiness:**
* Swappiness is a Linux kernel parameter that controls the relative weight given to swapping out runtime memory pages, as opposed to dropping pages from the system page cache. This parameter affects how aggressively the kernel uses swap space to free up RAM.

* Default value: The default swappiness value is usually 60. This means the kernel will start to swap out pages when the system's free memory falls below 40% (100 - 60).

* Range of Values 
  * The swappiness parameter can be set between 0 and 100:
      * 0: The kernel will avoid swapping as much as possible. It will prefer to drop pages from the page cache rather than using swap space.
      * 100: The kernel will use swap space aggressively, even if there is still some free memory available.
      * Low Swappiness (0-30): The system will be reluctant to use swap space and will prefer to use free memory and page cache. This is useful for systems with a lot of RAM and where performance is critical, such as databases or real-time applications.
      * Medium Swappiness (30-60): This is the default range and balances between using swap and keeping data in RAM.
      * High Swappiness (60-100): The system will use swap space more aggressively. This can be useful for systems with limited RAM where it is important to avoid running out of memory, such as virtual machines or systems running many applications.
   - **Checking Swappiness:**
     ```bash
     cat /proc/sys/vm/swappiness
     ```
   - **Setting Swappiness:**
     - To change the swappiness value temporarily:
       ```bash
       sysctl vm.swappiness=10
       ```
     - To change it permanently, add or modify the entry in `/etc/sysctl.conf`.
       ```bash
       vm.swappiness = 10
       ```

**7. Best Practices:**
   - Ensure swap space is sufficient but not excessive. The amount of swap space needed depends on the system's workload and RAM size.
   - Regularly monitor swap usage to identify if adjustments are needed.

Understanding these concepts and commands will help you effectively manage swap space on a Linux system and prepare for the RHCSA exam.
