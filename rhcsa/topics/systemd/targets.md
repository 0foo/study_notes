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