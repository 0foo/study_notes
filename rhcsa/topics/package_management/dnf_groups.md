### DNF groups

* environment group
    * An environment group is a larger collection of RHEL packages that provides all necessary software to build the operating system foundation for a desired purpose. 

* group
    * A group, on the other hand, is a small bunch of RHEL packages that serve a common purpose.
    

* `dnf group list`
    * To list all available and installed package groups from all repositories
    * pass as a final parameter
        * `hidden` display all hidden groups as well
        * `installed` display only installed groups
        * `available` display on available groups 

* `dnf group summary`
    * displays number of installed and available groups


* `dnf group info <group name>`
    * lists all packages a group contains
    * use -v for more info

* `sudo dnf group install -y "<group name>"`
    * installs all packages in a group
    * if a package from a group is already present will attempt to upgrade that package to latest version
    
* `sudo dnf group update "<group name>"`
    * upgrades all group packages

* `sudo dnf group remove "<group name>"`
    * uninstalls all packages from the group

