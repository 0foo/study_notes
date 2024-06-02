### User logins
* who
    * whoami (show user)
    * Show logged in users

* what
    * w (shorthand)
    * Show logged in users with more detail

* id 
    * get info on a user

* logname
    * Show real username (if using su)

* id
    * Shows a user's UID, username, GUID etc.

* last
    * List all user logins and system reboots

* lastb
    * List all failed login attempts

* lastlog
    * List recent logins





### Permissions

* To grant the owner, group, and others all permissions using the *chmod* command:
    ```shell
    chmod 777 file1
    ```

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


### Permissions on files and directories
* All files created will get user as owner and user's primary group


* Read
  * open a file
  * list contents of directory
* Write
  * change file contents
  * create/delete files
* Execute
  * run a file
  * navigate into the directory





### users

* view all users in the system
    * `cat /etc/passwd | cut -d: -f1`
        * d is delimiter to cut on
        * f is column to output

* create new user 
    * 2 ways:
        * `sudo adduser <newusername>`
            * this handles creation of user directory, creation of password
        * `sudo useradd -m <newusername>`
            * this creates a new user
            * will HAVE to pass -m to create the user directory
            * will have to set a password with `passwd <newusername>` command 


* user accounts
    * /etc/passwd
        * user file
        * username:password(replaced by /etc/shadow):UID:GID:Comment:Directory:Shell to use when login

    * /etc/shadow
        * password file
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


* vipw/vigr
    * basically a vi shortcut 
    * quick link to open/edit /etc/passwd, /etc/group, and /etc/shadow directly
        * if mess up or have a typo in this fill will block all users from logging in

    * vipw will open editor to edit those files also
        * vipw -s opens /etc/shadow
        * vipw -g opens /etc/group (equivqlent to vigr command)
        * vipw (optional -p) open /etc/passwd
        * vipw DOES NOT validate syntax so can mess up system if theres a typo

* passwd
    * used to add/change a users password
    * -n : minimum usage in days before it can be changd
    * -x : days until pass expires
    * -w : days before expiry to give warning


* chage [options] username
    * sets password age setting
    * -E <yyyy-mm-dd> : account will expire after this date
    * no options chage enters interactive mode
    * chage -l to list the info

* useradd
    * sudo useradd username
    * The command adds an entry to the /etc/passwd, /etc/shadow, /etc/group and /etc/gshadow files.
    * -m : will create a home directory at /home/username by copying /etc/skel files there
        * ALWAYS ADD THIS FLAG WHEN CREATING A USER
    * -d : create home directory in another location specified 
    * -u : pass in a custom UID for the user 
        * By default, when a new user is created, the system assigns the next available UID from the range of user IDs specified in the login.defs file.
    * -g : allows you to create a user with a specific initial group. 
        * You can specify either the group name or the GID number. 
        * The group name or GID must already exist.
        * The default behavior of the useradd command is to create a new group with the same name as the username, and same GID as UID.
    * -G : allows adding users to one or more secondary groups separated by comma
    * -s : allows specifying a login shell 
    * -c : add a comment
    * -e : allows creating an expiration date for the user
    * -D : use to view/change useradd defaults 
        * defaults stored in /etc/default/useradd

* passwd 
    * sets a user passwd
    * To be able to log in as the newly created user, you need to set the user password. 
    * To do that run the passwd command followed by the username

* usermod
    * -aG : add to a group,.

* user environment (i.e. path)
    * read from files in this order: /etc/profile, /etc/bashrc, ~/.profile, ~/.bashrc

* userdel
    * This command removes the user's account and related files, such as the user's home directory if you use the -r option (sudo userdel -r username
    * -r deletes a users home directory

* global user addition default files
    * /etc/login.defs
        * various login defaults
            * motd file
            * password expiration timeframe
            * indicates the first UID to use when creating users
            * boolean whether to create home directory for user by default CREATE_HOME=yes
            * path variable 

    * /etc/default/useradd
        * customize global defaults for the useradd command
        * good descrptive comments if you cat the file


### groups
* `groups`
    * get groups of a user

* groups
    * here are two types of groups in Linux operating systems Primary group and Secondary (or supplementary) group. Each user can belong to exactly one primary group and zero or more secondary groups.
    * user HAS to be in a primary group
    * primary group is what is group owner when creating files
    * primary group stored in /etc/passwd
    * groups are stored in file /etc/groups
    * secondary group mmberships stored in /etc/groups
        * secondray groups allow access to files i.e. if group has access so does user

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



### Su/Sudo
* `su`
    * A user can switch to another user using the *su* command. The *-i* option ensures that the target users login scripts are run:
        ```shell
        sudo -i -u targetUser
        ``` 
    * open subshell as different user
    * no user specified will open with root
    * if specifiy a user will open subshell as that user
    * by default is NOT a login shell, must pass `-`, `-l`, or `-i` for login shell
    * can pass either `-l`, `-`, or `-i` to simulate a fresh login
        * will treat the login as login shell and run all scripts that create the login environment
        * It loads the user's login environment by executing the user's login scripts (~/.bash_profile, ~/.profile, etc.).
        * Sets the current working directory to the user's home directory.
        * Resets environment variables to those defined during a fresh login.
        * May change the user's shell to the default shell specified in /etc/passwd.



* `sudo`
    * To run a command as root without switching:
        ```shell
        sudo -c
        ``` 
    * The configuration for which users can run which commands using sudo is defined in the `/etc/sudoers` file. The visudo command is used to edit the sudoers file. The sudo command logs successful authentication and command data to `/var/log/secure`.
    * run specific commands as root
    * allows fine grained permissions for users to perform specific tasks
    * config by /etc/sudoers
    * visudo also edits /etc/sudoers
    * linda ALL=/usr/bin/useradd, /usr/bin/passwd
        * only allows linda to run useradd command as sudo with sudo command




### chown

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




## Exam Objectives:  

### Log in and switch users in multiuser targets 
* **Login Methods**:
  * **Graphical Login**: Usually provided by a display manager like GDM, allowing users to log in through a graphical interface.
  * **Text-based Login**: Accessible via virtual consoles (e.g., Ctrl+Alt+F2 to F6) or through SSH for remote login.

* **Switching Users**:
  * **Using `su` Command**:
    * `su username`: Switches to the specified user.
    * `su - username` or `su -l username`: Simulates a full login, loading the user's environment.
    * `exit`: Returns to the previous user.
  * **Using `sudo` Command**:
    * `sudo command`: Executes a command as another user, typically the root user.
    * `sudo -i`: Starts an interactive root shell.
    * `sudo -u username command`: Executes a command as the specified user.

* **Multi-User Targets**:
  * **Understanding Systemd Targets**:
    * `multi-user.target`: A non-graphical multi-user system state, similar to the traditional runlevel 3.
    * `graphical.target`: A graphical multi-user system state, similar to the traditional runlevel 5.
  * **Switching Targets**:
    * `systemctl isolate multi-user.target`: Switches to a non-graphical multi-user target.
    * `systemctl isolate graphical.target`: Switches to a graphical multi-user target.
    * `systemctl set-default multi-user.target`: Sets the default target to multi-user (non-graphical) for subsequent boots.
    * `systemctl set-default graphical.target`: Sets the default target to graphical for subsequent boots.

* **Managing User Sessions**:
  * **Viewing Logged-in Users**:
    * `who`: Lists currently logged-in users.
    * `w`: Shows who is logged in and what they are doing.
    * `last`: Displays a list of last logged-in users.
  * **Broadcasting Messages**:
    * `wall "message"`: Sends a message to all logged-in users.
    * `write username`: Sends a message to a specific user.

* **Basic User Management**:
  * **Creating and Deleting Users**:
    * `sudo adduser username`: Adds a new user.
    * `sudo userdel username`: Deletes a user.
  * **Adding Users to Groups**:
    * `sudo usermod -aG groupname username`: Adds a user to a specific group.

* **Password Management**:
  * **Changing User Passwords**:
    * `passwd`: Changes your own password.
    * `sudo passwd username`: Changes the password of a specified user.
  * **Password Aging and Policies**:
    * `chage -l username`: Lists password aging information.
    * `sudo chage -M days username`: Sets the maximum number of days before a password change is required.
    * `sudo chage -m days username`: Sets the minimum number of days between password changes.
    * `sudo chage -E YYYY-MM-DD username`: Sets the account expiration date.


### List, set, and change standard ugo/rwx permissions 

* **Listing Permissions**:
  * **Using `ls -l`**:
    * `ls -l filename`: Lists detailed information about a file, including its permissions.
  * **Example**:
    ```bash
    ls -l
    ```
    * Output:
      ```plaintext
      -rw-r--r-- 1 user group 1234 May 19 12:00 example.txt
      ```
    * Interpretation:
      - `-rw-r--r--`: File type and permissions (user: rw-, group: r--, others: r--)
      - `1`: Number of hard links
      - `user`: Owner
      - `group`: Group
      - `1234`: File size in bytes
      - `May 19 12:00`: Last modification date and time
      - `example.txt`: File name

* **Setting and Changing Permissions**:
  * **Using `chmod`**:
    * **Symbolic Mode**:
      * `chmod u+rwx,g+r,o+r filename`: Adds read, write, and execute permissions for the user, read permission for the group, and read permission for others.
      * `chmod u-x filename`: Removes execute permission for the user.
      * `chmod g+w filename`: Adds write permission for the group.
      * `chmod o-r filename`: Removes read permission for others.
    * **Numeric (Octal) Mode**:
      * Permissions are represented by a three-digit octal number, where each digit ranges from 0 to 7:
        * `r = 4`, `w = 2`, `x = 1`
        * Sum the values to get the octal representation.
      * `chmod 755 filename`: Sets permissions to rwxr-xr-x (user: rwx, group: r-x, others: r-x).
      * `chmod 644 filename`: Sets permissions to rw-r--r-- (user: rw-, group: r--, others: r--).

  * **Examples**:
    * Add execute permission for the user:
      ```bash
      chmod u+x filename
      ```
    * Remove write permission for the group:
      ```bash
      chmod g-w filename
      ```
    * Set permissions to rwxr-xr-x (755) using numeric mode:
      ```bash
      chmod 755 filename
      ```

* **Changing Ownership**:
  * **Using `chown`**:
    * `chown user filename`: Changes the owner of the file to `user`.
    * `chown user:group filename`: Changes the owner to `user` and the group to `group`.
  * **Examples**:
    * Change the owner of `example.txt` to `newuser`:
      ```bash
      sudo chown newuser example.txt
      ```
    * Change the owner to `newuser` and the group to `newgroup`:
      ```bash
      sudo chown newuser:newgroup example.txt
      ```

* **Changing Group Ownership**:
  * **Using `chgrp`**:
    * `chgrp group filename`: Changes the group of the file to `group`.
  * **Example**:
    * Change the group of `example.txt` to `newgroup`:
      ```bash
      sudo chgrp newgroup example.txt
      ```

* **Common Permissions**:
  * **Directories**:
    * Read (`r`): Allows listing the directory contents.
    * Write (`w`): Allows creating, deleting, and renaming files within the directory.
    * Execute (`x`): Allows accessing the files and directories within the directory.

  * **Files**:
    * Read (`r`): Allows reading the file.
    * Write (`w`): Allows modifying the file.
    * Execute (`x`): Allows running the file as a program or script.

Understanding these commands and concepts will help you manage file and directory permissions effectively, which is an important part of the RHCSA exam and day-to-day Linux system administration.

