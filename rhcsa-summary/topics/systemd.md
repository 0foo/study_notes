
### Systemd
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
    * note disable just stops it from starting at boot but can be started manually
* isolate
* get-default/set-default
* systemctl list-units --type target




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
