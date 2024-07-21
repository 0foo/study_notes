### upgrade kernel

* `yum upgrade kernel` and `yum install kernel`
    * install new kernel alongside old kernel in /boot

* /boot directory
    * keeps the last 4 kernel files installed on system
    * GRUB looks at this and allows selecting

* Step 1: Check the Current Kernel Version
`uname -r`

* Step 2: Update the Repository
`sudo yum update`

* Step 3: Install the New Kernel
`sudo yum install kernel`

* Step 4: Verify the Installation
`rpm -q kernel`

* Step 5: Update the GRUB Configuration
`sudo grub2-mkconfig -o /boot/grub2/grub.cfg`

* Step 6: Reboot the System
`sudo reboot`

* Step 7: Verify the New Kernel
*  After the system reboots, check the kernel version again to ensure that the new kernel is running.
`uname -r`

### Adding new kernel versions
* GRUB 2 picks up new kernels automatically from /boot directory and adds them to the boot menu automatically 
    * nothing has to be added manually



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

### Modify GRUB config
* grub config files are located at /etc/default/grub and at /etc/grub.d/ 
* edit this file and run a grub transpiler
    * `update-grub` (ubuntu)
    * `grub2-mkconfig -o /boot/grub2/grub.cfg` (red hat)
* this creates and populates files in /boot directory
    * If your system is a BIOS system, the name of the file is /boot/grub2/grub.cfg. 
    * On a UEFI system the file is written to /boot/efi/EFI/redhat
    * the command is grub2-mkconfig
    * BIOS system: grub2-mkconfig -o /boot/grub2/grub.cfg
    * UEFI system: grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg


### Install grub to MBR or EFI file system
* `sudo grub-install /dev/sda`
* `sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=grub`
* the generate the config file
    * `sudo grub2-mkconfig -o /boot/grub2/grub.cfg`


### Isolated Target states, i.e. the large scale targets that entire systems change into
* these are isolated targets
    * Isolatable targets contain everything a system needs to boot or change its current state.
    * essentially a complete state for a system
    * targets you can set to get into after a system starts
    * an isolated target starts with all of its dependencies

* contain: `AllowIsolate=yes` in unit file

* use `systemctl isolate` command to switch to a differnt isolated target

* Targets
    * emergency.target
        * only minimal number of units is started, just enough to fix your system 
    * rescue.target
        * start all systems to get a fully functional linux system, but no non-essential unit
    * multi-user.target
        * default target a system starts in
        * starts everything needed for full system functionality
    * graphical.target
        * starts all units needed for fully functional linux system, as well as graphics

    * co-orespond to legacy run levels
        * poweroff.target runlevel 0
        * rescue.target runlevel 1
        * multi-user.target runlevel 3
        * graphical.target runlevel 5
        * reboot.target runlevel 6

### Change targets manually

* To boot a Linux system in a different target (runlevel), you can follow these steps:

1. Check Current Target: 
   `systemctl get-default`

2. List Available Targets: 
   `systemctl list-units --type=target`
    * note: not all of these are able to be isolated

3. Change Target Temporarily:
   You can change the target for the current session without rebooting. This will not persist after a reboot.
   `sudo systemctl isolate <target>`

   For example, to change to the graphical target (equivalent to runlevel 5):
   `sudo systemctl isolate graphical.target`

4. Change Default Target:
   To make the change persistent across reboots, set the default target:
   `sudo systemctl set-default <target>`

   For example, to set the multi-user target (equivalent to runlevel 3):
   `sudo systemctl set-default multi-user.target`

5. Reboot the System:
   If you changed the default target and want to apply it immediately, you can reboot the system:
   `sudo reboot`

* Other notes: 
    * can identify all isolatable targets:
        * `systemctl list-units --type=target`
        *  by grepping service files: `grep -r "AllowIsolate=yes" /usr/lib/systemd/system/*.target`
    * Interesting note: `systemctl isolate reboot.target` reboots computer

### Working with systemd targets
* systemctl --type=target
    * see a list of targets currently active on the computer
* systemctl --type=target --all
    * see all targets available active and inactive
* can grep for grep Isolate *.target in `/usr/lib/systemd/system` to find all the units that allow isolation
* check current target: `systemctl get-default`
* To set the default target to multi-user target: `systemctl set-default multi-user.target`
* Type systemctl get-default to see the current default target 
* use systemctl set-default to set the desired default target



### Swap
1. create a new partition or a new lvm or new file
    * lvcreate
    * parted
    * dd if=/dev/zero of=/swapfile bs=1M count=1024 && chmod 600 /swapfile
2. mkswap
3. swapon/swapoff
* need to add to fstab to make persistent after reboot: /dev/sdX1 none swap sw 0 0
* can remove by swapoff then delete file or partition
* swapon --show (or -s)
* free -h
* important note: for lvm swap may be reported with swapon --show as a mapped drive with the name dm-<something> 
    * can coorelate this to lv's by: `ls -l /dev/mapper`


