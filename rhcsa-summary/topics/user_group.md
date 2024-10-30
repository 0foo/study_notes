### essentials
* change info
    * useradd/usermod/userdel (can see all the options with help)
    * groupadd/groupmod/groupdel (can see all the options with help)
    * gpasswd: add/remove user from group
    * alternative add/remove user from group
        * usermod -aG groupname username
        * usermod -G <all groups minus one to remove>

* view info
    * `id username`, to view user id and groups/group ids that a user is in
    * /etc/passwd to view all users, /etc/groups to view all groups
    * can use `groups` command if need an iterable for the groups a user is in
    
* change password expiration:
    * existing user
        * `sudo chage -M days username`
        * `date -d "+180 days" +%F`
        * for all existing users will have to use a for loop
    * can edit /etc/login.defs to change it for any new users, but this will not change any retroactively

* force passwd change on first login: `chage -d 0 dbuser1`
* set minimum password age: `chage -m 10 dbuser1`
* set maximum password age: `chage -M 10 dbuser1`

* change accounts
    * use su
    * to switch to root use either: `sudo -i` or `su -`
        * sudo -i uses your passwords and su - uses the root password
    * when use a - with su will run all logins scripts just like the user had logged in them selves (login shell)
    * without - will maintain all the variables and login shell of current user just with new privileges of su user

* When a user is removed with userdel without the -r option specified, the system, will have files that are owned by an unassigned UID.

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
