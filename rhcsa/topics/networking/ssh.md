### SSH

1. Access remote systems using SSH

    * Secure Shell (SSH) provides a secure mechanism for data transmission between source and destination systems over IP networks.
    
    * SSH uses encryption and performs data integrity checks on transmitted data.
    
    * The version of SSH used is defined in `/etc/ssh/sshd_config`.
    
    * The most common authentication methods are Password-Based Authentication and Public/Private Key-Based Authentication.
    
    * The command *ssh-keygen* is used to generate keys and place them in the .ssh directory, and the command *ssh-copy-id* is used to copy the public key file to your account on the remote server.
    
    * TCP Wrappers is a host-based mechanism that is used to limit access to wrappers-aware TCP services on the system by inbound clients. 2 files `/etc/hosts.allow` and `/etc/hosts.deny` are used to control access. The .allow file is referenced before the .deny file. The format of the files is \<name of service process>:\<user@source>.
    
    * All messages related to TCP Wrappers are logged to the `/var/log/secure` file.
    


### Hardening SSH server


* Disable root login
    * SSH servers by default have root login enabled
    * modify the PermitRootLogin parameter in /etc/ssh/sshd_config and reload or restart the service.
* Disable password login
* Configure a nondefault port for SSH to listen on
    * /etc/ssh/sshd_config change port line
    * Active sessions will not be disconnected after restarting the SSH server (unless you fail to restart the SSH server successfully).
    * Network ports are labeled with SELinux security labels to prevent services from accessing ports where they should not go.
    * To allow a service to connect to a nondefault port, you need to use semanage port to change the label on the target port.
    * Before doing so, it is a good idea to check whether the port already has a label. You can do this by using the semanage port -l command.
    * If the port does not have a security label set yet, use -a to add a label to the port. If a security label has been set already, use -m to modify the current security label.
* Allow specific users only to log in on SSH
    * in /etc/ssh/sshd_config file
    * AllowUsers. This option takes a space-separated list of all users that will be allowed login through SSH.


### Cache SSH passphrase
1. Type ssh-agent /bin/bash to start the agent for the current (Bash) shell.
2. Type ssh-add to add the passphrase for the current user’s private key. The key is now cached.
3. Connect to the remote server. Notice that there is no longer a need to enter the passphrase.
* This procedure needs to be repeated for all new sessions that are created.


* `ssh-keygen`
        * generate ssh keys
        * add public key to remote server in ~/.ssh/authorized in home directory of user with the private key
            * use ssh-copy-id remote server name
        * add private key to ~/.ssh/someprivatekeyfilename

* `ssh`
    * To login using SSH: 
        ```shell
        ssh user@host
        ``` 
    * -p : can specify port to connect to
    * -l : can specify a username
    * -v : verbose to get info about the connection
    * public key of the server connected to is stored in ~/.ssh/known_hosts
        * every time you connect to that server ssh will check the be sure that key matches


1. `scp`
    * scp source destination
    * -r : recurisvely copy directory
    * -P : (uppercase) SSH port if not 22
    * to download a file
        * scp root@server:/some/remote/location  ~/some/local/location
    * to upload a file
        * scp ~/some/local/location root@server:~/some/remote/location


## Exam Topics

###   Access remote systems using SSH 

* **Connecting to a Remote System**:
  * **Basic SSH Command**:
    * `ssh username@hostname`: Connects to the remote system specified by `hostname` using the SSH protocol with `username`.
    * Example:
      ```bash
      ssh user@example.com
      ```
  * **Specifying a Port**:
    * Use the `-p` option followed by the port number to connect to a non-standard SSH port.
    * Example:
      ```bash
      ssh -p 2222 user@example.com
      ```

* **Authentication**:
  * **Password Authentication**:
    * Enter the password when prompted after executing the SSH command.
    * Example:
      ```bash
      ssh user@example.com
      Password: [enter your password]
      ```
  * **Public Key Authentication**:
    * Preconfigure SSH keys for passwordless authentication:
      1. Generate SSH keys on your local machine using `ssh-keygen`.
      2. Append your public key (`~/.ssh/id_rsa.pub`) to the remote system's `~/.ssh/authorized_keys` file.
    * Example:
      ```bash
      ssh-copy-id -i ~/.ssh/id_rsa.pub user@example.com
      ```

* **Executing Commands Remotely**:
  * **Running Commands**:
    * Execute a command directly on the remote system using SSH without interactive shell:
      ```bash
      ssh user@example.com "ls -l /var/log"
      ```
  * **Interactive Session**:
    * Start an interactive session on the remote system:
      ```bash
      ssh user@example.com
      ```

* **File Transfer with SCP**:
  * **Copying Files**:
    * Use `scp` (secure copy) to transfer files between local and remote systems:
      ```bash
      scp /path/to/local/file user@example.com:/path/to/remote/location/
      ```
    * Example:
      ```bash
      scp example.txt user@example.com:/home/user/
      ```

* **Advanced SSH Configurations**:
  * **SSH Configuration File**:
    * Customize SSH behavior using the `~/.ssh/config` file:
      ```plaintext
      Host example
          HostName example.com
          User user
          Port 2222
          IdentityFile ~/.ssh/id_rsa
      ```
    * Connect using:
      ```bash
      ssh example
      ```

* **Security Considerations**:
  * **Disable Root Login**:
    * Set `PermitRootLogin no` in `/etc/ssh/sshd_config` to prevent root from logging in directly.
  * **Firewall Rules**:
    * Ensure that SSH port (default: 22) is open and accessible through firewall rules.

* **Troubleshooting**:
  * **Verbose Mode**:
    * Use `-v` option to troubleshoot connection issues:
      ```bash
      ssh -v user@example.com
      ```
  * **Check Logs**:
    * Review SSH logs on both local and remote systems (`/var/log/auth.log` on Ubuntu, `/var/log/secure` on CentOS/RHEL).

