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

