* Compress files with gzip
    * `gzip filename`
    * `gunzip filename.gz`
* Compress files with bzip2
    * `bzip2 filename`
    * `bunzip2 filename.bz2`
* Compress files with xz
    * `xz filename`
    * `unxz filename.xz`
* Create a tar archive, j is bzip, z is gzip
    * `tar -cvf archive.tar /path/to/directory`
    * `tar -xvf archive.tar`
    * `tar -czvf archive.tar.gz /path/to/directory`
    * `tar -xzvf archive.tar.gz`
    * `tar -cjvf archive.tar.bz2 /path/to/directory`
    * `tar -xjvf archive.tar.bz2`
    * `tar -cJvf archive.tar.xz /path/to/directory`
    * `tar -xJvf archive.tar.xz`
    * `tar rvf myTar.tar /etc/hosts`
    * `tar -tvf myTar.tar`
