## Commands by topic

### General info
* if a command is aliased can use a forward slash to ignore the alias
    * ie if ls is aliased to ls -la use \ls to use the original command





### History
* `history`: gives command history
    * cntr + r
    * -c clears current history, -w clears ALL history(can also delete ~/.bash_history)
    * located in ~/.bash_history (all commands kept in memory until shell closed then history is written)


### Permissions
* `su`
    * A user can switch to another user using the *su* command. The *-i* option ensures that the target users login scripts are run:
        ```shell
        sudo -i -u targetUser
        ``` 
* `sudo`
    * To run a command as root without switching:
        ```shell
        sudo -c
        ``` 
    * The configuration for which users can run which commands using sudo is defined in the `/etc/sudoers` file. The visudo command is used to edit the sudoers file. The sudo command logs successful authentication and command data to `/var/log/secure`.

* `chvt `
    * switches between virtual terminals

### Power

* Power off
    * `shutdown` [flags] [now | {time format}] [any message string]
        * like poweroff but gracefully shuts off machine
        * -r  will reboot after shutdown
        * allows a delay string
            * time format can be: +20 to shutdown in 20 min or actual time 05:00
        * message string notifys all users on the system
        * sudo shutdown -r +10 "System upgrade"
        * cancel a scheduled shutdown
            * `sudo shutdown -c "Cancelling reboot"`
    * commands:
        * `systemctl reboot`
        * `reboot`
        * `systemctl halt`
        * `halt`
        * `systemctl poweroff`
        * `poweroff`
        * `shutdown -r now`
        * `init 6`
        * `sudo systemctl start reboot.target`
    * `poweroff` talks to power management on the machine to shutoff power, sends ACPI command
    * `halt` shuts down system without powering off, does not shutoff power
    * `echo b > /proc/sysrq-trigger`



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
* dd command
    * The dd tool is super useful for converting and copying data. It reads input from a file or data stream and writes it to a file or data stream. 
    * $ dd if=/home/pete/backup.img of=/dev/sdb bs=1024 
        * if=file - Input file, read from a file instead of standard input
        * of=file - Output file, write to a file instead of standard output
        * bs=bytes - Block size, it reads and writes this many bytes of data at a time. You can use different size metrics by        denoting the size with a k for kilobyte, m for megabyte, etc, so 1024 bytes is 1k
        * count=number - Number of blocks to copy.
* lsusb
    * lists all usb devices
* lspci
    * lists all pci devices
* lsscsi
    * lists all scsi devices


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


### Remote Connections
* `ssh-keygen`
        * generate ssh keys
        * add public key to remote server in ~/.ssh/authorized in home directory of user with the private key
            * use ssh-copy-id remote server name
        * add private key to ~/.ssh/someprivatekeyfilename

* `ssh`
    * To login using SSH: 
        ```shell
        ssh user@host
        ``` 
    * -p : can specify port to connect to
    * -l : can specify a username
    * -v : verbose to get info about the connection
    * public key of the server connected to is stored in ~/.ssh/known_hosts
        * every time you connect to that server ssh will check the be sure that key matches

1. `scp`
    * scp source destination
    * -r : recurisvely copy directory
    * -P : (uppercase) SSH port if not 22
    * to download a file
        * scp root@server:/some/remote/location  ~/some/local/location
    * to upload a file
        * scp ~/some/local/location root@server:~/some/remote/location

1. `sftp`
    * secure ftp
    * encrypted ftp

1. `rsync`
    * synchronizes files
    * -r : recursive, entire directory tree
    * -l : also symbolic links
    * -p : preserves symbolic links
    * -n : only a dry run, not actually sync anything
    * -a : use archive mode and ensure that entire subdirectory and file properties are synchronized
    * -A : archive mode (-a) PLUS sync ACLs
    * -X : sync SELinux content as well


## Documentation

* Locate, read, and use system documentation including man, info, and files in `/usr/share/doc`
    * man command, <command> --help, info/pinfo
        * see command list above
    * /usr/share/docs
        * some services put very useful info here

    * The *man* command can be used to view help for a command. To search for a command based on a keyword the *apropros* command or *man* with the -k option can be used. The *mandb* command is used to build the man database.

    * To search for a command based on a keyword in occurring in its man page:
        ```shell
        man -k <keyword>
        ```

    * The *whatis* command can be used to search for a command in the man database for a short description.

    * The *info* command provides more detailed information than the *man* command. 

    * The `/usr/share/doc` directory contains documentation for all installed packages under sub-directories that match package names followed by their version.


### Text processing

1. `less`
    * press q to quit less
    * search with forward slash: /<keyword>
    * search backwards with questio mark: ?<keyword>
    * cycle search with 'n'
    * 'G' to go to last line of file
    * This same commands as vim and man
    * note: more is similar to less(less is a newer version)

1. `cat`
    * TBI

1. `head` and `tail`
    * default is 10 lines, use -n to custom define line nums
    * can tail -f  for real time following of file updates
    * can view specific line numbers by combining them
        * head -n 11 | tail 1
        * will show line 11 

1. `cut`
    * essentially an explode 
    * -d is the delimiter
    * -f is the field number to extract
    * cut -d : -f 1 /etc/passwd
        * cuts with colon delimiter
        * extracts field number 1 

1. `sort`
    * default is byte order NOT alphabetically
    * -n is numeric order
    * -r is reverse
    * -t:  column separator, i.e. what explodes it
    * -k: column to sort with -t
    * ex: sort -k3  -t: /etc/passwd
        * uses field separator : to sort by 3rd field

1. `wc`
    * counts lines, words, characters etc.
    * in format lines, words, characters
    * 

1. `awk`
    * awk and sed are huge programs dont need to focus too much on them, easy to get lost in them
    * awk is a huge system and whole books written about it
    * how much to know about awk for rhcsa?
    * can pull out 4th field: 
        * awk -F : '{print $4}' /etc/passwd
    * equivalent to:
        * cut -d : -f 4 /etc/passwd
    * awk has better parsing ability than cut sometimes, so if cut no work try awk


1. `sed`
    * awk and aed are huge programs dont need to focus too much on them, easy to get lost in them
    * stream editor
    * can filter files like grep but also allows modification of the files
    * sed -i s/old-text/new-text/g somefile
    * can put quotes around the s/ field
    * delete a line number:
        * sed -i -e '2d' ~/somefile
        * delete line 2

1.  `grep`
    * Use grep and regular expressions to analyse text
    * The grep command is used to find text. For example:
        ```shell
        grep user100 /etc/passwd 
        ```
    * grep: general regular expression parser 
        * -i: not case sensitive
        * -v: invert, lines that do NOT contain the regex
        * -r: recursively search all files/subdir's
        * -e: search for lines matching more than one regex
        * -A, -B: num lines before and after the match to return

    * Always surround regex with quotes or single quotes for escaping purposes
        * grep '^root' /etc/passwd
      
    * Common regular expression parameters are shown below:
        | Symbol | Description                                                        |
        |--------|--------------------------------------------------------------------|
        | ^      | Beginning of a line or word                                        |
        | $      | End of a line or word                                              |
        | \|     | Or                                                                 |
        | .      | Any single character: r.t matches rat rot rut, etc.                                                      |
        | *      | Zero to infinite number of the previous character                                        |
        | ?      | Zero or one  of any of the previous character: cou?ler, matches color and couler, makes previous character optional                                              |
        | []     | Range of characters  [abc] matches a or b or c                                        |
        | \      | Escape character                                                   |
        | ''     | Mask meaning of enclosed special characters                        |
        | ""     | Mask meaning of all enclosed special characters except \, $ and '' |
        |{x}| matches a number of the PREVIOUS character: x{3}, matches xxx|
        |{x,y}| matches a minimum of x and maximum of y: x{1,3} matches 1 to 3 x's|


### Archive, compress, unpack, and decompress files using tar, star, gzip, and bzip2

1. `tar`
    * -v is verbose
    * -f is the archive to target

    * To archive using tar use -c:
        ```shell
        tar cvf myTar.tar /home
        ``` 

    * To add file to archive use -r
        ```shell
        tar rvf myTar.tar /etc/hosts
        ```
    
    * To update the files in archive with newer version use -u
        ```shell
            tar rvf myTar.tar /home
        ```
    * View contents of tar file with -t
        ```shell
            tar -tvf myTar.tar
        ```

    * To unpack using tar:
        ```shell
        tar xvf myTar.tar
        ``` 
            * note can use -C to unpack to a target location
            * can unpack a single file by passing in a filename
                * tar xvf myTar.tar /somefile


    * To compress using tar and gzip:
        ```shell
        tar cvfz myTar.tar /home
        ``` 

    * To compress using tar and bzip2:
        ```shell
        tar cvfj myTar.tar /home
        ``` 

    * To decompress using tar and gzip:
        ```shell
        tar xvfz myTar.tar /home
        ``` 

    * To decompress using tar and bzip2:
        ```shell
        tar xvfj myTar.tar /home
        ``` 

    * The star command is an enhanced version of tar. It also supports SELinux security contexts and extended file attributes. The options are like tar.


1. `gzip`, `bzip2`, `gunzip`, `bunzip2`
        * can use flags with `tar -z(gzip) -j(bzip2)`


### File management
1. wildcards
    * star(*) used for 1 or more characthers
        * ls * would show all files in current directory (except hidden with dot would need -a)
    * ? used for a single character
        * ls c*t  would match any character 
    * brackets [] used for one character amongst these
        * ls c[ua]t  would match cat and cut

1. Directories
    * mkdir, cd, pwd, rmdir, cp, rm, rm -rf, ls, ln, ln -s
    * absolute vs relative paths

1. cp
    * cp -R : recursively copies everything 
    * cp -a : archive mode copies all permissions and everything exactly the same
    * tip: add a slash after copy to not create the new folder and get error message
        * cp /etc/hosts /tmp/ vs cp /etc/hosts /tmp



1. Create and edit text files

    * To create an empty file:
        ```shell
        touch file
        cat > newfile
        ``` 

    * To create a file using vim:
        ```shell
        vi file
        ``` 


1. Create, delete, copy, and move files and directories

    * To create a directory:
        ```shell
        mkdir directory
        ``` 

    * To move a file or directory:
        ```shell
        mv item1 item2
        ```     

    * To copy a file or directory:
        ```shell
        cp item1 item2
        ```     

    * To remove a file:
        ```shell
        rm file1
        ```

    * To remove an empty directory:
        ```shell
        rmdir directory
        ```

    * To remove a non-empty directory:
        ```shell
        rm -r directory
        ```


### Permissions
1. List, set, and change standard ugo/rwx permissions

    * Permissions are set for the user, group, and others. User is the owner of the file or the directory, group is a set of users with identical access defined in `/etc/group`, and others are all other users. The types of permission are read, write, and execute.
    
    * Permission combinations are shown below:
        | Octal Value | Binary Notation | Symbolic Notation | Explanation                           |
        |-------------|-----------------|-------------------|---------------------------------------|
        | 0           | 000             | ---               | No permissions.                       |
        | 1           | 001             | --x               | Execute permission only.              |
        | 2           | 010             | -w-               | Write permission only.                |
        | 3           | 011             | -wx               | Write and execute permissions.        |
        | 4           | 100             | r--               | Read permission only.                 |
        | 5           | 101             | r-x               | Read and execute permissions.         |
        | 6           | 110             | rw-               | Read and write permissions.           |
        | 7           | 111             | rwx               | Read, write, and execute permissions. |

    * To grant the owner, group, and others all permissions using the *chmod* command:
        ```shell
        chmod 777 file1
        ```

    * The default permissions are calculated based on the umask. The default umask for root is 0022 and 0002 for regular users (the leading 0 has no significance). The pre-defined initial permissions are 666 for files and 777 for directories. The umask is subtracted from these initial permissions to obtain the default permissions. To change the default umask:
        ```shell
        umask 027
        ```

    * Every file and directory has an owner. By default, the creator assumes ownership. The owner's group is assigned to a file or directory. To change the ownership of a file or directory:
        ```shell
        useradd user100
        chown user100 item1
        chgrp user100 item1
        ```
    
        ```shell
        chown user100:user100 item1
        ```
    * Note that the -R option must be used to recursively change all files in a directory.


### Hard/Soft link 

1. soft link
    ```shell
    ln -s file1 softlink
    ``` 

1. hard link
    ```shell
    ln file1 hardlink
    ``` 


### Mounts
* Commands for managing mounts
    * View mounts
        * /proc/mounts directory
            * contains mount data
        * mount
            * overview of all mounted devices
            * same data as /proc/mount
            * also shows kernel interfaces
        * df -Th
            * size info about mounts
        * findmnt
            * tree structure showing relationship between mounts
            * findmnt -A 
    * mount 


### Kernel data gathering
* dmesg the same as: journalctl -dmesg the same as: journalctl -k
    * shows contents of the kernel ring buffer (KRB)
    * KRB is where kernel keeps log messages
    * note: pass -T to dmesg in order to see time as objective time vs seconds since kernel start
* uname
    * info about the linux kernel
    * -r, relevant kernel version
    * -a, much info about operating system
    * info about cpu
* cat /etc/redhat-relesae
    * info about the redhat version
* hostnamectl status
    * another place to get info on kernal and O.S. version
* view kernel threads with: `ps aux`
    * kernel threads have square brackets around them []


### upgrade kernel

* `yum upgrade kernel` and `yum install kernel`
    * install new kernel alongside old kernel in /boot

* /boot directory
    * keeps the last 4 kernel files installed on system
    * GRUB looks at this and allows selecting


### Kernel Module management


* lsmod
    * lists all currently loaded kernel modules

* modinfo
    * to find out more about a specific kernal module
    * module alias is another name that can be used to address the module
    * params: parameters that can be set while loading the module

* modprobe/modprobe -r
    * load/unload modules
    * insmod and rmmod are legacy way to load modules
        * does not also load dependencies
    * modprobe -r will give error message if trying to unload a module that's currently in use

* lspci 
    * shows all hardware devices that have been detected on the pci bus
    * pass -k to show co-oresponding kernel modules loaded to match the hardware device



### write to logfile from bash
    * can use logger command to write to rsyslogd from bash or script
    * logger <message>
    * sends message to /var/messages
    * add -p for an error priority 
    * logger writes to /dev/log which is a socket via udp 
        * journald is listening on that socket
        * journald records then forwards the message to rsyslog
    * https://unix.stackexchange.com/questions/464361/examining-dev-log
    * https://serverfault.com/questions/959982/is-rsyslog-redundant-on-when-using-journald


### journalctl
    * reports starting from oldest to newest
    * -f : latest 10 messages
    * -r : view in newest to oldest
    * G will go to end
    * / and ? work to search
    * --no-pager : shows output without a pager i.e. like a cat
    
### view boot logs
* journalctl -xb
    * shows boot logs