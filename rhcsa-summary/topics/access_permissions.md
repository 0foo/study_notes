### Essentials/Tips
* New files never get execute
permission.
* FACLs: a whole fucking thing


### Basic file perm's
* `sudo chown user:group filename`
* `sudo chmod 755 filename`
* `sudo chmod -R 755 directory`
* `umask 022`
* `chmod u+rwx,g+rx,o+r filename`
* `chmod u-s,g-s,o-s directory`


### Permissions meanings
* file:
    * read-can read file
    * write-can write to file
    * execute-can execute file
* dir
    * read-can list contents
        * note: if read only directory, will only be able to see file names and NOT permissions or anything else
    * write-means nothing
    * write + execute-can create files in the dir
    * execute-can navigate to the dir

* 4-read
* 2-write
* 1-execute

### Special permissions
* `sudo chmod +t directory`
* `sudo chmod u+s filename`
* `sudo chmod g+s directory`
* chmod, chattr, chown
* set: guid, suid, sticky bit



### umask EXAM OBJECTIVE
* files default = 666
* directory default = 777
* note: umask of 000 on files means: rw-rw-rw- (666)
    * NO EXECUTE!!
* subtract umask from this
* note: cannot set files to execute with umask!!! (only manually)
    * WILL ROUND DOWN (i.e. umask of 055 is 044 for files)
* execute on directory mean can navigate to them
* put in /etc/profile and reboot to make permanant



### Set guid: EXAM OBJECTIVE
* anyone who creates new files/directories will create them with the group of the directory instead of their default user group
1. Create a directory: `mkdir /path/to/directory`
2. Change group ownership to a specific group: `chown root:groupname /path/to/directory`
3. Set the set-GID bit on the directory: `chmod g+s /path/to/directory`
4. Verify that the set-GID bit is set (look for 's' in the group permissions): `ls -ld /path/to/directory`


### Configure SUDO EXAM OBJECTIVE
* always use visudo to edit
* format of file entries:
    * `<user> <hosts>=(<runas>) <tag>: <commands>`
* `vagrant ALL=(ALL) ALL`
    * can run all commans from all hosts as all users
* `vagrant ALL=(ALL) ls,pwd`
    * can only run ls and pwd as any user including root
* `sudo -u anotheruser command`
    * run commands as another user
* `vagrant ALL=(ALL) NOPASSWD: ALL`
    * add nopasswd tag to not require entering a password


### ACL

* Essentials
    * setfacl -m 
    * setfacl -x
    * getfacl
    * use X
    * ACL mask
    * default, user, group, owner, other




* ls -l (+) means there's ACL's
* FACL overwrite standard permissions
* Mask settings show the maximum permissions possible for all users and groups
    * does not restrict the permissions of the file owner or other users
* getfacl shows an effective comment beside entries that are restricted by a mask setting.
* delete ALL facls: `setfacl -b file`
* use capital X for execute permissions insteaad of lower X
    * This is how the capital "X" behaves—it gives execute permission to directories and only to files that already had execute permission.
    * lower case x will make ALL FILES EXECUTABLE

```
# file: .
# owner: user
# group: operators
# flags: -s-
user::rwx
user:consultant3:---
user:1005:rwx
group::rwx
group:consultant1:r-x
group:2210:rwx
mask::rwx
other::---
default:user::rwx
default:user:consultant3:---
default:group::rwx
default:group:consultant1:r-x
default:mask::rwx
default:other::---
```
* default: are directory only and specifiy what permissions happen when a new file or directory is created inside
* Mask settings show the maximum permissions possible for all users and groups


* `ls -l`
    * if have a plus after it means ACL's are configured
    
* View
    * `getfacl filename`
* Set/Remove
    * `setfacl -m u:username:rw- filename`
    * `setfacl -m g:groupname:r-- filename`
    * `setfacl -m o::--- filename`
    * `setfacl -m m::rwx filename`
    * `setfacl -x u:username filename`
    * `setfacl -b filename`
    * `setfacl -R -m u:username:rwx directory`
* Default
    * `setfacl -d -m u:username:rwx directory`
    * `setfacl -d -m g:groupname:rx directory`
* Examples
    * `setfacl -m u:alice:rw- example.txt`
    * `setfacl -m g:developers:r-- project`
    * `setfacl -x u:alice example.txt`
    * `setfacl -d -m u:alice:rwx /shared`
    * `setfacl -R -m g:developers:rx /project`
    * `setfacl -b example.txt`
    * `setfacl -m m::rwx example.txt`



