* chattr +s somefile
* chattre -s somefile

* lsattr


* may need to enable in /etc/fstab with the user_xattrib mount option



* A: doesn't modify file access time
    * normally everytime a file is opened it's access time is modified
    * this disables it
* a: allows file to be added but not removed
* c: makes sure file is compressed first time compression engine becomes active
* D: makes sure files are written to disk and not cached first
* d: makes sure file is not backed up in backups where the 'dump' utility is used
* I: enables indexing for the directory it's applied, faster access for older file systems without b-tree access
* i: makes file immutable, no changes can be made
* j: makes sure that on ext3, the file is writted to journal first then the data blocks written to disk
* s: overwrites the blocks where the file data was stored with 00000 zeros after the file is deleted
* u: saves undelete information, works with undelete utilities

