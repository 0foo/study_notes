* Understand and use essential tools
    * [Access a shell prompt and issue commands with correct syntax.](/essentials/shell.md)
    * [Use input-output redirection (>, >>, |, 2>, 2>&1, etc.)](/essentials/shell.md)
    * [Use grep and regular expressions to analyze text](/topics/filesystem/text_processing.md)
    * [Access remote systems using SSH](/topics/networking/ssh.md) 
    * [Log in and switch users in multiuser targets](/essentials/shell.md)
    * [Archive, compress, unpack, and uncompress files using tar, gzip, and bzip2](topics/filesystem/compression.md)
    * [Create and edit text files](/topics/filesystem/files.md)
    * [Create, delete, copy, and move files and directories](/topics/filesystem/files.md)
    * [Create hard and soft links](/topics/filesystem/files.md)
    * [List, set, and change standard ugo/rwx permissions (symbolic AND numeric)](/topics/user_group_management/basic_perms.md)
    * Locate, read, and use system documentation including man, info, and files in /usr/share/doc 

* Create simple shell scripts
    * Conditionally execute code (use of: if, test, [], etc.)
    * Use Looping constructs (for, etc.) to process file, command line input
    * Process script inputs ($1, $2, etc.)
    * Processing output of shell commands within a script
    * all of these topics addressed here: [link](/topics/scripting/bash.md)

* Operate running systems
    * [Boot, reboot, and shut down a system normally](/topics/boot/power.md)
    * [Boot systems into different targets manually](/topics/boot/3-systemd.md)
    * [Interrupt the boot process in order to gain access to a system](/topics/boot/troubleshooting.md)
    * [Identify CPU/memory intensive processes and kill processes](/topics/resource_management/process_management.md)
    * [Adjust process scheduling](/topics/resource_management/process_management.md)
    * Manage tuning profiles
    * Locate and interpret system log files and journals
    * Preserve system journals
    * Start, stop, and check the status of network services
    * Securely transfer files between systems

* Configure local storage
    * List, create, delete partitions on MBR and GPT disks
    * Create and remove physical volumes
    * Assign physical volumes to volume groups
    * Create and delete logical volumes
    * Configure systems to mount file systems at boot by universally unique ID (UUID) or label
    * Add new partitions and logical volumes, and swap to a system non-destructively

* Create and configure file systems
    * Create, mount, unmount, and use vfat, ext4, and xfs file systems
    * Mount and unmount network file systems using NFS
    * Configure autofs
    * Extend existing logical volumes
    * Create and configure set-GID directories for collaboration
    * Diagnose and correct file permission problems

* Deploy, configure, and maintain systems
    * Schedule tasks using at and cron
    * Start and stop services and configure services to start automatically at boot
    * Configure systems to boot into a specific target automatically
    * Configure time service clients
    * Install and update software packages from Red Hat Network, a remote repository, or from the local file system
    * Modify the system bootloader

* Manage basic networking
    * Configure IPv4 and IPv6 addresses
    * Configure hostname resolution
    * Configure network services to start automatically at boot
    * Restrict network access using firewall-cmd/firewall

* Manage users and groups
    * View, Create, delete, and modify local user accounts
    * Change passwords and adjust password aging for local user accounts
    * View, Create, delete, and modify local groups and group memberships
    * Configure superuser access


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


* Manage containers
    * Find and retrieve container images from a remote registry
    * Inspect container images
    * Perform container management using commands such as podman and skopeo
    * Build a container from a Containerfile
    * Perform basic container management such as running, starting, stopping, and listing running containers
    * Run a service inside a container
    * Configure a container to start automatically as a systemd service
    * Attach persistent storage to a container