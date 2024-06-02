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


### Exam Objectives:  Archive, compress, unpack, and uncompress files using tar, gzip, and bzip2


* **Using `tar` for Archiving and Compressing**:
  * **Create an Archive**:
    * `tar -cvf archive.tar file1 file2 dir1`: Create an uncompressed archive.
  * **Extract an Archive**:
    * `tar -xvf archive.tar`: Extract an uncompressed archive.
  * **View Contents of an Archive**:
    * `tar -tvf archive.tar`: List the contents of an archive.
  * **Create a Compressed Archive with gzip**:
    * `tar -czvf archive.tar.gz file1 file2 dir1`: Create a gzip-compressed archive.
  * **Extract a gzip-compressed Archive**:
    * `tar -xzvf archive.tar.gz`: Extract a gzip-compressed archive.
  * **Create a Compressed Archive with bzip2**:
    * `tar -cjvf archive.tar.bz2 file1 file2 dir1`: Create a bzip2-compressed archive.
  * **Extract a bzip2-compressed Archive**:
    * `tar -xjvf archive.tar.bz2`: Extract a bzip2-compressed archive.

* **Using `gzip` and `gunzip`**:
  * **Compress a File**:
    * `gzip file`: Compresses the file, resulting in `file.gz`.
  * **Uncompress a File**:
    * `gunzip file.gz`: Uncompresses the file, restoring the original file.

* **Using `bzip2` and `bunzip2`**:
  * **Compress a File**:
    * `bzip2 file`: Compresses the file, resulting in `file.bz2`.
  * **Uncompress a File**:
    * `bunzip2 file.bz2`: Uncompresses the file, restoring the original file.

* **Using `tar` with gzip and bzip2**:
  * **Compress with gzip**:
    * `tar -czvf archive.tar.gz file1 file2 dir1`: Combines tar and gzip to compress files into an archive.
  * **Compress with bzip2**:
    * `tar -cjvf archive.tar.bz2 file1 file2 dir1`: Combines tar and bzip2 to compress files into an archive.
  * **Extract with gzip**:
    * `tar -xzvf archive.tar.gz`: Extracts a tarball compressed with gzip.
  * **Extract with bzip2**:
    * `tar -xjvf archive.tar.bz2`: Extracts a tarball compressed with bzip2.
