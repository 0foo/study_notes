## Network Storage

### NFS

* authentication is expected to be managed with a different service like LDAP/Kerberos

* NFS versioning
    * current version of NFS (as of writing this) is NFS4
    * fallback to previous versions 
        * if trying to connect to a server that only offers an older NFS version:
        * mount option nfsvers=
        * This can prove useful if you are connecting to a server or a device that offers NFS 3 only.

* viewing available shares
    * showmount -e <some nfsserver ip/dns>
    * NOTE: showmount relies on the portmapper service for share discovery
        * firewalld nfs service opens port 2049 only: 
            * only for mapping 
            * does not allow portmapper traffic for showmount share discovery
        * for share discovery mountd and rpc-bind services need to be added to the firewall as well.

* mount NFS server
    * showmount -e some.nfsserver.ip_or_dns.com
    * mount some.nfsserver.ip_or_dns.com:/ /mnt
    * use mount command and `ls /mnt` to verify success


### CIFS
* evolved from Samba which is Microsoft server message block
* SMB used to be a microsoft propriety sharing protocal but was opened up 
* The Samba project formed to use it to allow sharing across operating systems
* Samba became the de facto standard for sharing files between different operating systems
* At some point transitioned from Samba to CIFS: Common Internet File System
    * the de facto interoperable sharing protocol between operating systems


* smbclient
    * linux tool for working with CIFS/SAMBA
    * smbclient -L <servername>
        * list available shares
        * note even though asks for a password can just hit enter to browse anonymously
        * this will be a read only guest

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
    * server1:/share /nfs/mount/point nfs sync 0 0 
        * first col: server and share name
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
        * maps a mount point to a secondary configuration file
        * /nfsdata/mount/point /etc/auto.nfsdata
    1. in /etc/auto.nfsdata
        * files -rw server2:/nfsdata
        * files keyword, mount options, server and share name
    1. access the share
        * if you try to access this mount with `ls` it will show not existing
        * mount will not show it existing as well
        * if you try to `cd` to the share autofs will mount the directory and it should now be present in `ls` and `cd`

* automount wildcard
    * can use wildcards with automount, for example, to mount a user directory when they login
    * note: not sure if on the exam, flesh out if needed/experiment with when have time



### FTP
* uses: vsftpd package
* see ./FTP.pdf in this directory