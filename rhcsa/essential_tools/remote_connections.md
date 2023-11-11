1. ssh, scp, rsync, sftp


1. Access remote systems using SSH

    * Secure Shell (SSH) provides a secure mechanism for data transmission between source and destination systems over IP networks.
    
    * SSH uses encryption and performs data integrity checks on transmitted data.
    
    * The version of SSH used is defined in `/etc/ssh/sshd_config`.
    
    * The most common authentication methods are Password-Based Authentication and Public/Private Key-Based Authentication.
    
    * The command *ssh-keygen* is used to generate keys and place them in the .ssh directory, and the command *ssh-copy-id* is used to copy the public key file to your account on the remote server.
    
    * TCP Wrappers is a host-based mechanism that is used to limit access to wrappers-aware TCP services on the system by inbound clients. 2 files `/etc/hosts.allow` and `/etc/hosts.deny` are used to control access. The .allow file is referenced before the .deny file. The format of the files is \<name of service process>:\<user@source>.
    
    * All messages related to TCP Wrappers are logged to the `/var/log/secure` file.
    

    * ssh-keygen
        * generate ssh keys
        * add public key to remote server in ~/.ssh/authorized in home directory of user with the private key
            * use ssh-copy-id remote server name
        * add private key to ~/.ssh/someprivatekeyfilename

    * To login using SSH: 
        ```shell
        ssh user@host
        ``` 
    * ssh 
        * -p : can specify port to connect to
        * -l : can specify a username
        * -v : verbose to get info about the connection
        * public key of the server connected to is stored in ~/.ssh/known_hosts
            * every time you connect to that server ssh will check the be sure that key matches

1. scp
    * scp source destination
    * -r : recurisvely copy directory
    * -P : (uppercase) SSH port if not 22
    * to download a file
        * scp root@server:/some/remote/location  ~/some/local/location
    * to upload a file
        * scp ~/some/local/location root@server:~/some/remote/location

1. sftp
    * secure ftp
    * encrypted ftp

1. rsync
    * synchronizes files
    * -r : recursive, entire directory tree
    * -l : also symbolic links
    * -p : preserves symbolic links
    * -n : only a dry run, not actually sync anything
    * -a : use archive mode and ensure that entire subdirectory and file properties are synchronized
    * -A : archive mode (-a) PLUS sync ACLs
    * -X : sync SELinux content as well