
### Boot
* can view MBR: `dd if=/dev/sda bs=512 count=1 | hexdump -C`
* view boot logs: 
* view kernel boot command/kernel params from running system: `cat /proc/cmdline`

