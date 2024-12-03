### File system

### inodes
* All administrative data about files is stored in inodes
* data block where contents are stored
* contains:
    * creation, access, modified dates
    * permissions
    * file owners
    * how many hard links pointing to the inode
    * Note: Name of file NOT stored in inode, that's stored in directory as a hard link
    * when hard link count reaches 0 the file data is no longer acessible
* Data Structure: Inodes are data structures that store metadata about a file, including its size, ownership, permissions, timestamps, and pointers to the data blocks where the file's actual content is stored.
* Unique Identifiers: Each inode has a unique number within the filesystem, but it does not store the filename or path.
* File Metadata: The inode contains all the metadata needed to access the file's content, except for the file's name.
* Inodes themselves are not stored in a tree structure within a filesystem. Instead, inodes are typically stored in a flat list or array structure. However, the directory entries that reference these inodes are often organized in a hierarchical tree structure. 
* Flat Structure: Inodes are stored in a list-like structure called the inode table. This table is usually part of the filesystem's metadata and is located in a specific area of the disk.
* Indexed by Number: Each inode is referenced by its index in the inode table, which corresponds to its inode number. This method allows quick direct access to an inode's data using its inode number.

### File inodes
* Each regular file has an inode that stores metadata about the file, such as its size, ownership, permissions, and pointers to the data blocks where the file's content is stored.

### Directory inodes
* Each directory is also represented by an inode. 
* The inode for a directory contains metadata similar to that of a file, but instead of pointing to data blocks containing file content, it points to data blocks containing directory entries.
* Directory entries map filenames to inode numbers. This mapping allows the filesystem to locate the inode for a file or subdirectory given its name within the directory.
* Content: The data blocks pointed to by a directory inode contain a list of entries. Each entry includes a filename and its corresponding inode number. These entries can be for regular files, other directories, symbolic links, etc.
* Navigation: When navigating the filesystem, the directory structure (which is essentially a tree of inodes) is traversed by following these entries from one directory to the next.


### Directories 
* Directories: Directories in a filesystem are special types of files that map filenames to inodes. Each entry in a directory contains a filename and a corresponding inode number.
* Path Resolution: When you access a file by its pathname, the filesystem looks up each component of the path in the respective directories, translating it into the corresponding inode number.
* Human-Readable Names: Directories provide the human-readable organization of files, allowing users to navigate and manage files using names and paths
* Linking: A directory entry links a filename to an inode number. Multiple directory entries (hard links) can point to the same inode, allowing a file to have multiple names.
* Separation: The separation of directories and inodes allows the filesystem to efficiently manage files, perform operations like renaming and moving files without altering the file's data or inode.
* File Deletion: When a file is deleted, its directory entry is removed. If no other directory entries (hard links) point to the inode, the inode and its data blocks can be freed.
* Hierarchical Tree: Directories are structured as a hierarchical tree, where each directory file contains entries that map filenames to inode numbers. This tree starts from a root directory (/ in Unix-like systems) and branches out to all other directories and files.
* Path Resolution: When navigating or manipulating files, the filesystem resolves paths by traversing this directory tree, translating human-readable file paths into inode references.
* Traversal for File Operations: For a file operation, the system starts at the root directory and follows the path through the tree of directories, using the entries in each directory to jump from one inode to another until it reaches the target file's inode.
* Inode Access: Once the final inode number is determined from the directory tree traversal, the actual inode is fetched directly from the inode table using its number.


### Example data structures

* directory entry i.e. hard link
```
struct directory_entry {
    char filename[255]; // Maximum filename length
    uint32_t inode_number; // Inode number of the file/directory
};
```


* inode
```
struct inode {
    uint32_t inode_number;         // Inode number
    uint16_t mode;                 // Permissions and file type
    uint16_t uid;                  // User ID of the owner
    uint16_t gid;                  // Group ID of the owner
    uint32_t size;                 // Size in bytes
    uint32_t atime;                // Last access time
    uint32_t mtime;                // Last modification time
    uint32_t ctime;                // Last status change time
    uint32_t block_pointers[12];   // Direct block pointers
    uint32_t single_indirect;      // Single indirect block pointer
    uint32_t double_indirect;      // Double indirect block pointer
    uint32_t triple_indirect;      // Triple indirect block pointer
};
```




## Hard/Soft link
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


## Mounts
* Mounting
    * allows mounting different devices to directories in the file structures
    * the device is formatted in such a way that now the file system can read the contents on the device

* Multi-mount architecture
    * prevents a single mount from filling up all the space blocking space for potentially critically needed files
    * provides added security. 
        * can mount with mount options such as noexec and nodev

* commonly mounted directories
    * /boot, /var(grows in uncontrolled/dynamice way), /home(security reasons), /usr(can mount as read only so no user access) 


## Ram based file system
    * These are generated by the O.S. from kernel info and exist in memory only
    * kernel interface to various hardware or processes
    * Specifically, it provides a filesystem-like view of information and configuration settings that the kernel provides of harware/processes
    * /sys, /proc, /dev
    * these files don't actually exists, they are generated by the O.S. from kernel info and exist in memory only



# File system management

### Configure systems to mount file systems at boot by universally unique ID (UUID) or label:**
   - **UUID and Label:** UUID is a unique identifier assigned to a filesystem, while a label is a human-readable name.
   - **Get UUID and Label:** Use `blkid` or `lsblk -f` to retrieve UUID and label.
     ```bash
     blkid /dev/sdX1
     lsblk -f 
     ```
   - **Edit `/etc/fstab`:** To mount a filesystem at boot, add an entry to `/etc/fstab` using UUID or label or device.
     ```bash
     UUID=1234-5678 /mnt/mydata ext4 defaults 0 2
     # or
     LABEL=mydata /mnt/mydata ext4 defaults 0 2
     # or
     /dev/sdXn /mnt/mountpoint ext4 defaults 0 2
     ```

### Add a file system to a partition or volume
 * `mkfs -t vfat /dev/sdXn`

 ### Mount/Unmount file system manually
 * `mount /dev/sdXn /mnt/mountpoint`
 * `umount /mnt/mountpoint`

 ### Check file systems

* ext4: `e2fsck /dev/sdXn`
* xfs: `xfs_repair /dev/sdXn`

### resize file system
* ext: `resize2fs /dev/sdXn <size>`
    * leave size blank to fill all available space in partition
    * can shrink file system with this as well by putting in a smaller number
* xfs: `xfs_growfs /mnt/mountpoint`
    * note XFS can't be reduced only grown

* AFTER reducing file system need to reduce partitions size.
* BEFORE increasing file system size need to increase partition size.

### Label a file system
* ext4: `e2label /dev/sdXn new_label`
* xfs: `xfs_admin -L new_label /dev/sdXn1`

### mount a file system by label
* use the -L flag
* `sudo mount -L test_lvm_fs /mnt/test`

### List file system info
* `df -h`
* view much info including UUID: `lsblk -f`
* view UUID's: `blkid`