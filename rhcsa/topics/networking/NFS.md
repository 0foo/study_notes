
### NFS

* hosting NFS on a server
    * uses `/etc/exports` as it's config file
        * configure a folder to share with the format:
            * directory host(options)
        * example:
            * `/srv/nfsdir 192.168.1.0/24(rw,sync,no_root_squash)`

        * options
            rw: Read and write access.
            ro: Read-only access.
            sync: Requires changes to be written to disk before responding to the client for data integrity. 
            async: Allows the server to reply to requests before changes are written to disk. Faster but less safe.
            no_root_squash: Disables root squashing. See below.
            root_squash: (Default) Maps requests from UID/GID 0 (root) to the anonymous UID/GID (usually nobody).
            all_squash: Maps all UIDs and GIDs to the anonymous user.
            subtree_check: Verifies if the file being requested is in the exported subtree. Enabled by default but can cause performance issues.
            no_subtree_check: Disables subtree checking, improving performance.
    
        * root squashing:
            * root on the client is mapped to an anonymous user (usually nobody) for security. 
            * no_root_squash keeps the root UID and GID, giving root access to the NFS share.

        * can use `exportfs` command to modify NFS share
* File level security
    * authentication is expected to be managed with a different service like LDAP/Kerberos
    * NFS is built on top of RPC authentication. With NFS version 3, the most common authentication mechanism is AUTH_UNIX. The user id and group id of the client system are sent in each RPC call, and the permissions these IDs have on the file being accessed are checked on the server. 
    * For this to work, the UID and GIDs must be the same on the server and the clients. 
    * However, you can force all access to occur as a single user and group by combining the all_squash, anonuid, and anongid export options. * * all_squash will map all UIDs and GIDs to the anonymous user, and anonuid and anongid set the UID and GID of the anonymous user. 
    * For example, if your UID and GID on your dev server are both 1001, you could export your home directory with a line like
    * `/home/darren       192.168.1.1/24(rw,all_squash,anonuid=1001,anongid=1001)`

* mounting NFS share on a client for short term use
    * `sudo mount -t nfs 192.168.1.100:/srv/nfsdir /mnt`
    * use the -t flag with nfs parameter for type in order to mount NFS shares

* viewing available shares on NFS server from client
    * showmount -e <some nfsserver ip/dns>
    * NOTE: showmount relies on the portmapper service for share discovery
        * firewalld nfs service opens port 2049 only: 
            * only for mapping 
            * does not allow portmapper traffic for showmount share discovery
        * for share discovery mountd and rpc-bind services need to be added to the firewall as well.

* NFS versioning
    * `mount -t nfs -o nfsvers=4.1 host:/remote/export /local/directory`
    * current version of NFS (as of writing this) is NFS4
    * fallback to previous versions 
        * if trying to connect to a server that only offers an older NFS version:
        * `mount -o nfsvers=<some version>`
        * This can prove useful if you are connecting to a server or a device that offers NFS 3 only.

* mount NFS server process:
    * showmount -e some.nfsserver.ip_or_dns.com
    * mount some.nfsserver.ip_or_dns.com:/ /mnt
    * use mount command and `ls /mnt` to verify success