* https://www.redhat.com/sysadmin/suid-sgid-sticky-bit


* chmod 
    * apply permissions to a file
    * read:4  write:2 execute:1
    * absolute mode : modifys all permissions
        * chmod 777 /somefile
    * relative mode:
        *   Who - represents identities: u,g,o,a (user, group, other, all)
            What - represents actions: +, -, = (add, remove, set exact)
            Which - represents access levels: r, w, x (read, write, execute)

        * can add or remove permissions on top of what exists
        * (u), (g), (o)
        * operator (+), (-)
        * chmod +x /somefile
            * add execute for ALL
        * chmod g+rw, o-r somefile
            * add read/write for groups, removes read for other
        * can use capital letter to only target directories
            * chmod -R 0+R somefile
    * Special permissions set in front of normal permissions
        * i.e. chmod 2755
        * SUID = 4
        * SGID = 2
        * Sticky = 1

        
* SUID (Set owner User ID up on execution)
    * set SUID: chmod u+s
    * chmod u+s file1.txt 
    * chmod 4750 file1.txt
    * A file with SUID always executes as the user who owns the file, regardless of the user passing the command
    * puts an s where execute should be
    * allows any user to execute that file as the owner
    * ex: /etc/bin/passwd which allows people to set their password 
        * needs to edit files with root access only
        * if run as normal user wouldn't have the root access to edit those files
        * with SUID set and user of root will run this as a root user and all files will be able to be edited
    Use cases:
        *  Where root login is required to execute some commands/programs/scripts.
        * Where you don’t want to give credentials of a particular user, but want to run some programs as the owner.
        * Where you don’t want to use SUDO command, but want to give execute permission for a file/script etc.

* GUID
    * set GUID: chmod g+s
    * If set on a file, it allows the file to be executed as the group that owns the file (similar to SUID)
    * If set on a directory, any files created in the directory will have their group ownership set to that of the directory owner
    * This permission set is noted by a lowercase s where the x would normally indicate execute privileges for the group. 
    * It is also especially useful for directories that are often used in collaborative efforts between members of a group. Any member of the group can access any new file. 
    


* sitcky bit
    * set sticky bit: chmod +t
    * set on a directory
    * Only the owner (and root) of a file can remove the file within that directory
    * Also, owner of the directory can remove files
    * can seee sticky bit as t in ls -l
