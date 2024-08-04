### Init
* setup root password on all boxes

### Network/SSH setup
* delete all the connection from eth1 interface on all the boxes so that eth1 had NO connections attached to it(nmcli)
* configure all the boxes so they can communicate with each other (nmcli)
* change the hostnames on all the boxes
    * box1->vagrant-server
    * box2->vagrant-client1
    * box3->vagrant-client2
* setup ssh so that client1 and client2 can ssh into the server

### Yum
* setup the yum repo in /repo on vagrant-server so that the other machines can access it
* setup the repo file on client1 to use this yum repo to update
* scp this file from client1 to server and scp this file down to client2 
* configure client2 to use this file  

### LVM/partitions/swap
* on vagrant-server configure only one of the unused volumes with gpt partition and add it to a volume group and create an logical volume from this
* create an ext4 file system on this new logical volume
* on vagrant-server configure the other unused drive with gpt partition and add it the same volume group 
* expand logical volume from previous step and expand the file system as well to be the full size of the volume group, which should also be the size of both volumes
* Create a file in this file system just large enough to allow shrinking the LVM and the filesystem by enough to allow removal of the physical volume
* remove the physical volume

---
* create, remove, update swap
    *  create a 500MiB swap partition on /dev/sdb and mount it persistently

### NFS/autofs
* configure vagrant-server to host an nfs folder and create a file in it 
* using the mount command on both machines, mount this to /mnt/nfs and read the file then unmount
* configure /etc/fstab to mount this and mount fstab file via the mount command
* setup autofs to mount this at /mnt/autofs



### one offs
* Set password policies to require a minimum of 8 characters and a maximum age of 60 days
* at/cron
* set a merged tuned profile using the the powersave and virtual-guest profiles
* start one stress-ng process with the niceness value of 19. Adjust the niceness value of the stress process to 10. Kill the stress process.
* Configure NTP synchronization on both servers. Point them to us.pool.ntp.org
* compress/archive stuff 
* symlinks


### important processes
*  Configure persistent journaling on both servers
    * SELinux: ports, files, booleans, etc
* Modify the bootloader with the following parameters:
    * Increase the timeout using GRUB_TIMEOUT=10
    * Add the following line: GRUB_TIMEOUT_STYLE=hidden
    * Add quiet to the end of the GRUB_CMDLINE_LINUX line
* be able to reset root password at boot time





* create, delete, update users, groups, permissions, guid, suid, umask, passwords
* bash scripting
* configure SUDO for users
* grep in files, find files
    * Find all setuid files on server1 and save the list to /root/suid.txt.
    * Find all files larger than 3MB in the /etc directory on server1 and copy them to /largefiles
