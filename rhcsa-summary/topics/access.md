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


* chmod, chattr, chown
* set: guid, suid, sticky bit