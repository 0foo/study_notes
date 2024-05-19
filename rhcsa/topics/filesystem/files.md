1. Directories
    * mkdir, cd, pwd, rmdir, cp, rm, rm -rf, ls, ln, ln -s
    * absolute vs relative paths

1. cp
    * cp -R : recursively copies everything 
    * cp -a : archive mode copies all permissions and everything exactly the same
    * tip: add a slash after copy to not create the new folder and get error message
        * cp /etc/hosts /tmp/ vs cp /etc/hosts /tmp

1. file <filename>
    * identifies what type of file it is

1. Create and edit text files

    * To create an empty file:
        ```shell
        touch file
        cat > newfile
        ``` 

    * To create a file using vim:
        ```shell
        vi file
        ``` 
        
1. Create, delete, copy, and move files and directories

    * To create a directory:
        ```shell
        mkdir directory
        ``` 

    * To move a file or directory:
        ```shell
        mv item1 item2
        ```     

    * To copy a file or directory:
        ```shell
        cp item1 item2
        ```     

    * To remove a file:
        ```shell
        rm file1
        ```

    * To remove an empty directory:
        ```shell
        rmdir directory
        ```

    * To remove a non-empty directory:
        ```shell
        rm -r directory
        ```


### File Attributes
* chattr
    * A set : The atime record is not updated.
    * S set : The changes are updated synchronously on the disk.
    * a set : File can only be opened in append mode for writing.
    * i set : File cannot be modified (immutable), the only superuser can unset the attribute.
    * j set : All of files information is updated to the ext3 journal before being updated to the file itself.
    * t set : No tail-merging is allowed.
    * d set : No more candidate for backup when the dump process is run.
    * u set : When such a file is deleted, its data is saved enabling the user to ask for its undeletion.

* lsattr -l
    * list attributes


### Hard/Soft link 

1. soft link
    ```shell
    ln -s file1 softlink
    ``` 

1. hard link
    ```shell
    ln file1 hardlink
    ``` 

### directory navigation

* ls
    * -h (human readable)
    * -a (show hidden)
    * -l (detailed)
    * -lt (newest file first)
    * -ltr (oldest file first)
    * -R (current dir plus all subdirs recursively)
    * -d (just shows names of directories)
    * List of files and directories

* pwd
    * Print working directory

* cd
    * ~ (home)
    * / (root)
    * - (switch)
    * .. (parent)
    * Change directories
    * - (last directory)
