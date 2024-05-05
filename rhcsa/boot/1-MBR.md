### MBR

* can view mbr with: `dd if=/dev/sda bs=512 count=1 | hexdump -C`

* view partition table info with: `parted -l` 
* can view type of partition table mbr or gpt with `parted -l`
    * msdos == MBR

* manipulate the partition table
    * parted
    * gdisk
    * fdisk
    * https://unix.stackexchange.com/questions/104238/fdisk-vs-parted


* MBR limitations
    * only on drives <2TB
    * only up to 4 partitions

* protective MBR
    * the very first LBA(logical block address, typically 0-512 bytes) on a GPT, LBA 0, contains legacy MBR information. 
    * The GPT boot header takes the next LBA, at LBA 1(513-1025). In this manner, we provide a recognizable MBR for older disk applications, and ensure the GPT won’t accidentally be overwritten. This is known as the Protective MBR, for just these reasons.


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