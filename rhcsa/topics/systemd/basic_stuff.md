## Systemd


### units
* systemd has different unit's specified by unit files that do different things
* can view all possible units with:
    * systemctl -t help




### systemd config file locations

* /run/systemd/system
    * automatically generated systemd unit files

* /etc/systemd/system
    * customizable file location
    * where to put custom files

* /usr/lib/systemd/system
    * default files from rpm packages
    * never edit directly
    * unit files!!!
    * including all of the isolated unit files!!!


* if files specifying same thing exist in multiple locations priority is:
    1. /run/systemd/system
    1. /etc/systemd/system
    1. /usr/lib/systemd/system

* if changing files, be sure to only edit file in /etc/systmd/system and not the default files auto generated in /usr/lib/systemd/system

* this will override  ON A SETTING BASIS
    * any settings not presetn in the custom edited config file will use the settings from other locations i.e. auto created  /usr/lib/systemd/system


* systemctl edit \<service name>
    * will create a subdirectory in /etc/systemd/system for the service you're editing

* systemctl cat \<service name>
    * shows current configuration of unit file that managers a service

* systemctl show \<unit name>
    * will show ALL units available for this along with their current settings or defaults if not set

* systemctl daemon-reload
    * after editing a systemd unit file will need to reload daemons

#### Service unit files
* these are most important and widely used
* used to start processes
* sections of service unit file:
    1. \[Unit\]
        * descirbes unit and dependencies
        * has Before and After sections
            * Before: start this unit Before the specified unit(s)
            * After: start this unit After the specified unit(s)
    1. \[Service\]
        * describes how to start/stop the service 
        * describes how to request status
        * ExecStart: how to start the unit
        * ExecStop: how to stop the unit
        * Type: start method, fork is most common, used by daemon procs
    1. \[Install\]
        * Indicates which target this unit has to be started

#### Mount unit files
* specifies how a file system can be mounted on a directory
* note: mount points can also be configure via /etc/fstab instead of mount unit files
    * in modern systems this is converted by systemd into mount units behind the scenes

* From man systemd.mount:
    * https://www.freedesktop.org/software/systemd/man/systemd.mount.html

    * Mount units may either be configured via unit files, or via /etc/fstab (see fstab(5) for details). Mounts listed in /etc/fstab will be converted into native units dynamically at boot and when the configuration of the system manager is reloaded. In general, configuring mount points through /etc/fstab is the preferred approach. See systemd-fstab-generator(8) for details about the conversion.

* sections of mount unit files:
    * \[Unit\]
        * After/Before
            * before and after dependencies
        * Conflicts
            * list units that can't be used with this unit, i.e. if this is mutually exclusive with another unit
    * \[Mount\]
        * standard mount information
        * will recognize all of the mount arguments



#### Socket unit files
* defines a port
* has \[Unit\] and \[Install \] sections
* has a \[ Socket \]
    * ListenStream key for TCP and ListenDatagram key for UDP




### Target unit files
* comparable to runlevels
* they're a group of units defining a set state of the system or a function of the system
* ex: printer.target
    * can use this target to start and stop all units the provide printer functionality
* basic.target is the target for units that should always be started
* systemctl list-dependencies
* a target unit file is similar to other unit file types 
    * has \[Unit\]  section with Before/After dependency, Conflicts, Requires, etc.
    * has \[Install\] section
* A target unit does not define it's members in it's unit files, the member unit's define their target in their own unit files




### systemctl

* systemctl enable
    * this ensures unit is automatically started when booting
    * will create a symlink from the service location to /etc/systemd/system/\<some target directory>
    * \[Install\] section determines which folder this symlink is created
    * this is called a wants directory
    * in the following a symlink is created in /etc/systmd/system/multi-user.target
    
    ```
    [Install]  
    WantedBy=multi-user.target
    ``` 
 

  * systemctl start, stop, status, enable(start at boot), disable
  * status info:
    * can get state: Active(running, exited, waiting), Inactive(dead)"
    * enabled/disabled
    * static: can't be enabled but may be stated by another unit

* systemctl list-units
    * shows all active units
* systemctl --type=service
* systemctl list-units --type=service
    * all
* systemctl list-units --type=service --all
    * shows inactive and active service units
* systemctl --failed --type=service
    * show failed services
* systemctl status -l your.service
    * show detailed info about a service




### Systemd dependencies
* certain unit types such as socket and path are directly related to a service unit
* Dependencies defined in the \[Unit\] section:
    * Requires: 
        * if this unit loads these other units loads, 
        * if one other units listed is deactivated so will this be
    * Requisite:
        * if the unit listed here is not already loaded this unit will fail
    * Wants 
        * wants to load units listed here but will not fail if any aren't loaded
    * Before:  
        * this unit will start before the listed units
    * After:
        * this unit will start after the listed units
* systemctl list-dependencies \<unit name>
    * gives the dependencies that this unit needs
    * --reverse option will give the dependencies that need this unit



