
### server
* host ssh sessions
    * ensure sshd service is running and firewall is open 

* enable root login
```
sudo nano /etc/ssh/sshd_config
PermitRootLogin yes
sudo systemctl restart sshd
```
* can add a users public key to their account manually
   * add key to authorized_hosts on the USERS ACCOUNT .ssh folder
* `echo "your-public-key" >> /home/username/.ssh/authorized_keys` 

### user

* generate ssh key
    * ssh_keygen

* copy your public id to remove server 
    * `ssh-copy-id username@remote_host`
    * as long as the account exist and you enter the correct password this will work

* SSH into a server 
    * `ssh username@server`

