### rsync
1. `rsync`
    * synchronizes files
    * -r : recursive, entire directory tree
    * -l : also symbolic links
    * -p : preserves symbolic links
    * -n : only a dry run, not actually sync anything
    * -a : use archive mode and ensure that entire subdirectory and file properties are synchronized
    * -A : archive mode (-a) PLUS sync ACLs
    * -X : sync SELinux content as well