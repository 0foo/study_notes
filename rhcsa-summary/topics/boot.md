### Essentials/Tips
* know how to reset root password
* know how to boot into different targets

### Change kernel parameters temporarily during boot
1. During boot, interrupt the boot process by pressing any key (except enter) to enter the GRUB menu.
2. In the GRUB menu, highlight the kernel you want to boot and press `e` to edit the boot options.
3. Find the line that starts with `linux` or `linux16`, and at the end of that line, add kernel parameter
4. Press `Ctrl + X` to boot with the modified options.

### useful kernel parameters

* `system.target=<sometarget>`
* `rd.break`

### Reset root password
1. add `rd.break` kernel parameter and then boot
2. a shell will appear with the root filesystem mounted as read only at /sysroot
3. `mount -o remount,rw /sysroot`: remount the root file system as read/write
4. `chroot /sysroot`:  make the /sysroot file system the new root of the shell
5. `passwd root`
6. fix SELinux contexts: 
    * `touch /.autorelabel`
    * this is because passwd command recreates the /etc/shadow file
6b. alternative to fix SELinux context
    * Instead of /.autorelabel
    * Can pass in `rd.break enforce=0` as kernel parameters
    * reset root password then exit from the shell which will restart and allow you to login with root password
    * Then run restorecon on the /etc/shadow file 
    * Reboot or run `setenforce=1` command
7. exit twice (once for chroot and another terminal)


### systemd boot targets
* `emergency.target`: mounts a readonly filesystem
* `rescue.target` : for sysinit.target to complete, so that more of the system is initialized, such as the logging service or the file systems.



### Stuck jobs
* `systemctl list-jobs`


