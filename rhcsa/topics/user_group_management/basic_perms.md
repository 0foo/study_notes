
* user accounts
    * /etc/passwd
        * username:password(replaced by /etc/shadow):UID:GID:Comment:Directory:Shell to use when login
    * /etc/shadow
        * login name/username:
        * encrypted password:
        * days since jan 1st 1970 that password was changed:
        * days until allowed to change password:
        * days after which password must be changed
        * days before password expires to warn user
        * days after password expires to disable account
        * days since jan 1 1970 that account is disabled
        * reserved field for future usex
    * /etc/group
        * group name, group password, group id, members
        * note: group password is now stored in /etc/gshadow

* groups
    * here are two types of groups in Linux operating systems Primary group and Secondary (or supplementary) group. Each user can belong to exactly one primary group and zero or more secondary groups.
    * user HAS to be in a primary group
    * primary group is what is group owner when creating files
    * primary group stored in /etc/passwd
    * groups are stored in file /etc/groups
    * secondary group mmberships stored in /etc/groups
        * secondray groups allow access to files i.e. if group has access so does user


* user addition default files
    * /etc/login.defs
        * various login defaults
            * motd file
            * password expiration timeframe
            * indicates the first UID to use when creating users
            * boolean whether to create home directory for user by default CREATE_HOME=yes
            * path variable 

    * /etc/default/useradd
        * default's to use with the useradd command


All files created will get user as owner and user's primary group


            file                    directory
Read        open a file             list contents of directory
Write       change file contents    create/delete files
Execute     run a file              navigate into the directory





* Permissions are set for the user, group, and others. User is the owner of the file or the directory, group is a set of users with identical access defined in `/etc/group`, and others are all other users. The types of permission are read, write, and execute.

* Permission combinations are shown below:
    | Octal Value | Binary Notation | Symbolic Notation | Explanation                           |
    |-------------|-----------------|-------------------|---------------------------------------|
    | 0           | 000             | ---               | No permissions.                       |
    | 1           | 001             | --x               | Execute permission only.              |
    | 2           | 010             | -w-               | Write permission only.                |
    | 3           | 011             | -wx               | Write and execute permissions.        |
    | 4           | 100             | r--               | Read permission only.                 |
    | 5           | 101             | r-x               | Read and execute permissions.         |
    | 6           | 110             | rw-               | Read and write permissions.           |
    | 7           | 111             | rwx               | Read, write, and execute permissions. |

* To grant the owner, group, and others all permissions using the *chmod* command:
    ```shell
    chmod 777 file1
    ```

* chown

* The default permissions are calculated based on the umask. The default umask for root is 0022 and 0002 for regular users (the leading 0 has no significance). The pre-defined initial permissions are 666 for files and 777 for directories. The umask is subtracted from these initial permissions to obtain the default permissions. To change the default umask:
    ```shell
    umask 027
    ```

* Every file and directory has an owner. By default, the creator assumes ownership. The owner's group is assigned to a file or directory. To change the ownership of a file or directory:
    ```shell
    useradd user100
    chown user100 item1
    chgrp user100 item1
    ```

    ```shell
    chown user100:user100 item1
    ```
* Note that the -R option must be used to recursively change all files in a directory.

* `su`
    * A user can switch to another user using the *su* command. The *-i* option ensures that the target users login scripts are run:
        ```shell
        sudo -i -u targetUser
        ``` 
* `sudo`
    * To run a command as root without switching:
        ```shell
        sudo -c
        ``` 
    * The configuration for which users can run which commands using sudo is defined in the `/etc/sudoers` file. The visudo command is used to edit the sudoers file. The sudo command logs successful authentication and command data to `/var/log/secure`.

* `chvt `
    * switches between virtual terminals



* id 
    * get info on a usre

groups
    * get groups of a user

* su 
    * open subshell as different user
    * no user specified will open with root
    * if specifiy a user will open subshell as that user
    * if pass a dash (-) will treat the login as login shell and run all scripts that create the login environment
    * without a dash will not be a login shell

* sudo
    * run specific commands as root
    * allows fine grained permissions for users to perform specific tasks
    * config by /etc/sudoers
    * visudo also edits /etc/sudoers
    * linda ALL=/usr/bin/useradd, /usr/bin/passwd
        * only allows linda to run useradd command as sudo with sudo command


* vipr/vigr
    * add a user
    * can edit /etc/passwd, /etc/group, and /etc/shadow directly
        * if mess up or have a typo in this fill will block all users from logging in
        * vipw will open editor to edit those files also
            * vipw -s opens /etc/shadow
            * vipw -g opens /etc/group (equivqlent to vigr command)
            * vipw (optional -p) open /etc/passwd
            * vipw DOES NOT validate syntax so can mess up system if theres a typo

* passwd
    * -n : minimum usage in days before it can be changd
    * -x : days until pass expires
    * -w : days before expiry to give warning


* chage [options] username
    * -E <yyyy-mm-dd> : account will expire after this date
    * no options chage enters interactive mode
    * chage -l to list the options

* useradd
    * sudo useradd username
    * The command adds an entry to the /etc/passwd, /etc/shadow, /etc/group and /etc/gshadow files.
    * -m : will create a home directory at /home/username by copying /etc/skel files there
    * -d : create home directory in another location specified 
    * -u : pass in a custom UID for the user 
        * By default, when a new user is created, the system assigns the next available UID from the range of user IDs specified in the login.defs file.
    * -g : allows you to create a user with a specific initial login group. You can specify either the group name or the GID number. The group name or GID must already exist.
        * When creating a new user, the default behavior of the useradd command is to create a group with the same name as the username, and same GID as UID.
    * -G : allows adding users to one or more secondary groups separated by comma
    * -s : allows specifying a login shell 
    * -c : add a comment
    * -e : allows creating an expiration date for the user
    * -D : use to view/change useradd defaults 
        * defaults stored in /etc/default/useradd
* passwd 
    * To be able to log in as the newly created user, you need to set the user password. To do that run the passwd command followed by the username:

* usermod
    * -aG : add to a group,.

* user environment (i.e. path)
    * read from files in this order: /etc/profile, /etc/bashrc, ~/.profile, ~/.bashrc

* userdel

* groupadd
    * create groups
    * -g allows to specify a group id 

* groupmod
    * manage group properties
    * change name or ID

* groupmems
    * tells membership of a group, users in group
    *-g: specify the group

newgrp
    * change the primary group of the current logged in user
    * will only last until logout


