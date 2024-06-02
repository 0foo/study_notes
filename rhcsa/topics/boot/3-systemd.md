## Systemd

###  initialization process


1. **Kernel Initialization**: The kernel initializes hardware, mounts the initial root filesystem (usually provided by `initramfs`), and starts the first userspace process, which is typically `systemd`.

2. Startup systemd: `systemd` is started as the init process (PID 1). It takes over the process of booting the system.
    ```sh
   /sbin/init
   ```

3. Initialize systemd: `systemd` starts by reading its configuration files, primarily located in `/etc/systemd/`.
    * See below for more info

4. Mount filesystems: `systemd` mounts necessary filesystems defined in the `fstab` file and in `systemd` unit files.
    * Root filesystem is already mounted by the kernel.
    * Other filesystems like `/home`, `/var`, `/tmp`, etc., are mounted.
    * Virtual filesystems like `proc`, `sysfs`, and `tmpfs` are also mounted.
    ```
    # run /etc/fstab
    mount -t proc proc /proc
    mount -t sysfs sys /sys
    mount -t devtmpfs dev /dev
    ```

5. Run Early Boot Services: Services required early in the boot process are started, such as:
    * udev: For device management.
    * tmpfiles: For creating temporary files and directories.

6. Sysinit Target: Completes basic system initialization, including:
    * Applying kernel parameters.
    * Setting up system time.
    * Initializing random seed.

7. Switch to default target
    * The default target is typically `default.target`, which is often an alias for `multi-user.target` or `graphical.target`.

4. Start services: 
    * `systemd` starts all required services in parallel, according to their dependencies and the specified target. 
    * Services are defined in unit files with `.service` extension.

5. Handling Sockets and Devices 
    * `systemd` manages sockets and devices using `.socket` and `.device` units. 
    * This allows it to handle activation on demand (socket activation) and respond to device availability (udev).



### units
* systemd has different unit's specified by unit files that do different things
* can view all possible units with:
    * systemctl -t help


### systemd config file locations

* /run/systemd/system
    * base level OS systemd unit files

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

* if changing files, be sure to only edit file in /etc/systemd/system and not the default files in /usr/lib/systemd/system

* this will override  ON A SETTING BASIS
    * any settings not presetn in the custom edited config file will use the settings from other locations i.e. /usr/lib/systemd/system


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


## Systemd targets
* A systemd target is a group of systemd units that belong together
    * some targets are states that a system needs to enter into 
        * default.target, graphical.target, multi-user.target
    * some targets are just a bundle of units that work together
        * nfs.target, printer.target

* systemctl enable and systemctl disable
    * add units to targets


### Isolated Target states
    * these are isolated targets
        * Isolatable targets contain everything a system needs to boot or change its current state.
        * essentially a complete state for a system
        * targets you can set to get into after a system starts
        * an isolated target starts with all of its dependencies
    
    * contain: `AllowIsolate=yes` in unit file

    * use `systemctl isolate` command to switch to a differnt isolated target


    * emergency.target
        * only minimal number of units is started, just enough to fix your system 
    * rescue.target
        * start all systems to get a fully functional linux system, but no non-essential unit
    * multi-user.target
        * default target a system starts in
        * starts everything needed for full system functionality
    * graphical.target
        * starts all units needed for fully functional linux system, as well as graphics

    * co-orespond to legacy run levels
        * poweroff.target runlevel 0
        * rescue.target runlevel 1
        * multi-user.target runlevel 3
        * graphical.target runlevel 5
        * reboot.target runlevel 6
    
    * switch to a new isolated target with `systemctl isolate`
        * can grep for grep Isolate *.target in `/usr/lib/systemd/system` to find all the units that allow isolation
        * switch to the target with :`systemctl isolate rescue.target``
        * Interesting note: `systemctl isolate reboot.target` reboots computer



### Target unit file
```
[Unit]
Description=Multi-User System
Documentation=man:systemd.special(7)
Requires=basic.target
Conflicts=rescue.service rescue.target
After=basic.target rescue.service rescue.target
AllowIsolate=yes
```

* does not contain much.  defines:
    * what it requires 
    * which services and targets it cannot coexist with. 
    * load ordering, by using the After statement in the [Unit] section.
* The target file does not contain any information about the units that should be included!!!
    * that is in the individual unit files and the wants in the [Install] section

### Target wants
    * Wants in Systemd define which units Systemd wants when starting a specific target.
    * Wants are created when Systemd units are enabled using systemctl enable
    * a want co-oresponds to a symbolic link in the /etc/systemd/system directory
    * In this directory, you’ll find a subdirectory for every target, containing wants as symbolic links to specific services that are to be started.
    * the [Install] section in the service unit file, the services know for themselves in which targets they need to be started
        * when systemctl enable is run will create the symlink
 
    * /etc/systemd/system
        * contains a directory for every target
        * in the directory is a symlink for every target wants
        * symlink to specific services that need to be started
    
    * Define the target a unit needs to be started in in the [Install] section of the unit file


### Viewing targets
* systemctl --type=target
    * see a list of targets currently active on the computer
* systemctl --type=target --all
    * see all targets available active and inactive
* can grep for grep Isolate *.target in `/usr/lib/systemd/system` to find all the units that allow isolation


### Setting the default target
* Type systemctl get-default to see the current default target 
* use systemctl set-default to set the desired default target


### User systemd processes
* Having multiple `systemd` processes on a Linux system is normal and expected. Here are the primary reasons why you might see more than one `systemd` process:
1. `systemd` as the Init System
    * The main `systemd` process (PID 1) is the init system responsible for initializing and managing the system. This process is started by the kernel at boot and is the ancestor of all other processes on the system.
2. User `systemd` Instances
    * In addition to the system-wide `systemd` instance (PID 1), there can be user instances of `systemd` for managing user sessions. These user instances handle user-specific services and are started when a user logs into the system.

* Example Scenario
1. **Main `systemd` process**: This is the primary system `systemd` process with PID 1.
2. **User `systemd` processes**: These are user session instances of `systemd`.

* Checking the `systemd` Processes
    * You can use `ps` to list the `systemd` processes and see their details:
```bash
ps -C systemd -o pid,ppid,user,cmd
```