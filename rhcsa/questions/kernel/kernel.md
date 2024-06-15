1. What command shows the contents of the kernel ring buffer (KRB)?
2. How can you view kernel log messages using `journalctl`?
3. What does the `-T` option do when used with the `dmesg` command?
4. Which command provides information about the Linux kernel and system?
5. What option with `uname` shows the relevant kernel version?
6. How do you get detailed information about the operating system and kernel using `uname`?
7. Which file contains information about the Red Hat version?
8. What command provides status information about the kernel and operating system?
9. How can you view kernel threads using the `ps` command?
10. What identifies kernel threads in the `ps aux` output?
11. Which commands can be used to upgrade or install a new kernel?
12. Where are kernel files stored on the system?
13. How many kernel files does the /boot directory typically keep?
14. What bootloader looks at the /boot directory to allow kernel selection?
15. Which command lists all currently loaded kernel modules?
16. What command provides detailed information about a specific kernel module?
17. What does the `modinfo` command show about kernel modules?
18. How can you load a kernel module using `modprobe`?
19. Which command is used to unload a kernel module?
20. What are the legacy commands for loading and unloading kernel modules?
21. Why is `modprobe` preferred over `insmod` and `rmmod`?
22. What does `modprobe -r` do?
23. How can you view all hardware devices detected on the PCI bus?
24. What option with `lspci` shows the corresponding kernel modules loaded?
25. What are the general tasks managed by the Linux kernel?
26. Which kernel subsystem is responsible for distributing CPU time among processes?
27. What is the role of the Memory Management Unit (MMU)?
28. What does the Virtual File System (VFS) provide?
29. What is the responsibility of the Networking Unit in the kernel?
30. What does the Inter-Process Communication Unit handle?
31. Which directory serves as an interface to the Linux kernel with human-readable files?
32. What information can you find in the /proc directory?
33. What is the purpose of the /sys directory?
34. How do you mount the sysfs filesystem?
35. What is the /dev directory used for?
36. Which daemon populates the /dev directory?
37. Why did the Linux kernel use to require recompilation for new additions?
38. What is the purpose of kernel modules?
39. Name an example of a kernel module that doesn't interface with hardware.
40. What is the function of device drivers in the kernel?
41. How does the Linux community help with open source drivers?
42. What are the risks associated with closed source drivers?
43. What can a badly performing driver do to the Linux kernel?
44. What is a tainted kernel?
45. Where can you create files to load modules not auto-loaded by the udev system?
46. How can you specify module parameters when loading modules?
47. What information can you get from `modinfo` about module parameters?
48. Give an example of a module parameter you might set in /etc/modprobe.d.
49. What does the `options` keyword do in /etc/modprobe.d?
50. Why is it important to understand kernel modules for the RHCSA exam?



1. `dmesg` or `journalctl -k`
2. `journalctl -k`
3. It shows the time as objective time instead of seconds since kernel start.
4. `uname`
5. `uname -r`
6. `uname -a`
7. `/etc/redhat-release`
8. `hostnamectl status`
9. `ps aux`
10. Kernel threads have square brackets around them `[]`.
11. `yum upgrade kernel` and `yum install kernel`
12. The /boot directory.
13. The last 4 kernel files.
14. GRUB bootloader.
15. `lsmod`
16. `modinfo`
17. Module alias, parameters that can be set while loading the module.
18. `modprobe`
19. `modprobe -r`
20. `insmod` and `rmmod`
21. Because `modprobe` also loads dependencies.
22. It unloads kernel modules and gives an error message if the module is currently in use.
23. `lspci`
24. `lspci -k`
25. Memory management, process management, device drivers, system calls, and security.
26. The Process Scheduler.
27. It manages memory resources and provides separate virtual address spaces for processes.
28. A unified interface to access stored data across different filesystems and physical storage media.
29. Handling network communication.
30. Managing communication between processes.
31. `/proc`
32. Information about CPU, memory, and mounts.
33. It exports kernel information about various kernel subsystems.
34. `mount -t sysfs sysfs /sys`
35. Interface with devices.
36. The `udev` daemon.
37. To add new functionalities or drivers.
38. To add new functionalities without recompiling the kernel.
39. The process scheduler.
40. Mediating between hardware and processes.
41. By fixing bugs and improving the drivers.
42. Bugs and security vulnerabilities that the community cannot fix.
43. It can crash the entire Linux kernel.
44. A kernel containing closed source drivers.
45. `/etc/modules-load.d/` and `/usr/lib/modules-load.d/`
46. By placing configuration files in `/etc/modprobe.d/`
47. Available parameters that can be set for the module.
48. `options cdrom debug=1`
49. It sets options for modules when they are loaded.
50. Understanding kernel modules is crucial for managing and troubleshooting the system effectively.
