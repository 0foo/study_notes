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