1. ssh, scp, rsync, sftp


1. Access remote systems using SSH

    * Secure Shell (SSH) provides a secure mechanism for data transmission between source and destination systems over IP networks.
    
    * SSH uses encryption and performs data integrity checks on transmitted data.
    
    * The version of SSH used is defined in `/etc/ssh/sshd_config`.
    
    * The most common authentication methods are Password-Based Authentication and Public/Private Key-Based Authentication.
    
    * The command *ssh-keygen* is used to generate keys and place them in the .ssh directory, and the command *ssh-copy-id* is used to copy the public key file to your account on the remote server.
    
    * TCP Wrappers is a host-based mechanism that is used to limit access to wrappers-aware TCP services on the system by inbound clients. 2 files `/etc/hosts.allow` and `/etc/hosts.deny` are used to control access. The .allow file is referenced before the .deny file. The format of the files is \<name of service process>:\<user@source>.
    
    * All messages related to TCP Wrappers are logged to the `/var/log/secure` file.
    
