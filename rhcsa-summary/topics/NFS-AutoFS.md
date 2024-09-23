### NFS

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
* in /etc/auto.master: `/mnt/nfs /etc/auto.nfs`
* in `/etc/auto.nfs`: `some_directory server:/path/to/nfs/export`
* restart autofs service
* `server:/path/to/nfs`  will be mounted at `/mnt/nfs/some_directory`
* note: if no file system type declared in config files, then nfs is the default
* ls or navigate will mount




