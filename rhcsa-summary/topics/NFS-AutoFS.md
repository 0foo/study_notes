### NFS/AutoFS
* show all remote mounts for a server
* mount an nfs share via cli
* mount an remote fs permanantly in fstab
* mount an remote fs permanantly via autofs
* Configure autofs(chatgpt what is needed for this: this is from exam objective)
* Mount and unmount network file systems using NFS




### Essentials/Tips
* `showmount -e <remote nfs server>`
* `mount -t nfs ....`
* `man nfs` for fstab examples
* /etc/auto.master: `base_mount_point base_mount_file`
* in `/etc/auto.nfs`: `some_directory server:/path/to/nfs/export`
* restart autofs service



* host an nfs share
```
sudo yum install nfs-utils -y   # For RHEL/CentOS
sudo mkdir -p /srv/nfs/shared
sudo chown nobody:nogroup /srv/nfs/shared   # Adjust as needed for your security requirements
sudo chmod 755 /srv/nfs/shared
sudo nano /etc/exports (if not present, create)
/srv/nfs/shared 192.168.1.0/24(rw,sync,no_subtree_check)
sudo exportfs -r   (or exportfs -a ??)
sudo systemctl start nfs-server
sudo systemctl enable nfs-server
firewall-cmd --add-service=mountd --add-service=rpc-bind --add-service=mountd --zone=public --permanent
sudo firewall-cmd --reload
verify: showmount -e localhost
verify: exportfs 
```

* access NFS share
    * `showmount -e <remote nfs server>`
    * `sudo mount -t nfs servername:/exported/share /mnt/nfs`
    * in `/etc/fstab`
        * `servername:/exported/share /mnt/nfs nfs defaults 0 0`

### autofs
* /etc/auto.master: `base_mount_point base_mount_file`
    * /etc/auto.master: `/mnt/nfs /etc/auto.nfs`
* in `/etc/auto.nfs`: `some_directory server:/path/to/nfs/export`
* restart autofs service
* `server:/path/to/nfs`  will be mounted at `/mnt/nfs/some_directory`
* note: if no file system type declared in config files, then nfs is the default
* ls or navigate will mount
* mount point in auto.master must be present 
* mount points in auto.nfs DO NOT need to be present

* direct mounts: manage all mounts in a single file with direct map: `/- /etc/auto.nfs`
    * note: all directories in /etc/auto.nfs must be present

* wildcard mounts: will mount the remote directory name locally so don't have to specify
    * `*   -rw,sync   serverb:/shares/&`