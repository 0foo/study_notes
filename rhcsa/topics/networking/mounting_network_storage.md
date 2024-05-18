### Mount command

* mounting NFS share on a client for short term use
    * `sudo mount -t nfs 192.168.1.100:/srv/nfsdir /mnt`
    * use the -t flag with nfs parameter for type in order to mount NFS shares

* mount CIFS/SAMBA share
    * `mount -t cifs -o user=guest //192.168.4.200/data /mnt`
    * -t is for type
        * not required mount is smart enough to identify the type of share
    * this is for a read only guest
    * To specify the Samba username you want to use, you can add the -o username=someone
        * will ask for password when you mount




### fstab
* /etc/fstab
* mounts when server restarts and keeps the mount permanantly
* remote file system format in fstab
        * Use a colon after the name of the server to identify the mount as an NFS share.
        * Use two forward slashes in remote server to identify a CIFS/Samba
* NFS mount example:
    * `server1:/share /nfs/mount/point nfs sync 0 0` 
        * first col: server:/share name
        * second col: local location to mount
        * third col: mount type
        * fourth col: mount option
            * sync ensure changed files are written to remote server immediately 
            * ensures changes are not placed in write buffers (needing flushing )first 
        * fifth col: backup via `dump` utility is activated
        * sixth col: indicates if should run a `fsck` on the file system BY THE CLIENT at boot to ensure integrity

* CIFS mount example:
    * `//server2/sambashare /sambamount cifs guest,uid=myuser,iocharset=utf8,rw 0 0`
    * challenges with SMB are the authorization/creds 
        * can specify username= and password= mount options in the fstab file but DONT
    



### automount
* automount is alternative to /etc/fstab file
* the share is mounted ON DEMAND not at boot
* ensures only file systems that are needed are mounted
* uses autofs to mount files NOT mount
    * autofs operates in userspace and subsequently no permissions are required
* ensure automount is running:  `systemctl enable --now autofs`

* mount an automount share is two step process:
    1. /etc/auto.master
        * parent root folder for autofs
        * inside this file are mappings of a root directory to some target file
        * `/somedir /etc/somefile --timeout 60`

    1. in /etc/somefile
        * mapping of subdirectory options remote_url:/share
        * `files -rw server2:/nfsdata`
        * this mounts remote: server2:/nfsdata to local mount point: /somedir/files


    1. access the share
        * if you try to access this mount with `ls` it will show not existing
        * mount will not show it existing as well
        * if you try to `cd` to the share autofs will mount the directory and it should now be present in `ls` and `cd`

* automount wildcard
    * can use wildcards with automount, for example, to mount a user directory when they login
    * note: not sure if on the exam, flesh out if needed/experiment with when have time


