### Archive, compress, unpack, and decompress files using tar, star, gzip, and bzip2

1. `tar`
    * -v is verbose
    * -f is the archive to target

    * To archive using tar use -c:
        ```shell
        tar cvf myTar.tar /home
        ``` 

    * To add file to archive use -r
        ```shell
        tar rvf myTar.tar /etc/hosts
        ```
    
    * To update the files in archive with newer version use -u
        ```shell
            tar rvf myTar.tar /home
        ```
    * View contents of tar file with -t
        ```shell
            tar -tvf myTar.tar
        ```

    * To unpack using tar:
        ```shell
        tar xvf myTar.tar
        ``` 
            * note can use -C to unpack to a target location
            * can unpack a single file by passing in a filename
                * tar xvf myTar.tar /somefile


    * To compress using tar and gzip:
        ```shell
        tar cvfz myTar.tar /home
        ``` 

    * To compress using tar and bzip2:
        ```shell
        tar cvfj myTar.tar /home
        ``` 

    * To decompress using tar and gzip:
        ```shell
        tar xvfz myTar.tar /home
        ``` 

    * To decompress using tar and bzip2:
        ```shell
        tar xvfj myTar.tar /home
        ``` 

    * The star command is an enhanced version of tar. It also supports SELinux security contexts and extended file attributes. The options are like tar.



* tar
    * -c (create)
    * -f (specifies name)
    * -v (verbose)
    * -r (append to existing)
    * -x (extract)
    * -z (compress with gzip)
    * -j (compress with bzip2)
    * Archive file


* star
    * Enhanced tar

1. `gzip`, `bzip2`, `gunzip`, `bunzip2`
    * can use flags with `tar -z(gzip) -j(bzip2)`

    * gzip/bzip2
        * -d (uncompress)
        * Compress files

    * gunzip/bunzip2
        * Uncompress files