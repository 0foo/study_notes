### KNOW
* start, stop, remove, view containers/images
* ports, volumes, naming
* run a command in a running container and in a container not yet created
* list all registries/file where registries defined (both root file and user file)
* run podman commands on all containers
* search registries and inspect local and remote images
* running commands on user level containers 
* creating service files for containers
* managing containers with systemd
    * what service files folder to create for user an what folder to navigate for root?
    * what command to generate the file
    * remember: delete container, reload systemd daemons
    * how to start/stop these generated containers with systemctl
* allow systemd service containers to run even if user not logged in
    * loginctl
        * enable-linger
        * disable-linger
        * show-user <username>
    * enable service in systemd



* `podman login <registry>`
* `podman search <package>`
    * always search because the package could be in a subdirectory

* `ps`, `rmi`, `rm`, `pull`, `run`, `stop`, `restart/kill`, `exec`, `info`, `login`, `images`
* flags: `--it, --rm`, `-d`, `-p`, `--name`, `-d`
    * `-a`
        * can run bulk commands on containers
        * `ps -a, rm -a, stop -a`
    * `-e MYSQL_USER=user_name`: pass in env variables
    * `-p 8000:8080` : open a port to local host
    * mount a local directory in container with `-v`
        * `-v <source dir>:<dest dir inside container>:Z`
        * note: the contents of source dir will be mounted inside of the dest dir
        * NEED THE Z for selinux to add the context to the source dir
        * mount directory(persistent storage) inside of container

* `pull` vs `run`: 
    * run will will pull it from registry and instantiate
    * pull will just pull the image locally

* `podman port -a`
    * You can use the podman port command with a container ID or name to list its port mappings,
    * or with the -a option to list all port mappings in use.

* `exec`
    * can run a command from a container with exec
    * `podman exec 7ed6e671a600 cat /etc/redhat-release`
    * `podman exec -it my_webserver /bin/bash`
* `run`
    * can run a command from an image with run DONT NEED `-it`
    * `podman run --name myquickweb --rm registry.lab.example.com/rhel8/httpd-24:1-105 cat /etc/redhat-release`





* can start/stop/restart with --name or container id
* config file : `/etc/containers/registries.conf`
* config file non-root: `~/.config/containers/registries.conf`

### Search/Inspect 
* do `podman search` to find images and do a `skopeo inspect` to find versions of that image
* `skopeo inspect docker://registry.redhat.io/rhel8/python-36`
    * The skopeo inspect command can inspect different image formats from different sources, such as remote registries or local directories. 
    * The docker:// triggers remote inspection
    * can view all versions/tags that are available
* `podman inspect registry.redhat.io/rhel8/python-36`: inspect local images
* `podman search <image>`:search for an image in registries


### Systemd containers
* make folder: `~/.config/systemd/user/`
* generate a systemd service file for a user
* `[user@host ~]$ cd ~/.config/systemd/user/` 
* `[user@host user]$ podman generate systemd --name web --files --new` : omit `--new` if you dont want the container to be 
deleted every time it stops
    * cd to the user directory: `~/.config/systemd/user/`  for user container services
    * cd to root directory: `/etc/systemd/system` for root container services
* `systemctl --user daemon-reload`
* After the file is created, you must delete the container because systemd expects the container to be absent initially.
* if generating it for root: simply run the above command in :  `/etc/systemd/system`
* all the commands are the same for user containers as root but with `--root` flag 
    * `systemctl --user start container-web`
    * Containers managed with the systemctl command are controlled by systemd. systemd monitors container status and restarts them if they fail.
* still use `enable` to start when computer starts: `systemctl --user enable container-web`
Do not use the podman command to start or stop these containers. Doing so may interfere with systemd monitoring.
* The command `loginctl enable-linger <username>` or just `loginctl enable-linger` if logged in. 
    * is used to allow a user’s systemd user services to run even when that user is not logged in.
* unit files located in: `~/.config/systemd/user/` 
* To control your new user services, use the systemctl command with the --user option
* `systemctl --user enable my-service.service`
* If these steps are done, then my-service.service will automatically start whenever the system boots




### TO BE ORGANIZED
* podman
    * build -t my-apache .
    * run -d -p 8080:80 --name apache-container -v /path/to/local/directory:/path/in/container my-apache
    * ps
    * stop apache-container
    * rm apache-container
    * pull <image>
    * logs <container_id>
    * exec -it <container_id> /bin/bash
    * rmi <image_id>
    * images
    * rm $(ps -a -q)
    * rmi $(images -f "dangling=true" -q)

* setup podman search
    * unqualified-search-registries=["registry.access.redhat.com", "registry.fedoraproject.org", "docker.io"]
    * cat /etc/containers/registries.conf

* Configure a container to start automatically as a systemd service
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
