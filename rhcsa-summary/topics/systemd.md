### ESsentials/Tips
* list available targets to boot into: `systemctl list-unit-files --type=target`
* list available services: `systemctl list-unit-files --type=service`
* `systemd is-enabled <service>`
*  `systemctl isolate`, `systemctl get-default`, `systemctl set-default`
* `systemctl status service`: will have location of service file 
* `loginctl enable-linger <username>` and `~/.config/systemd/user/` and `systemctl --user <command>`

### dealing with services
* systemctl list-units --type service
* enable/disable
* reload
* restart
* start/stop
* status
* systemctl cat <service name>
    * view service file
* systemctl edit <service name>
    * edit service file
* systemctl list-dependencies <service>
* mask/unmask
    * makes it completely impossible to start a service either manually or automatically
    * `systemctl mask sendmail.service`

### Boot systems into different targets manually
* list available targets: `systemctl list-unit-files --type=target`
    * targets with `enabled` status can typically be isolated
    * can only isolate targets that have AllowIsolate=yes set in their unit files
* check current target: `systemctl get-default`
* temporarily switch to different target while system is running: `sudo systemctl isolate target_name.target`
* set a default target for boot: `sudo systemctl set-default target_name.target`
* list all target based dependencies: `systemctl list-dependencies graphical.target | grep target`

### systemd service files
* /etc/systemd/system/<service-files>

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

### Change targets temporarily during boot
1. During boot, interrupt the boot process by pressing a key (usually `Esc` or `Shift`) to enter the GRUB menu.

2. In the GRUB menu, highlight the kernel you want to boot and press `e` to edit the boot options.

3. Find the line that starts with `linux` or `linux16`, and at the end of that line, add one of the following:
   - `systemd.unit=multi-user.target` for multi-user mode.
   - `systemd.unit=graphical.target` for graphical mode.
   - `systemd.unit=rescue.target` for rescue mode.
   - `systemd.unit=emergency.target` for emergency mode.

4. Press `Ctrl + X` or `F10` to boot with the modified options.


### Login linger
* The command loginctl enable-linger <username> is used to allow a user’s systemd user services to run even when that user is not logged in.
* user specific unit files located in: `~/.config/systemd/user/` 