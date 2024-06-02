* POST Hardware configuration 
    * (F2, Esc, F10, or another key). 
    * Replace hardware.

* Selecting the bootable device 
    * BIOS/UEFI configuration or hardware boot menu. 
    * Replace hardware or use rescue system.

* Loading the boot 
    * loader grub2-install and edits to /etc/defaults/grub. 
    * GRUB boot prompt and edits to /etc/defaults/ grub, followed by grub2-mkconfig.

* Loading the kernel 
    * Edits to the GRUB configuration and /etc/ dracut.conf. 
    * GRUB boot prompt and edits to /etc/defaults/grub, followed by grub2-mkconfig.

* Starting /sbin/init 
    * Compiled into initramfs. 
    * init= kernel boot argument
    * rd.break kernel boot argument.

* Processing initrd.target 
    * Compiled into initramfs. 
    * Not typically required.

* Switch to the root file system 
    * Edits to the /etc/fstab file. 
    * Edits to the /etc/fstab file.

* Running the default target 
    * Using systemctl set-default to create the /etc/systemd/system/ default.target symbolic link 
    * Start the rescue.target as a kernel boot argument.


### Kernel parameters
* remove the rhgb and quiet to view errors as this is surpressing

* rd.break
    * can stop the boot process in the initramfs stage

* systemd.unit=emergency.target
    * loads the system with a very minimal set of units

* systemd.unit=rescue.target
    * loads the sytem with minimal set of units but more than emergency.target

### GRUB boot prompt
* can press e to enter a GRUB configuration screen
* this is essentially or very similar to the GRUB file: /etc/default/grub
* can edit boot parameters by editing on the line beginning with this:
    * linux ($root)/vmlinuz...
    * NOT Persistent just for this boot, will have to edit /etc/default/grub and run grub2-mkconfig to make persistent
* press control + X to start kernel with these parameters


### Rescue disk
Provide a list of options, some useful ones are:
    * Memory Test
    * Boot from Local disk, will try a GRUB on the disk instead of GRUB on external device, in case GRUB is broken
    * start a rescue system

### Rescue system
* loads a read onlyrescue system from the disk
* many time rescue system will recognize your system and mount it at /mnt/sysimage
* will need to use chroot /mnt/sysimage to fix directory references temporarily
    * chroot /mnt/sysimage will temporarily map /mnt/sysimage => / 
    * without this: utilites on the local disk will try to write to files but will be trying to write to the readonly disk 

### Reinstall GRUB with rescue disk
* follow the rescue image steps above to chroot /mnt/sysimage
* grub2-install <device to install i.e. /dev/sda> 

### Rebuild initramfs with rescue disk
* dracut command with no arguments will create an initramfs file system for the currently loaded kernel

### Fixing the initramfs
* symptoms: 
    * never see root drive mounted
    * never see any systemd units starting
* run dracut --force
    * (need force to overwrite the current existing initramfs)


### Recovering from file system issues
* will occur at initramfs section of boot while initramfs is running fsck checks on file system
* will present a message of "Give root password for maintenance"
* enter root password 
* journalctl -xb 
    * shows boot logs
    * look for relevant file system error messages
* type mount -o remount,rw / to make sure the root file system is mounted read/write 
    * analyze what is wrong in the /etc/fstab file and fix it.


### Resetting root password
1. GRUB 2 boot menu-> press e
1. enter rd.break kernel param
    * `linux /boot/vmlinuz-xxxx-generic root=UUID=xxxx ro quiet splash rd.break`
1. this drops into initrams at end of initramfs boot step
1. mount -o remount,rw /sysroot
    * get access to disk operating system
    * remounts root as read writable

1. chroot /sysroot
    * make /sysroot the new root /
    
1. `passwd` command as usual

1. The SELinux context will be messed up now two options:
    1. create file in root directory:   /.autorelabel
        * force SELinux to relable file system
        * note: this is easier but can cause relabeling issue

    1. SELinux context change on /etc/shadow
        * more targetted approach
        * SELinux not started at this step of the boot process
        * load_policy -i to start SELinux
        * manually set the correct context type to /etc/shadow. To do this, type chcon -t shadow_t /etc/shadow
        * reboot




### Get into recovery shell
1. **Reboot the System**:
   - Restart your computer. If it’s a virtual machine, use the reboot option from your virtualization software.

2. **Access the GRUB Menu**:
   - As the system boots, press and hold the `Shift` key (for BIOS systems) or the `Esc` key (for UEFI systems) to bring up the GRUB menu. The exact key can vary depending on your system, so refer to your system's documentation if these don't work.



#### Method 1
1. **Select Recovery Mode**:
   - In the GRUB menu, there should be a recovery mode entry for each kernel. This entry is usually named something like `Advanced options for Ubuntu` or `Recovery mode`.
   - Use the arrow keys to select this entry and press `Enter`.
2. **Access the Recovery Menu**:
   - The system will boot into a recovery menu with several options, including `root`, `fsck`, `network`, etc.
   - Select the `root` option to access a root shell.

#### Method 2
1. **Edit GRUB Boot Options**:
   - Once the GRUB menu appears, use the arrow keys to select the kernel you want to boot.
   - Press `e` to edit the selected boot entry.
2. **Modify the Boot Parameters**:
   - Find the line that starts with `linux` and ends with `ro quiet splash` or similar. This is the line that loads the kernel.
   - Replace `ro` (read-only) with `rw` (read-write) and append `init=/bin/bash` or `init=/bin/sh` at the end of this line. This tells the kernel to start a basic shell instead of the usual initialization process.
     ```
     linux /boot/vmlinuz-xxxx-generic root=UUID=xxxx rw init=/bin/bash
     ```
   - Press `Ctrl + X` or `F10` to boot with these parameters.

* this will mount a shell at the real root filesystem which is usually more complete

### Method 3
1. **Edit GRUB Boot Options**:
   - Once the GRUB menu appears, use the arrow keys to select the kernel you want to boot.
   - Press `e` to edit the selected boot entry.
2. **Modify the Boot Parameters**:
   - Find the line that starts with `linux` and ends with `ro quiet splash` or similar. This is the line that loads the kernel.
   - enter rd.break kernel param
    * `linux /boot/vmlinuz-xxxx-generic root=UUID=xxxx ro quiet splash rd.break`

   - Press `Ctrl + X` or `F10` to boot with these parameters.

* this will mount a shell in initramfs
* useful in case the real root file system needs special functionality to load like encrypted or RAID or something

#### Use the root shell
1. **Access the Root Shell**:
   - The system should boot to a shell prompt as the root user.
   - From here, you can perform necessary maintenance tasks. For example, if you need to change the root password, you can use:
     ```bash
     passwd
     ```
2. **Remount the File System**:
   - If you need to remount the file system to make changes, use:
     ```bash
     mount -o remount,rw /
     ```
3. **Reboot the System**:
   - After making your changes, reboot the system using:

     `exec /sbin/init`  
     or if available:  
     `reboot`
