### Journald


* new logging, tightly integrated with systemd
* It centralizes logs from various sources, including system logs, kernel logs, and application logs.
* listens on UDP on /dev/log
* forwards messages to rsyslog
* by default journal has built in logrotation used monthly
* handles it's own compression, cleanup, rotation of old logs, i.e. does not use logrotate
* by default journal will will begin dropping older entries if if:
    * it reaches 10% of file system size
    * the file system only has 15% of it's space left
* can adjust all of these setting in journald.conf
* journald files are written in binary
* use journalctl command to examine journald
* config file: /etc/systemd/journald.conf


### Logging persistence of journald:  /run/log/journal vs /var/log/journal
The directories /run/log/journal and /var/log/journal in Linux systems are related to the storage of system logs, 
specifically those managed by systemd-journald, a service that collects and stores logging data. 
The distinction between these two directories lies in the nature of the storage and persistence of the log files they contain:

* `/run/log/journal`
    * by default all journal  data stored in /run/log/journal as binary data 
    * Temporary Storage: The /run directory is a temporary filesystem (tmpfs) that resides in RAM. 
    * This means that any data stored in /run/log/journal is volatile and gets cleared on reboot. 
    * It does not persist across system restarts.
    * Purpose: It's typically used for storing active system logs that do not need to survive a reboot. This setup is useful for systems that want to minimize write operations to persistent storage (like SSDs), which can extend the hardware's life.
    * Performance Considerations: Storing logs only in RAM (/run/log/journal) can reduce disk I/O, which might be beneficial for performance and disk longevity, especially on systems with flash storage. However, it means losing logs at reboot, which can be a drawback for diagnosing issues that occur before a system crash or reboot.

* `/var/log/journal`
    * Persistent Storage: Unlike /run, the /var directory resides on persistent storage. 
    * Log files stored in /var/log/journal are maintained across reboots, providing a permanent record of system logs.
    * Purpose: This directory is used when log persistence is required. It allows system administrators and tools to review historical data for troubleshooting, audit, and system performance analysis over longer periods.
    * Management and Compliance: For systems where log retention is critical for compliance or detailed system analysis, using /var/log/journal is essential.

* Configuration and Usage
    * System Configuration: Whether systemd-journald uses /run/log/journal, /var/log/journal, or both can depend on system configuration. 
    * By default, systemd-journald may store logs in /run/log/journal and will only store them persistently in /var/log/journal if the directory exists or specific configurations are set.

* Creating Persistent Logs: 
    * If a system administrator wants to ensure logs are stored persistently, they can:
    * create the /var/log/journal directory and if Storage setting in journald.conf `Storage=auto` this will start persistent logging just with the directory being created
    * adjust the journald configuration (/etc/systemd/journald.conf) to specify the storage behavior.
    * in /etc/systemd/journald.conf a setting `Storage=`
        * `auto`: journal written to /var/log/journal IF this directory exists
            * this is the default
            * be sure this directory is also owned by root:systemd-journal and 2755 permission with guid set
        * `volatile`: never persist to /var/log/journal is wiped every restart
        * `persistent`: will create /var/log/journal for you and always save the data
        * `none`: will never write to the journal but forwarding to other targets still works

```
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journalctl
sudo chown root:systemd-journal /var/log/journal
sudo chmod 2755 /var/log/journal
sudo systemctl restart systemd-journald
ls -l /var/log/journal  # verify via log existence
journalctl --disk-usage  # verify via disk usage
```
    



