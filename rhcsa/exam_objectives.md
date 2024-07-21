### Basics
* Understand and use essential tools
    * [Access a shell prompt and issue commands with correct syntax.](/rhcsa/essentials/shell.md)
    * [Use input-output redirection (>, >>, |, 2>, 2>&1, etc.)](/rhcsa/topics/filesystem/shell.md)
    * [Use grep and regular expressions to analyze text](/rhcsa/topics/filesystem/text_processing.md)
    * [Access remote systems using SSH](/rhcsa/topics/networking/ssh.md) 
    * [Log in and switch users in multiuser targets](/rhcsa/topics/user_group_management/basic_perms.md)
    * [Archive, compress, unpack, and uncompress files using tar, gzip, and bzip2](/rhcsa/topics/filesystem/compression.md)
    * [Create and edit text files](/rhcsa/topics/filesystem/files.md)
    * [Create, delete, copy, and move files and directories](/rhcsa/topics/filesystem/files.md)
    * [Create hard and soft links](/rhcsa/topics/filesystem/files.md)
    * [List, set, and change standard ugo/rwx permissions (symbolic AND numeric)](/rhcsa/topics/user_group_management/basic_perms.md)
    * [Locate, read, and use system documentation including man, info, and files in /usr/share/doc](/rhcsa/topics/filesystem/documentation.md)

### Users/Groups
* Manage users and groups
    * [View, Create, delete, and modify local user accounts](/rhcsa/topics/user_group_management/basic_perms.md)
    * [Change passwords and adjust password aging for local user accounts](/rhcsa/topics/user_group_management/basic_perms.md)
    * [View, Create, delete, and modify local groups and group memberships](/rhcsa/topics/user_group_management/basic_perms.md)
    * [Configure superuser access](/rhcsa/topics/user_group_management/basic_perms.md)
    * [Diagnose and correct file permission problems](/rhcsa/topics/user_group_management)
    * [Create and configure set-GID directories for collaboration](/rhcsa/topics/user_group_management/special_perms.md)

### Storage
* Configure local storage and Create and configure file systems
    * [List, create, delete partitions on MBR and GPT disks](topics/resource_management/storage_management.md)
    * [Create and remove physical volumes](/rhcsa/topics/resource_management/storage_management.md)
    * [Assign physical volumes to volume groups](/rhcsa/topics/resource_management/storage_management.md)
    * [Create and delete logical volumes](/rhcsa/topics/resource_management/storage_management.md)
    * [Configure systems to mount file systems at boot by universally unique ID (UUID) or label](/rhcsa/topics/filesystem/file_system.md)
    * [Add new partitions and logical volumes, and swap to a system non-destructively](/rhcsa/topics/resource_management/storage_management.md)
    * [Create, mount, unmount, and use vfat, ext4, and xfs file systems](/rhcsa/topics/filesystem/file_system.md)
    * [Mount and unmount network file systems using NFS](/rhcsa/topics/filesystem/file_system.md)
    * [Configure autofs](/rhcsa/topics/networking/mounting_network_storage.md)
    * [Extend existing logical volumes](/rhcsa/topics/resource_management/storage_management.md)

### General system tasks
* Operate running systems
    * [Boot, reboot, and shut down a system normally](/rhcsa/topics/boot/power.md)
    * [Boot systems into different targets manually](/rhcsa/topics/boot/3-systemd.md)
    * [Interrupt the boot process in order to gain access to a system](/rhcsa/topics/boot/troubleshooting.md)
    * [Identify CPU/memory intensive processes and kill processes](/rhcsa/topics/resource_management/process_management.md)
    * [Adjust process scheduling](/rhcsa/topics/resource_management/process_management.md)
    * [Manage tuning profiles](/rhcsa/topics/resource_management/device_management.md)
    * [Locate and interpret system log files and journals](/rhcsa/topics/logging)
    * [Preserve system journals](/rhcsa/topics/logging/journald.md)
    * [Start, stop, and check the status of network services](rhcsa/topics/networking/basic_stuff.md)
    * [Securely transfer files between systems](/rhcsa/topics/networking)

* Deploy, configure, and maintain systems
    * [Schedule tasks using at and cron](/rhcsa/topics/scheduled_tasks)
    * [Start and stop services and configure services to start automatically at boot](topics/boot/3-systemd.md)
    * [Configure systems to boot into a specific target automatically(side note: also how to change targets on a  running system)](/rhcsa/topics/boot/3-systemd.md)
    * [Configure time service clients](/rhcsa/topics/networking/time.md)
    * [Install and update software packages from Red Hat Network, a remote repository, or from the local file system]()
    * [Modify the system bootloader](/rhcsa/topics/boot/1-GRUB.md)






### Networking
* Manage basic networking
    * [Configure IPv4 and IPv6 addresses](/rhcsa/topics/networking/basic_stuff.md)
    * [Configure hostname resolution](/rhcsa/topics/networking/basic_stuff.md)
    * [Configure network services to start automatically at boot](/rhcsa/topics/networking/basic_stuff.md)
    * [Restrict network access using firewall-cmd/firewall](/rhcsa/topics/networking/firewalld.md)



### SELinux/firewalld
* Manage security(Firewalld, ACL's/umask, SSH, SELinux)
    * Configure firewall settings using firewall-cmd/firewalld
    * Manage default file permissions
    * Configure key-based authentication for SSH
    * Set enforcing and permissive modes for SELinux
    * List and identify SELinux file and process context
    * Restore default file contexts
    * Manage SELinux port labels
    * Use boolean settings to modify system SELinux settings
    * Diagnose and address routine SELinux policy violations


### Bash scripting
* Create simple shell scripts-[link](/rhcsa/topics/scripting/bash.md)
    * Conditionally execute code (use of: if, test, [], etc.)
    * Use Looping constructs (for, etc.) to process file, command line input
    * Process script inputs ($1, $2, etc.)
    * Processing output of shell commands within a script


### Containers
* Manage containers
    * Find and retrieve container images from a remote registry
    * Inspect container images
    * Perform container management using commands such as podman and skopeo
    * Build a container from a Containerfile
    * Perform basic container management such as running, starting, stopping, and listing running containers
    * Run a service inside a container
    * Configure a container to start automatically as a systemd service
    * Attach persistent storage to a container




* good reference
* https://github.com/jdelgit/rhcsa-notes/tree/master


* Practice questions
* https://github.com/chlebik/rhcsa-practice-questions/tree/master/questions