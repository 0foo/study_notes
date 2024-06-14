1. /bin : 
    * Essential command binaries that need to be available in single-user mode; for all users, e.g., cat, ls, cp. 
    * Contains binary executables.
    * Common linux commands you need to use in single-user modes are located under this directory.
    * Commands used by all the users of the system are located here e.g. ps, ls, ping, grep, cp 

1. /lib:
    * Libraries essential for the binaries in /bin/ and /sbin/.
    * Library filenames are either ld* or lib*.so.*
    * Example: ld-2.11.1.so, libncurses.so.5.7

1. /sbin : 
    * Essential system binaries, e.g., fsck, init, route.
    * Just like /bin, /sbin also contains binary executables.
    * The linux commands located under this directory are used typically by system administrators, for system maintenance purposes.
    * Example: iptables, reboot, fdisk, ifconfig, swapon

1. /usr : 
    * Secondary hierarchy for read-only user data; contains the majority of (multi-)user utilities and applications. 
    * Contains binaries, libraries, documentation, and source-code for second level programs.
    * /usr/bin contains binary files for user programs. If you can’t find a user binary under /bin, look under /usr/bin. 
        * For example: at, awk, cc, less, scp
    * /usr/sbin contains binary files for system administrators. If you can’t find a system binary under /sbin, look under /usr/sbin. 
        * For example: atd, cron, sshd, useradd, userdel
    * /usr/lib contains libraries for /usr/bin and /usr/sbin
    * /usr/local contains user’s programs that you install from source. 
        * For example, when you install apache from source, it goes under /usr/local/apache2
    * /usr/src holds the Linux kernel sources, header-files and documentation. 

1. /opt : 
    * Optional application software packages.
    * Contains add-on applications from individual vendors.
    * Add-on applications should be installed under either /opt/ or /opt/ sub-directory.


1. /dev directory
    * Full of device files/nodes for devices attached to the system
    * Device files/nodes are abstractions of standard devices that applications interact with via I/O system calls.
    * Userspace applications can use these device nodes to interface with the systems hardware, 
        * For example, the X server will "listen to" /dev/input/mice so that it can relate the user's mouse movements to moving the visual mouse pointer. 
     * Note: some hardware interfaces not in /dev, typically for legacy reasons and the code is too involved to change now
        * network interfaces not in /dev
            * these were historically considered not amenable to file style communication
                * can't use simple read() write() calls to communicate like most file style hardware devices
                * networking communicates in packets vs bytes and has connections/streams which come and go frequently
                * connections require more than simple file name passed to read()
            * network applications are more complex than file accessing applications
            * network sockets are files though but in different location
                * see below
        * video
            * x-server writes to video adaptor memory directly
            * if communicated with kernel system calls each time need to change video memory would be too slow 
        * https://unix.stackexchange.com/questions/23199/why-are-network-interfaces-not-in-dev-like-other-devices
        * https://askubuntu.com/questions/306594/why-do-ethernet-devices-not-show-up-in-dev
    * /dev directory is populated by udev daemon
    * /dev/random vs /dev/urandom
        * prefer /dev/urandom
        * /dev/random has been deprecated for a decade
        * /dev/random can block if it runs out of entropy and halt process execution
        * provides random series of bytes
        * generate a random number with $RANDOM 
        * deprecation: https://lkml.org/lkml/2017/7/20/993
    * /dev/null
    * /dev/tty, /dev/console
        * tty is the virtual console i.e. if ssh'd in
        * https://unix.stackexchange.com/questions/60641/linux-difference-between-dev-console-dev-tty-and-dev-tty0



1. /sys directory
    * Primarily provides access to kernel data structures related to devices, drivers, and other kernel subsystems.
    * /sys is an interface to kernel data structures, while /dev provides access to actual hardware devices via device files
    * contains all the information for all devices on your system, such as the manufacturer and model, where the device is plugged in, the state of the device, the hierarchy of devices and more. 
    * The files you see here aren't device nodes, so you don't really interact directlywith devices from the /sys directory, you interact with the kernel structures of those devices
    * Enables users and applications to configure and manage device settings.
    * Often used for monitoring kernel events and system status. 
    * kernel docs here:
        * https://www.kernel.org/doc/Documentation/filesystems/sysfs.txt



1. /proc:
    * Virtual filesystem providing process and kernel information as files.
    * Contains files and directories that represent running processes and other system information.
    * Allows inspection of kernel parameters, system memory, CPU usage, network connections, and loaded modules. 
    * In Linux, it corresponds to a procs mount. Generally, automatically generated and populated by the system, on the fly.
    * Contains information about system process.
    * This is a pseudo filesystem that contains information about running processes. 
        * For example: /proc/{pid} directory contains information about the process with that particular pid.
    * This is a virtual filesystem with text information about system resources. 
        * For example: /proc/uptime
    * /proc/meminfo
    * contains all info about memory
    * /proc/cpuinfo
        * contains all info about cpu


1.  /home :
      * Users’ home directories, containing saved files, personal settings, etc.
      * Home directories for all users to store their personal files.
      * example: /home/kishlay, /home/kv
1.  /root
      * the home directory of root user



1. /media:
    * Mount points for removable media such as CD-ROMs (appeared in FHS-2.3).
    * Temporary mount directory for removable devices.
    * Examples, /media/cdrom for CD-ROM; /media/floppy for floppy drives; /media/cdrecorder for CD writer

1. /mnt :
    * Temporarily mounted filesystems.
    * Temporary mount directory where sysadmins can mount filesystems.




1. /etc :
    * Host-specific system-wide configuration files.
    * Contains configuration files required by all programs.
    * This also contains startup and shutdown shell scripts used to start/stop individual programs.
    * Example: /etc/resolv.conf, /etc/logrotate.conf.
    * /etc/profile
    * /etc/bashrc
    * /etc/motd
        * message after login
    * /etc/issues:
        * message before login, good for specifying login issues or security concerns
    * /etc/passwd, /etc/shadow, /etc/group, /etc/gshadow, /etc/skel
        * user management
    * /etc/*release
        * redhat: /etc/redhat-release
        * ubuntu: /etc/lsb-release
    * /etc/services
        * a nice list of well known ports for different services
        
1. /boot :
    * Boot loader files, e.g., kernels, initrd. 
    * Kernel initrd, vmlinux, grub files are located under /boot
    * Example: initrd.img-2.6.32-24-generic, vmlinuz-2.6.32-24-generic
1. /var
    * files that change in size dynamically
    * For example: log files, mail boxes, spool files
    * /var/log/secure

1. /tmp : 
    * Temporary files. Often not preserved between system reboots and may be severely size restricted.
    * Directory that contains temporary files created by system and users.
    * Files under this directory are deleted when the system is rebooted.

1. /run
    * process and user specific info since last boot
    * temp file system i.e. memory based and wiped every re-start
    * /run is the "early bird" equivalent to /var/run, in that it's meant for system daemons that start very early on (e.g. systemd and udev) to store temporary runtime files like PID files and communication socket endpoints, while /var/run would be used by late-starting daemons (e.g. sshd and Apache).

    * Traditional /var/run was an actual directory on disk, which meant the underlying filesystem may not have been mounted at the point systemd et al needed to write stuff into it. Making /run a tmpfs (i.e. RAM-based) filesystem neatly solved this problem and eliminated the need to clean it up on the next boot.

    * Of course, having two runtime scratch directories struck many as being a bit much, so in many modern Linux distros, /var/run is just a symlink to /run.

1. /srv
    * Site-specific data served by this system, such as data and scripts for web servers, data offered by FTP servers, and repositories for version control systems.
    * srv stands for service.
    * Contains server specific services related data.
    * Example, /srv/cvs contains CVS related data.








