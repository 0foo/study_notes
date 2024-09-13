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

### Basic file perm's
* `sudo chown user:group filename`
* `sudo chmod 755 filename`
* `sudo chmod -R 755 directory`
* `umask 022`
* `chmod u+rwx,g+rx,o+r filename`
* `chmod u-s,g-s,o-s directory`

### Special permissions
* `sudo chmod +t directory`
* `sudo chmod u+s filename`
* `sudo chmod g+s directory`

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
* chown, chmod, umask
* id, whoami, lastlog, su
