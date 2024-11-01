### At start of exam
* setup ssh instead of using VM terminal
* `dnf -y install setroubleshoot policycoreutils-python policycoreutils setroubleshoot-server`
* run `mandb &`


### To remember
* CONFIG FILE
  * after change a config file, do one of these:
  * `RESTART SERVICE`
  * `systemctl daemon-reload`
  * reboot

* DNF REPO
  * Always run `dnf update` after changing dnf repo files!!

* NMCLI:
  * After changing a network connection with nmcli RELOAD 
  * `nmcli connection reload`
  * can also restart network manager 
    * `systemctl restart NetworkManager`
  
* Do not forget to run `systemctl daemon-reload` after editing `/etc/fstab` in recovery mode

* FIREWALLD
  * when editing firewalld rules with `--permanant` flag need to run:  `firewall-cmd --reload`


* VERIFY FSTAB
    * `findmnt --verify /mountpoint`: RUN EVERYTIME!!!
    * `mount /mountpoint` - uses fstab file 
    * `mount -a`

* VERIFY PARTED
    * `parted /filesystem`
    * note: this is useful to make sure you made the right size partition

* verify swap: `swapon` with no param's

* test NFS mounts by mounted with plain `mount -t nfs` command before adding to fstab or auto.master/auto.nfs

* always use .d folders instead of modifying to original config file
  * i.e. yum.repos.d, 




### Misc
* create a file: 
  * allocate space, no writing, faster: `fallocate -l 100M`
  * allocate space and write to file, slower`dd if=/dev/zero of=/swapfile bs=1M count=1024 && chmod 600 /swapfile`
* backslash before command \rm will use an unaliased command
* find out if a command is an alias: type <command>
* Always use visudo to edit the sudoers file
* sudo will not run any alias or function even root as it does not include any env context
* get all aliases with `alias` command
* `file` command to tell which type of file it is
* use `zcat` or `zless` to read zipped files!
* get a date in the future: `date -d "+180 days" +%F`
* math: 
  * `bc`
  * integers: `expr 56276 + 73768` (+,-,/ works but have to escape * in this)
  * doubles: `echo "4.2 * 2" | bc` or just use `bc`/ quit or cntrl+d to exit
* `mkdir -p`  will recursive create directories!
* shortcuts:
  * `cntl+c`: sigint: terminate process
  * `cntr+z`: SIGTSTP: pauses and puts in backgroup 
  * `cntrl+d`:EOF - End of File to interactive session, can typically use instead of typing quit or exit
* dollar sign args:
  * $0(name of script file)
  * $1..., - single arguments passed to function
  * $*, $@ - full argument list passed to function
  * $?, - exit status of last command
  * $$ - proc id of the current shell
* `lsof /some/dir/ectory` : find out what procs are using this directory(delve more into sometime)
* binary vs decimal system
  * Binary system (Mebibyte - MiB, Gibibyte - GiB, etc.):
      * 1 MiB = 1,048,576 bytes
      * 1 GiB = 1,073,741,824 bytes
  * Decimal system (Megabyte - MB, Gigabyte - GB, etc.):
      * 1 MB = 1,000,000 bytes
      * 1 GB = 1,000,000,000 bytes
* run endless process: `sha1sum /dev/zero` or   `yes > /dev/null`
* `ls -d [ei]*`
  * pass -d to not descend into subdirectories when ls encounters a directory
  * should be default!
* `uptime`: system load average
























### Navigating man, less, etc.
* Spacebar Scroll forward (down) one screen
* PageDown Scroll forward (down) one screen
* PageUp Scroll backward (up) one screen
* DownArrow Scroll forward (down) one line
* UpArrow Scroll backward (up) one line
* D Scroll forward (down) one half-screen
* U Scroll backward (up) one half-screen
* /string Search forward (down) for string in the man page
* N Repeat previous search forward (down) in the man page
* Shift+N Repeat previous search backward (up) in the man page
* G Go to start of the man page
* Shift+G Go to end of the man page
* Q Exit man and return to the command shell prompt
