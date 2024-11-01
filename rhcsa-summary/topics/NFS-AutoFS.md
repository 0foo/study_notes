### NFS/AutoFS
* show all remote mounts for a server. what is flag!?
* mount an nfs share via cli
* mount an remote fs permanantly in fstab
* mount an remote fs permanantly via autofs
* Configure autofs: normal, indirect, direct
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
* in `/etc/auto.master`
    * `/mnt /etc/auto.nfs`

* in `/etc/auto.nfs`
    * `nfs_share nfs-server:/data`


* restart autofs service
* `nfs-server:/data`  will be mounted at `/mnt/nfs_share`


* nfs is the default filesystem, can define another 
* ls or navigate will mount!
* mount point in auto.master must be present
* mount points in auto.nfs DO NOT need to be present



* direct mounts: 
    * manage all mounts in a single file vs declaring a parent mount in auto.master
    * note: all directories in /etc/auto.nfs must be present
    * in `/etc/auto.master`
        * `/- /etc/auto.nfs`
    * in `/etc/auto.nfs`:
```
    /data     nfs-server:/data
    /backup   nfs-server:/backup
```

* wildcard mounts:
    * the `auto.master` is normal
    * the `auto.nfs` doesn't have a directory for a mount point 
    * has asterisk instead
    * will mount any remote directory name locally so don't have to specify
    * `*   -rw,sync   serverb:/shares/&`