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
* `dnf install autofs`
* in `/etc/auto.master`
    * define mount point and mount config file-> `/mnt /etc/auto.nfs`
* in `/etc/auto.nfs`
    * `nfs    -rw,soft    servername:/exported/share`
    * will mount at /mnt/nfs, (first field in both files)
* `systemctl [reload|restart] autofs`
* can navigate to the folder or ls the folder and it will mount
* note: if no file system type declared in config files, then nfs is the default
