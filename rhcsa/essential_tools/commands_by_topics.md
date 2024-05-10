## Commands by topic


### System resources

* Memory
    * free
    * /proc/meminfo

* cpu
    * top

* disk
    * du
    * df




### Processes
* strace <command>
    * can see all system calls a command makes






### Hardware 







### Storage
* find your block size: `lsblk -o NAME,PHY-SeC`

### Partition table
* partition table: parted, gdisk, fdisk
    * view partition table: parted -l



### Boot
* can view MBR: `dd if=/dev/sda bs=512 count=1 | hexdump -C`
* view boot logs: 
* view kernel boot command/kernel params from running system: `cat /proc/cmdline`




### Network
* DNS
* IP




