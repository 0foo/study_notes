
* A soft link associates one file with another. If the original file is removed the soft link will point to nothing. To create a soft link to file1:
    ```shell
    ln -s file1 softlink
    ``` 
    softlink:
        * a link to an actual hardlink of the file 
        * can link directories and to locations on other devices
        * does not increment inode counts, so when the file is deleted the soft link quites working



* A hard link associates multiple files to the same inode making them indistinguishable. If the original file is removed, you will still have access to the data through the linked file. To create a soft link to file1:
    ```shell
    ln file1 hardlink
    ``` 
    * hardlinks:
        * are a direct link to the inode
        * increase link count in the inode
        * must exist on SAME device/partition/logical volume
        * cannot create hard links to directories only files
        * when the last name/hard link to file is removed the file data is no longer acccessible, i.e. when hard link count reaches 0



