### Misc
* create a file: `fallocate -l 100M`
* backslash before command \rm will use an unaliased command
* find out if a command is an alias: type <command>
* Always use visudo to edit the sudoers file
* sudo will not run any alias or function even root as it does not include any env context
* get all aliases with `alias` command
* `file` command to tell which type of file it is

* text block via cli
```
cat <<EOF > file.txt
This is line 1.
This is line 2.
This is line 3.
EOF
```

### Man
* use section 5 for files
* use regular man for commands
* man -K
    * searches for a keyword
    * -w is case sensitive
* catman
    * updates all manual pages
* catman && man -K



### access





### NFS/AutoFS
* show all remote mounts for a server
* mount an nfs share via cli
* mount an remote fs permanantly via file
* mount an remote fs permanantly via autofs

### Logging
* journald, journalctl, ausearch

### File system
* create swap
* create file system
* adjust file system size
* mount file system
* format a volume
* permanantly mount existing volume
* LVM

### Shutdown/reboot
* shutdown -r now
* shutdown -h now

### processes
* search processes
* kill processes
* set process priority
* set process niceness

### scp
* scp <remote-user>@<host/ip>:/remote/path/to/source /local/path/destination
* scp /loca/path/source <remote-user>@<host/ip>:/remote/path/to/destination



### Systemd
* systemctl
    * enable, mask, isolate, get-default/set-default
* /etc/systemd/system/
* list all target units

### journald
* TBI

### time
* add ntp servers
    * remember after updating chrony.conf to restart
* enable/disable ntp with timedatectl
* change timezone with timedatectl and symlink in /etc

### DNF
* repo files @ /etc/yum/yum.repos.d
* 


### general-networking
* hostnamectl

### resolvers
* never modify /etc/resolv.conf directly!
* nmcli connection modify <connection-name> ipv4.dns "<DNS-Server-IP>"  
    * nmcli connection reload 
    * systemctl restart NetworkManager
* /etc/resolve.conf
* /etc/hosts


### selinux
* Primary commands
    * `sestatus`
    * `setenforce 1` or `0`
    * `ls -Z`
    * `sudo semanage fcontext -a -t httpd_sys_content_t "/repo-write(/.*)?"`
    * `sudo restorecon -R /repo-write`
    * `sudo chcon -R -t httpd_sys_content_t /repo-write`
    * can run `man semanage-fcontext` and search `/example`to see examples


### selinux booleans
* getsebool -a
* getsebool boolean_name
* setsebool boolean_name on|off
* sudo setsebool -P boolean_name on|off
* semanage boolean -l


### bash scripting
* for loop, read command, conditional, test


```
# Read a file line by line
while read line; do
    echo "$line"
done < input_file.txt
```

```
if [ "$str1" = "$str2" ]; then
  echo "Strings are equal."
else
  echo "Strings are not equal."
fi

# double brackets allow regex/pattern matching
if [[ "$str" == hello* ]]; then
  echo "String starts with 'hello'."
else
  echo "String does not start with 'hello'."
fi
```

* pipe to while loop
```
ls | while read file; do
  echo "File: $file"
done
```
* note: the while loop is in a subshell so subshell free version:
```
count=0
while read line; do
  echo "Processing: $line"
  count=$((count + 1))
done < <(ls)
```

```
IFS=$'\n'; for i in $(ls -d1 */); do echo "$here/$i"; cd "$here/$i"; ls; cd $here; done;
```

```
for i in $(ls); do echo "LOCATION: $here/$i"; test -d "$here/$i" && cd "$here/$i"; ls; cd ~; done;
```

### Find all keyword in all bash scripts on the system
find / -iname "*.sh" -exec fgrep -H -n -A3 -B3 -- "case" {} \; 2>/dev/null | less

### containers
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






### firewalld
* firewall-cmd
* https://github.com/jdelgit/rhcsa-notes/blob/master/07.%20Manage%20Basic%20Networking.md#restrict-network-access-using-firewall-cmdfirewall
* primary commands
    * `sudo firewall-cmd --list-all`
    * `sudo firewall-cmd --add-service=http --permanent --zone=public`
