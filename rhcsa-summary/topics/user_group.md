### essentials
* change info
    * useradd/usermod/userdel (can see all the options with help)
    * groupadd/groupmod/groupdel (can see all the options with help)
    * gpasswd: add/remove user from group
    * alternative add/remove user from group
        * usermod -aG groupname username
        * usermod -G <all groups minus one to remove>
    
* view info
    * groups username, to view groups a user is in
    * id username, to view info about a user
    * /etc/passwd to view all users, /etc/groups to view all groups

* change password expiration:
    * existing user
        * `sudo chage -M days username`
        * for all existing users will have to use a for loop
    * can edit /etc/login.defs to change it for any new users, but this will not change any retroactively



### General
* useradd, usermod, userdel, adduser, /etc/passwd
* groupadd, groupmod, groupdel, gpasswd, /etc/group, make a sudo account: usermod -aG wheel <username>
* passwd, chage, /etc/shadow, visudo
* id, whoami, lastlog, su
* getent: literally just cat's /etc/passwd and /etc/group

## user
* `sudo useradd username`
* `sudo useradd -m -c "User Full Name" -s /bin/bash -G groupname -u 1001 username`
* `sudo usermod -c "New Comment" -s /bin/zsh -G newgroupname username`
* `sudo userdel username`
* `sudo userdel -r username`
* `sudo passwd username`

### Group
* `sudo groupadd groupname`
* `sudo groupmod -n newgroupname oldgroupname`
* `sudo groupdel groupname`
* `sudo usermod -aG groupname username`
* `sudo gpasswd -d username groupname`

### Password
* `sudo passwd username`
* `sudo chage -d 0 username`
* `sudo chage -M 30 username`
* `sudo chage -m 7 username`
* `sudo chage -W 7 username`
* `sudo chage -l username`



### Other commands
* `id username`
* `who`
* `lastlog`
* `su - username`
* `whoami`


## commands
* useradd, usermod, userdel
* groupadd, groupmod, groupdel
* passwd, chage
* id, whoami, lastlog, su
