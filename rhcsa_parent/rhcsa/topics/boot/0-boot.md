## BIOS Boot

1.  POST (power on self test)
    * hardware testing

1. BIOS firmware starts
    * BIOS can only see disks, and read raw bytes, cannot see OS or file systems or partition tables

2. The BIOS will iterate through each storage medium in the order you set, and determine whether it can boot from that device

3. The BIOS reads the MBR to see if drive is bootable.
    * Looks at MBR stored in first boot sector of every drive
    * MBR has partition table and bootloader IF this is a bootable drive
    * If bootable drive will have a boot signature 
    * Boot signature is the last two bytes of boot sector being coded as: 0xAA55 at the very END of the MBR.
    * This indicates the presence of bootloader code.

4. IF drive is bootable BIOS either looks for an (active partition) OR (bootloader code in the MBR bootloader section) 
    1. MBR has a location for bootloader code and the BIOS can trasfer control to that which then points to stage 1.5 bootloader
    2. MBR also has the concept of **active partition** wherin a partition is marked as active via a boot flag
        * Location: One of the entries in the MBR partition table, marked with a boot indicator flag (0x80).
        * The BIOS then loads the boot sector of the active partition and transfers control to it
        *  Determines which partition's boot sector the BIOS will load and execute. Only one partition can be active at a time on an MBR disk.
        * If a bootloader is on a partition boot loader has a lot of space so will also install stage 1, 1.5, and 2 all on the active partition.
        * Stage 1.5 is specific to GRUB
        * Windows uses the active partition method and does NOT have a stage 1.5

    * Note: GRUB can use either method
        * if it uses the MBR bootloader code then it will have a stage 1.5 bootloader located in the space between MBR and the partitions
        * if it uses the active partition method then it will install stage 1, 1.5 and 2 on the partition.

    * stage 1.5
        * The common name for this file is: `core.img`
        * stage 1.5 exists becasue space in MBR (stage 1) for a bootloader is too small to contain filesystem drivers and modules needed to load stage 2
        *  The core.img file is typically located in the first few megabytes of the disk, following the Master Boot Record (MBR), but before actual partitions start, there is a gap there
        * stage 1.5 contains:
            * Basic GRUB modules: Essential modules required for GRub to start and load additional modules.
            * Filesystem drivers: Drivers to access the filesystem where the GRUB configuration and additional modules are stored.
            * Boot configuration: Basic settings and configuration for booting the operating system.

4. Full bootloader i.e. Stage 2
    * Stage 2 is usually located on the filesystem of the /boot directory of the Linux partition. 
    * The exact location can vary, but common paths include:
        * /boot/grub/
        * /boot/grub2/

    * Files: Stage 2 consists of various modules and configuration files, such as:
        * grub.cfg: The main configuration file containing boot menu entries and settings.
        * GRUB Modules: Additional modules required for specific filesystems, devices, or features.
    
    * Function: Stage 2 is larger and more complex than Stage 1. It loads additional GRUB modules and provides the full functionality of GRUB, including presenting the boot menu, reading configuration files (grub.cfg), and loading operating system kernels or other bootloaders.
            
    * Stage 2 has all the functionality to allow operating system selection and also load the kernel and init ram file system
        * SEE GRUB PAGE

## EFI Boot

### EFI System Partition(ESP)
* UEFI CAN Read partition tables and file systems
* UEFI only supports GPT partition tables
* GPT disks used for UEFI booting have an ESP(EFI system partition) 
* ESP is formatted with a FAT file system (typically FAT32). 
* Any bootloader's for the disk are stored here
* Typically mounted at `/efi` or `/boot/efi`
* Other notable details
    * This ESP partition can be identified by a specific common default well known partition type GUID: (C12A7328-F81F-11D2-BA4B-00A0C93EC93B).
    * This GUID is used to identify the ESP on GPT (GUID Partition Table) formatted disks.
    * Not always the case

### EFI file
* On EFI systems GRUB is compiled as an EFI file: for example: `/boot/efi/EFI/ubuntu/grubx64.efi`
* Besides a bootloader, EFI (Extensible Firmware Interface) includes:
    * Pre-boot applications: Utilities that can run before the operating system loads, such as diagnostic tools, firmware updates, and system configuration utilities.
    * Device drivers: Drivers for various hardware components that are required during the boot process, providing a consistent environment for the operating system to boot.
    * Boot manager: A built-in EFI application that allows users to select which operating system or device to boot from.
    * System partition: A special disk partition formatted with a file system that is accessible by the firmware, storing EFI applications, drivers, and other boot-related files.
    * Runtime services: Services available to the operating system after it has loaded, such as firmware updates and system reset functionality.
    * Secure boot: A feature that ensures only trusted software is allowed to run during the boot process, enhancing system security.



### UEFI power on to bootloader

1. Iterates through qualified drives: Drive must be GPT formatted with EFI partition with FAT file system
2. Looks in default locations or (nvram)programmed locations for grub compiled as an .efi file
3. An EFI file contains a bootloader (plus other things, see below for more detail) 


### Detail
1.  POST (power on self test)
    * hardware testing

1. UEFI firmware starts


2. UEFI looks for GPT formatted disks with FAT file system and bootloaders in ESP(EFI system partition) files with the extension *.efi
    * These can be iterated over or programmed into nvram with tools like `efibootmgr` or `bcedit`
    * can configure the order of these in UEFI config

3. UEFI finds .efi files in two ways
    1. for already installed OS's, an entry is stored during OS installation into the NVRAM of the UEFI with the location of the bootloader in the EFI partition for that OS
            * For example, Windows always adds an entry titled "Windows Boot Manager" which points to the file "\EFI\Microsoft\Bootmfgw.efi", which is the Windows bootloader in the EFI partition.
            * example: grubx64.efi: The GRUB bootloader compiled as an EFI executable. This file is used by the EFI firmware to launch the GRUB bootloader, which then loads the operating system.
            * these entries can also be manually configured using tools like `efibootmgr` on Linux or `bcdedit` on Windows.
                * `efibootmgr --create --disk /dev/sda --part 1 --label "MyNewBootEntry" --loader \\EFI\\ubuntu\\grubx64.efi --disk-guid C12A7328-F81F-11D2-BA4B-00A0C93EC93B`

    2. UEFI can look for standardized fallback locations in GPT ESP partitions on drives, this is called the fallback path
        * For example, a 64-bit UEFI system might have a fallback path of: \EFI\BOOT\BOOTX64.EFI where the bootloader will be
        * This is how it finds bootloaders that haven't been previously mapped in the NVRAM
    
    3. There are no multiple grub stages as in BIOS boot everything and all stages are via the *.efi file
        * example: there is no stage 1.5 i.e.: core.img


## Other notable features
    * Legacy boot via BIOS is also possible if configured 
    * Custom entrys with paths to bootloaders can also be configured in UEFI config
    * In a dual-boot setup on a UEFI system with GRUB as the bootloader, you can boot into Windows either via GRUB OR straight into Windows via UEFI selection




## References
* https://superuser.com/questions/420557/mbr-how-does-bios-decide-if-a-drive-is-bootable-or-not
* https://superuser.com/questions/1378816/how-does-uefi-detect-boot-devices-in-partitions

