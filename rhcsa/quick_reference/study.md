* configure all the boxes so they can communicate with each other (nmcli)
* change the hostnames on all the boxes
    * box1->vagrant-server
    * box2->vagrant-client1
    * box3->vagrant-client2
* setup ssh so that client1 and client2 can ssh into the server
* setup the yum repo in /repo on vagrant-server so that the other machines can access it
* setup the repo file on client1 to use this yum repo to update
* scp this file from client1 to server and scp this file down to client2 
* configure client2 to use this file  

### NFS
* configure vagrant-server to host an nfs folder and create a 


### LVM
* on vagrant-server configure /dev/sdb with gpt partition and add it to a volume group and create an logical volume from this
* create an ext4 file system on this new logical volume
* on vagrant-server configure /dev/sdc with gpt partition and add it the same volume group 
* expand logical volume from previous step and expand the file system as well
* Create a file in this 



* create, delete, update users, groups, permissions, guid, suid, umask, passwords
* symlinks
*  Configure persistent journaling on both servers
    * SELinux: ports, files, booleans, etc
* create,remove, update, expand/reduce: pg, vg, lv, partitions, file system
* create, remove, update swap
    *  create a 500MiB swap partition on /dev/sdb and mount it persistently
* setup ssh on host and client
* configure network interfaces and hostnames
* configure yum repos on host and client
* setup NFS on host and client/setup autofs
* Set password policies to require a minimum of 8 characters and a maximum age of 60 days
* configure SUDO for users
* compress/archive stuff 
* grep in files, find files
    * Find all setuid files on server1 and save the list to /root/suid.txt.
    * Find all files larger than 3MB in the /etc directory on server1 and copy them to /largefiles
* at/cron
* Modify the bootloader with the following parameters:
    * Increase the timeout using GRUB_TIMEOUT=10
    * Add the following line: GRUB_TIMEOUT_STYLE=hidden
    * Add quiet to the end of the GRUB_CMDLINE_LINUX line
* set a merged tuned profile using the the powersave and virtual-guest profiles
* start one stress-ng process with the niceness value of 19. Adjust the niceness value of the stress process to 10. Kill the stress process.


TBI:

* Configure NTP synchronization on both servers. Point them to us.pool.ntp.org