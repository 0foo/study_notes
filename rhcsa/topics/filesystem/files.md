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
* softlink:
    * A soft link associates one file with another. 
    * If the original file is removed the soft link will point to nothing.
    * a link to an actual hardlink of the file 
    * can link directories and to locations on other devices
    * does not increment inode counts, so when the file is deleted the soft link quites working


* hard link
    * same think as a directory entry
    * are a direct link to the inode
    * increase link count in the inode
    * must exist on SAME device/partition/logical volume
    * cannot create hard links to directories only files
    * when the last name/hard link to file is removed the file data is no longer acccessible, i.e. when hard link count reaches 0
    * A hard link associates multiple files to the same inode making them indistinguishable. If the original file is removed, you will still have access to the data through the linked file. To create a soft link to file1:
    *  Since hard links share the same inode, they have the same metadata (permissions, timestamps, etc.) and point to the same data blocks on the disk.
    * note: inode has no idea which files are pointing to it so have to use find command.
    * can view inode id number with ls -i, then can use find with -inum flag to find all hardlinks


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



## Exam Objectives


### Create and edit text files

* **Using `vi`/`vim`**:
  * **Open/Create a File**:
    * `vi filename`: Opens an existing file or creates a new one if it doesn't exist.
  * **Insert Mode**:
    * Press `i` to enter insert mode for editing.
  * **Save and Exit**:
    * Press `Esc` to exit insert mode, then type `:wq` and press `Enter` to save and exit.
  * **Exit Without Saving**:
    * Press `Esc`, then type `:q!` and press `Enter`.

* **Using `nano`**:
  * **Open/Create a File**:
    * `nano filename`: Opens an existing file or creates a new one if it doesn't exist.
  * **Editing**:
    * Directly start typing to edit the file.
  * **Save and Exit**:
    * Press `Ctrl+O` to save the file, then `Ctrl+X` to exit.
  * **Exit Without Saving**:
    * Press `Ctrl+X`, then press `N` when prompted to save changes.

* **Using `echo` and Redirection**:
  * **Create a File with Content**:
    * `echo "Hello, World!" > filename`: Creates a file with the specified content.
  * **Append Content to a File**:
    * `echo "Additional line" >> filename`: Appends content to an existing file.

* **Using `cat` for Quick Edits**:
  * **Create/Overwrite a File**:
    * `cat > filename`: Type the content and press `Ctrl+D` to save and exit.
  * **Append to a File**:
    * `cat >> filename`: Type the content and press `Ctrl+D` to append and exit.

* **Using `touch` to Create an Empty File**:
  * **Create an Empty File**:
    * `touch filename`: Creates an empty file or updates the timestamp if it exists.


### Create, delete, copy, and move files and directories

* **Creating Files**:
  * **Using `touch`**:
    * `touch filename`: Creates an empty file or updates the timestamp if the file exists.
  * **Using `echo`**:
    * `echo "content" > filename`: Creates a file with the specified content.
  * **Using `cat`**:
    * `cat > filename`: Creates a file and allows you to type content, press `Ctrl+D` to save and exit.

* **Creating Directories**:
  * **Using `mkdir`**:
    * `mkdir dirname`: Creates a new directory.
    * `mkdir -p parentdir/childdir`: Creates nested directories (if parentdir doesn't exist, it will be created).

* **Deleting Files**:
  * **Using `rm`**:
    * `rm filename`: Deletes a file.
    * `rm -f filename`: Forcefully deletes a file without prompting for confirmation.

* **Deleting Directories**:
  * **Using `rmdir`**:
    * `rmdir dirname`: Deletes an empty directory.
  * **Using `rm`**:
    * `rm -r dirname`: Deletes a directory and its contents recursively.
    * `rm -rf dirname`: Forcefully deletes a directory and its contents recursively without prompting.

* **Copying Files**:
  * **Using `cp`**:
    * `cp sourcefile destfile`: Copies a file to a new location.
    * `cp -r sourcedir destdir`: Copies a directory and its contents recursively.

* **Moving/Renaming Files**:
  * **Using `mv`**:
    * `mv sourcefile destfile`: Moves or renames a file.
    * `mv sourcedir destdir`: Moves or renames a directory.

* **Examples**:
  * **Create an empty file named `example.txt`**:
    * `touch example.txt`
  * **Create a directory named `mydir`**:
    * `mkdir mydir`
  * **Copy `example.txt` to `example_backup.txt`**:
    * `cp example.txt example_backup.txt`
  * **Move `example.txt` to `mydir`**:
    * `mv example.txt mydir/`
  * **Delete the file `example_backup.txt`**:
    * `rm example_backup.txt`
  * **Delete the directory `mydir` and its contents**:
    * `rm -r mydir`


### Create hard and soft links

* **Creating Hard Links**:
  * **Using `ln`**:
    * `ln sourcefile linkname`: Creates a hard link named `linkname` pointing to `sourcefile`.

  * **Examples**:
    * Create a hard link named `hardlink.txt` pointing to `original.txt`:
      ```bash
      ln original.txt hardlink.txt
      ```

* **Creating Soft (Symbolic) Links**:
  * **Using `ln -s`**:
    * `ln -s sourcefile linkname`: Creates a symbolic (soft) link named `linkname` pointing to `sourcefile`.

  * **Examples**:
    * Create a symbolic link named `softlink.txt` pointing to `original.txt`:
      ```bash
      ln -s original.txt softlink.txt
      ```

* **Key Differences**:
  * **Hard Links**:
    * Refer to the same inode as the original file, meaning they point directly to the data on the disk.
    * Cannot span different filesystems (partitions).
    * When the original file is deleted, the hard link still retains the data.
    * Syntax: `ln sourcefile hardlinkname`.

  * **Soft (Symbolic) Links**:
    * Refer to the path of the original file rather than the inode.
    * Can span different filesystems.
    * If the original file is deleted, the symbolic link becomes a dangling (broken) link.
    * Syntax: `ln -s sourcefile softlinkname`.

* **Viewing Links**:
  * **Using `ls -l`**:
    * Hard links appear with the same inode number as the original file.
    * Symbolic links show the link name and the path it points to.
    * Example output:
      ```bash
      ls -l
      ```
      ```plaintext
      -rw-r--r-- 2 user user  0 Jan  1 12:00 original.txt
      -rw-r--r-- 2 user user  0 Jan  1 12:00 hardlink.txt
      lrwxrwxrwx 1 user user 12 Jan  1 12:00 softlink.txt -> original.txt
      ```

* **Removing Links**:
  * **Using `rm`**:
    * `rm linkname`: Removes both hard and soft links without affecting the original file.

  * **Examples**:
    * Remove a hard link or symbolic link:
      ```bash
      rm hardlink.txt
      rm softlink.txt
      ```
