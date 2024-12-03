### ESsentials/Tips
* know how to list services and targets
* know how to find unit file, how to tell if unit is enabled or masked 
* know how to disable a unit completely from being started
* know how to change targets and set boot target and view current boot target
* location of unit files for root and for user
* know the structure of a service file, can just output existing one for reference
* login linger and user services and how to run a user service even after user has logged out
* know kernel parameter to change the target at boot
* switch systems into different targets temporarily
* boot systems into different targets
* view current target 
* view all targets possible


### dealing with services
* `enable/disable`, `reload`, `restart`, `start/stop`, `status`
* `systemctl list-unit-files --type service|target --all`, `systemctl list-units --type service|target --all` 
    * view dependencies: `systemctl list-dependencies`
    * REMEMBER `--all`!!
* `mask/unmask`: makes it completely impossible to start a service either manually or automatically
*  `systemctl isolate`, `systemctl get-default`, `systemctl set-default`

### Changing targets
* `systemctl isolate`, `systemctl get-default`, `systemctl set-default`    
* can only start targets that have `AllowIsolate=yes` set in their unit files

### Targets
* list available targets: `systemctl list-unit-files --type=target`
    * targets with `enabled` status can typically be isolated
    * can only isolate targets that have AllowIsolate=yes set in their unit files
* check current target: `systemctl get-default`
* temporarily switch to different target while system is running: `sudo systemctl isolate target_name.target`
* set a default target for boot: `sudo systemctl set-default target_name.target`
* list all target based dependencies: `systemctl list-dependencies graphical.target | grep target`
* can change the target at boot with kernel parameter: 
    * `systemd.unit=target.target`  i.e. `emergency.target` or `rescue.target`

### Service files
* view location of service files
    * with `systemctl status <item>`, the unit file location will be in there 
    * `systemctl cat <item>` will output the unit file

* typically located: 
    * /etc/systemd/system/<service-files> for root service files
    * `/home/<username>/.config/systemd/user/`  for user service files

```
[Unit]
Description=<decription>
Want=<wanted-services>

[Service]
Restart=always
ExecStart=/usr/bin/podman start <container-name>
ExecStop=/usr/bin/podman stop -t 2 <container-name>

[Install]
WantedBy=multi-user.target
```


### Login linger
* The command loginctl enable-linger <username> is used to allow a user’s systemd user services to run even when that user is not logged in.
* user specific unit files located in: `~/.config/systemd/user/` 
* `loginctl enable-linger <username>` and `~/.config/systemd/user/` and `systemctl --user <command>`
