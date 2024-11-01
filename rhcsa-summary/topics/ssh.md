
### server
* /etc/ssh/ssh_config
* permitrootlogin
* authorized_keys


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
* ssh_keygen
* ssh-copy-id
* ssh


* generate ssh key
    * ssh_keygen

* copy your public id to remove server 
    * `ssh-copy-id username@remote_host`
    * as long as the account exist and you enter the correct password this will work

* SSH into a server 
    * `ssh username@server`


* eval $(ssh-agent) && ssh-add
    * if have a passphrase ssh-agent will cache it prevent having to type it numerous times

### Can run a command instead of ssh in
ssh root@192.168.1.1 hostname
some_host.example.com


### SCP
* scp <remote-user>@<host/ip>:/remote/path/to/source /local/path/destination
* scp /loca/path/source <remote-user>@<host/ip>:/remote/path/to/destination


### View logged in users
* `w` will view logged in users

