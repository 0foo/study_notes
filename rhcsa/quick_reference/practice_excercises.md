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

### LVM/partitions/swap/labels
* on vagrant-server configure only one of the unused volumes with gpt partition and add it to a volume group and create an logical volume from this
* create an ext4 file system on this new logical volume
* on vagrant-server configure the other unused drive with gpt partition and add it the same volume group 
* expand logical volume from previous step and expand the file system as well to be the full size of the volume group, which should also be the size of both volumes
* Create a file in this file system just large enough to allow shrinking the LVM and the filesystem by enough to allow removal of the physical volume
* remove the physical volume
* create a 500MiB swap partition on this unused physical volume, confirm it's active,  lable the drive as somethings, and mount it persistently with that label

### NFS/autofs
* configure vagrant-server to host an nfs folder and create a file in it 
* using the mount command on both machines, mount this to /mnt/nfs and read the file then unmount
* configure /etc/fstab to mount this and mount fstab file via the mount command
* setup autofs to also mount this at /mnt/autofs

### one offs
* at/cron
    * Create a job using at to write "This task was easy!" to /coolfiles/at_job.txt in 10 minutes.
    * Create a job using cron to write "Wow! I'm going to pass this test!" every Tuesday at 3pm to /var/log/messages.
* set a merged tuned profile using the the powersave and virtual-guest profiles
* start one stress-ng process with the niceness value of 19. Adjust the niceness value of the stress process to 10. Kill the stress process.
* Configure NTP synchronization on both servers. Point them to us.pool.ntp.org
* compress/archive stuff 
    * On server1 create a tar w/gzip archive of /etc called etc_archive.tar.gz in the /archives directory.
* symlinks
    *  On server1 create a folder called /links, and under links create a file called file01. Create a soft link called file02 pointing to file01, and a hard link called file03 pointing to file01. Check your work.

### important processes
* Configure persistent journaling on both servers
* Modify the bootloader with the following parameters:
    * Increase the timeout using GRUB_TIMEOUT=10
    * Add the following line: GRUB_TIMEOUT_STYLE=hidden
    * Add quiet to the end of the GRUB_CMDLINE_LINUX line
* be able to reset root password at boot time via grub menu

### searching/find/grep
* grep in files, find files
* Find all setuid files on server1 and save the list to /root/suid.txt.
* Find all files larger than 3MB in the /etc directory on server1 and copy them to /largefiles

### Bash scripting
* Write a script named awesome.sh in the root directory on server1.
    * If “me” is given as an argument, then the script should output “Yes, I’m awesome.”
    * If “them” is given as an argument, then the script should output “Okay, they are awesome.”
    * If the argument is empty or anything else is given, the script should output “Usage ./awesome.sh me|them”

### SELinux: ports, files, booleans,
* Put SELinux on server2 in permissive mode then back into enforcing mode both via cli and via config file
* Assign SELinux context to a folder both permanantly and temporarily
* Install httpd(if not already) and create a symlink in /var/www/html to a folder outside of the httpd directory structure and allow httpd to get documents from a specific folder not in /var/www folder

### Containers
* On server1, as the user cindy, create an httpd container image with the tag web_image.
* From the newly created image, deploy a container as a service with the container name cindy_web. The web config files should map to ~/web_files, and the local port of 8000 should be mapped to the container's port 80. Create a default page that says "Welcome to Cindy's Web Server!". The service should be enabled and the website should be accessible.

### user/permissions
* Configure both servers to create files with 660 permissions by default.
* Set password policies to require a minimum of 8 characters and a maximum age of 60 days
* configure SUDO for users
* Write a script to create groups according to these specs:
```
dba_admin:5010
dba_managers:5011
dba_staff:5012
dba_intern:5013
it_staff:5014
it_managers:5015
```
* Write shell scripts on server1 that create users according to the following parameters. Ensure all users except cindy use autofs for their profiles
* 
```
manny:1010:dba_admin,dba_managers,dba_staff
moe:1011:dba_admin,dba_staff
jack:1012:dba_intern,dba_staff
marcia:1013:it_staff,it_managers
jan:1014:dba_admin,dba_staff
cindy:1015:dba_intern,dba_staff
```
* Set the password on all of the newly created users to dbapass
* Create sudo command alias for MESSAGES with the command /bin/tail -f /var/log/messages
* Enable superuser privileges according to the following:
```
dba_managers: everything
dba_admin: SOFTWARE, SERVICES, PROCESSES
dba_intern: MESSAGES
```
*  Switch to the various users using su and test their privileges.





---TBI
* create, delete, update users, groups, permissions, guid, suid, umask, passwords


### Answers might be in one of these
* https://github.com/aggressiveHiker/rhcsa9/blob/main/exam_prep/solutions_ordered_task_list.md

### More questions: Round 2
* https://github.com/chlebik/rhcsa-practice-questions/blob/master/questions