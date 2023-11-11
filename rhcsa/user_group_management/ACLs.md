* with basic perms cant give permissions to more than one user or group on a file


* Some utilities may not support ACL's
    * create backup of facls with: getfacl
    * restore backup with: setfacl



* To enable ACL on the file system 
    * need to add the acl mount option to /etc/fstab
    * this allows the file system to be mounted with ACL support



* setfacl
    * set ACLs 
    * setfacl -m g:sales:rx /dir
        * set read/execute on the directory for the group sales
        * -m is modify
    * setfacl -m u:linda:rwx /data
        * sets linda to have rwx access on /data folder
    * setfacl can be subractive: use minus sign (-) to remove access
        * setfacl -m u:anna:- /dir
        * removes anna from acl list of dir
        * also overrwites permissions obtained from the 'others' entity
    * use -R to set recursively


* getfacl
    * get current ACLs
    * getfacl /dir

* Note: ls -la does not show ANY ACL's
    * shows a + indicating that ACL's exist





### Default ACLs
* pass the d option to setfacl when adding acl to a directory
* will apply this access to all new files/dir's created in this directory
* note: this is not retroactive, i.e. existing files will not inherit this ACL setting
    * will have to change existing files manually
* ex: setfacl -m d:g:sales:rx /somedir


### Default systemwide permissions setting
* called the umask
* this is default permissions when creating any file/dir
* can use umask -S to view in more user friendly way
* umask if 4 digits, the first is special bit the other 3 are u/g/o
* The first digit of the umask represents a special bit (sticky bit, SGID bit, or SUID bit). 
    * If the first digit is set to 0, the special bit is not set. 
* can view and set with umask command
* will need to add this command to /etc/profile or to the user profile to make it permanant

* Umask values are in the form owner/group/others
    Octal value : Permission
    0 : read, write and execute
    1 : read and write
    2 : read and execute
    3 : read only
    4 : write and execute
    5 : write only
    6 : execute only
    7 : no permissions

    

* To determine the umask value you want to set, subtract the value of the permissions you want from 666 (for a file) or 777 (for a directory)
* umask of 002
    * 666 - 002 = 664 = rw,rw, r
    * 777 - 002 = 775 = rwx,rwx, rx

* a good security measure is to set root umask to 027 or something more secure, which differes from normal user or 022 or 002