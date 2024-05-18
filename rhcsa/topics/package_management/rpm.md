### RPM's
* single package package installer
* will not resolve dependencies
    * have to manage/install dependencies yourself
    * sometimes have to install entire chains of dependencies


### Package database
* location: /var/lib/rpm


* two package databases are maintained, yum and rpm
    * if install package with yum, rpm database will be updated
    * if install package with rpm, yum database will NOT be updated
    * so always install via yum and no longer use RPM for package installation

* rpm filename
    * <packagename>-<version>-<subversion>-<redhat version this package was targetted for>-<platform package creatd for>
    * ex: autofs-5.0.7-40.el7.x86_64.rpm

* rpm command is great for querying packages still


* rpm -q flag queries the rpm database
    * queries packages already installed on system
    * rpm -q<subflag> <packagename>
        * -q
            * if no subflag will simply tell if package is installed
        * -qa
            * list all installed packages
            * similar to yum list installed
        * -qi 
            * list info about installed package
        * -ql
            * list all files in installed package
        * -qd
            * get all documentation files from installed package
        * -qc 
            * get all configuration files
        * -qR
            * get all package dependencies
        * -qf <some file name>
            * list which packages own this file
        * -q --whatrequires
            * which packages use this package as a dependency
        * -V   
            * which parts of package have changed since installation
        * -qip <name of some .rpm file>
            * pass a .rpm file to find out information about it
            * used to look at package files before installation
            * need to use complete filename
            * rpm -qip --scripts
                * queries the package for any scripts
                * useful to find out if the package about to install contains any scripts 
            * only woks on package files, does not look at repositories


* rpm -ivh
    * -i -> install an rpm
    * -v -> (verbose)
    * -h -> (hashmarks) show progress bar

* rpm -ivh --replacepkgs
    * will overwrite a package
    * useful if you suspect corruption in a package and want to start fresh

* rpm -U
    * upgrades a package
    * will install if it doesn't exist

* rpm -F
    * 'freshen'
    * upgrades a package
    * will not install if not exist

* rpm -ev
    * -e -> uninstall
    * -v -> verbose
    * note: this will fail if any packages depend on it

* rpm2cpio
    * can be used to extract files from an .rpm package
    * good for:
        * examining the contents of the package
        * replacing a corrupted or lost command
        * replacing a critical configuration file of an installed package to its original state
    * converts to a cpio file which can then be operated on by cpio tool
    * `rpm2cpio package-file.rpm | cpio -idmv`
        * -i: Extract files from the archive.
        * -d: Create leading directories where needed.
        * -m: Preserve modification times.
        * -v: Verbose mode, showing the files being extracted.

* rpm -K package-file.rpm
    * checks both signature and integrity of an rpm FILE
        * signature verifies that the packages comes from correct source
            * uses keys installed on the system, see section
        * integrity verifies that the package contents are correct
            * uses checksums/Hashes that are included in the package
    * can pass --nosignature to only check integrity

* `rpm -V` <package name>
    * verifies the interegity of an INSTALLED package
    * `rpm -Va`
        * verifies ALL packages
    * `rpm -Vf` <some file name>
        * can verify if a single file has changed
    * by default will only output changed files
    * to output every file even if it hasn't changed use -v flag    
        * `rpm -Vv`
    * outputs a list of codes that tell what has changed about the file
        * S: The file size has changed.
        * M: The file mode (permissions) or file type has changed.
        * 5: The MD5 checksum of the file has changed.
        * D: The device number has changed.
        * L: A symbolic link has changed.
        * U: The user ownership has changed.
        * G: The group ownership has changed.
        * T: The modification time (timestamp) of the file has changed.
        * A dot (.): No changes were detected for this attribute.
    * shows the file type also
        * c: Configuration file
        * d: Documentation file
        * g: Ghost file
        * l: License file
        * r: Readme file



### GPG keys
* location of GPG keys in RHEL
    * `/etc/pki/rpm-gpg/`
    * this is called a GPG keyring

* used to verify the package is from the correct source and is authentic

* sudo rpmkeys --import <some GPG key file or key id>
    * will either copy the gpg file into the directory
    * however, if a key id file is passed instead of a key, this command will fetch the co-oresponding key from the key server and put into the directory
* view keys:
    * `rpm -q gpg-pubkey`
        * lists all gpg keys
    * `rpm -qi gpg-pubkey-fd431d51-4ae0493b`
        * lists information about a single key


### Working with remote repos with RPM
* repoquery 
    * allows querying the package in the repos
    * part of yum-utils package
    * similar flags as rpm 
    * no --scripts flag, have to download the package file first

* yumdownloader
    * in yum-utils package
    * allows downloading just the package file from the repos

