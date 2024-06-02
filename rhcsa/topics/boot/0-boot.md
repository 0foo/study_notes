## Boot 

### Power on
1.  POST (power on self test)
    * hardware testing



### BIOS - power on to bootloader

1. BIOS firmware starts
    * BIOS can only see disks, and read raw bytes, cannot see OS or file systems or partition tables

2. The BIOS will iterate through each storage medium in the order you set, and determine whether it can boot from that device (via the MBR data). If it can, it does - if not, it continues iterating through the other devices (again, in the order you selected).
    * MBR stored in first boot sector of every drive, has partition table and bootloader if bootable drive
    * the BIOS checks for the boot signature, a specific sequence of bytes (0x55AA), at the end of the MBR. This indicates the presence of bootloader code.

3.  Bootloader: If the boot signature and active partition are found, the BIOS loads the bootloader code from the boot sector into memory and executes it. The bootloader then proceeds to load the operating system.
    *   NOTE: if this drive is not bootable will either get an error message or the device will return control back to the BIOS

4. BIOS Bootloader is typically in stages due to limited space in MBR
    * stage 1 is located in MBR

    * GRUB has a stage 1.5
        * Location: Stage 1.5 is located in the unused sectors between the MBR and the first partition on the disk.
        * Function: Stage 1.5 contains filesystem drivers necessary to access files stored on the filesystems of the disk. It enables GRUB to read configuration files and other necessary data from the filesystem before loading the main GRUB modules.
            * note: it doesn't mount the drive since there's no kernel yet to mount it into BUT it can READ from certain file systems.

    * stage 2:
        * much more complex bootloader as it has much more space available for functionality
        * in non-GRUB: indicated by the active/bootable partition flag in the MBR, phase 1 bootloader looks for this flag and loads the first sector of that partition kicking off the tage 2 bootloader
        * in GRUB: location is pointed to in Stage 1.5
            * the code from stage 1.5 knows which block the second stage starts at (completely ignoring the partition table and the 'active' flag), and this might vary between disks, so the bootsector must be written by the grub-install program individually for each disk.
            * Location: Stage 2 of GRUB, is also known as the core image (core.img),
            * Function: Stage 2 is larger and more complex than Stage 1. It loads additional GRUB modules and provides the full functionality of GRUB, including presenting the boot menu, reading configuration files (grub.cfg), and loading operating system kernels or other bootloaders.
            
4. This bootloader will then read the partition table and on dual booting systems bootloader will allow operating system selection


* https://superuser.com/questions/420557/mbr-how-does-bios-decide-if-a-drive-is-bootable-or-not
* https://superuser.com/questions/1378816/how-does-uefi-detect-boot-devices-in-partitions



### UEFI power on to bootloader

1. UEFI firmware starts
    * UEFI CAN Read partition tables and file systems
    * UEFI only supports GPT partition tables
    * GPT disks used for UEFI booting have an ESP(EFI system partition) formatted with a FAT file system (typically FAT32). This partition is identified by a specific partition type GUID (C12A7328-F81F-11D2-BA4B-00A0C93EC93B).
    * Any bootloader's for the disk are stored here

2. UEFI looks for GPT formatted disks and bootloaders in ESP files with the extension *.efi
    * can configure the order of these in UEFI config

3. UEFI finds bootable drives in two ways
    1. for already installed OS's, an entry is stored during OS installation into the NVRAM of the UEFI with the location of the bootloader in the EFI partition for that OS
            * For example, Windows always adds an entry titled "Windows Boot Manager" which points to the file "\EFI\Microsoft\Bootmfgw.efi", which is the Windows bootloader in the EFI partition.
            * these entries can also be manually configured using tools like `efibootmgr` on Linux or `bcdedit` on Windows.

    2. UEFI can look for standardized fallback locations in GPT ESP partitions on drives, this is called the fallback path
        * For example, a 64-bit UEFI system might have a fallback path of: \EFI\BOOT\BOOTX64.EFI where the bootloader will be
        * This is how it finds bootloaders that haven't been previously mapped in the NVRAM

    * Legacy boot via BIOS is also possible if configured 
    * Custom entrys with paths to bootloaders can also be configured in UEFI config
    * In a dual-boot setup on a UEFI system with GRUB as the bootloader, you can boot into Windows either via GRUB OR straight into Windows via UEFI selection

3. There are no multiple grub stages as in BIOS boot, there is no core.img...everything and all stages are via the *.efi file


### Bootloader
* Bootloader takes control
    * GRUB on linux
    * Can do operating system selection on dual boot machines by EITHER looking at bootloader files or looking at partition table
    * GRUB looks at it's configuration/or the UI selection menu 
    * Grub will then put together kernel params + kernel + initramfs file system

