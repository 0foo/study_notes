## Logging


* services write to logs in numerous ways
    1. append directly to a log file
    1. rsyslogd
        * enhancement of syslogd
        * manages centralized log files
        * write messages to different files in /var/log directory
        * has module's that act as plugins to do different functions such as writing to a database or filtering 
        
    1. journald and systemd-journald
        * tightly integrated with systemd and allows getting log info
        * gets alot of system info: kernel, entire boot prodecure, services
        * writes this info to a binary even journal
        * use journalctl to read this info
        * this journal is not persistent between reboots (unless configured explicitly)
        * also forwards messages to rsyslogd


* to investigate a system have to:
    1. monitor /var/log folders
    1. use journalctl to get info from the journal
    1. use systemctl status <unit> to get info on the specific units in systemd


### Log rotation


* the logrotate is started periodically via cron to rotate files
* when a file is rotated the old file is copied to a file that has the date in the filename
    * default weekly and keep 4 old files are stored

* /etc/logrotate.conf is configuration file for log rotate
* can create a logrotate config file in /etc/logrotate.d for specific logfiles that overrides /etc/logrotate.conf



### common log files
    * /var/log/messages
        * most commonly used log file, generic log file where most messages are written
    * /var/log/dmesg
        * kernel log messages
    * /var/log/secure
        * authentication related errors, can look at authentication errors here
    * /var/log/boot.log
        * messages related to system startup
    * /var/log/audit/audit.log
        * audit messages, SELinux writes to this file
    * /var/log/maillog
        * mail related logging
    * /var/log/samba
        * samba logging, written directly and not through rsyslog
    * /var/log/sssd
        * ssd logs, i.e. authentication service
    * /var/log/cups
        * print service cups
    * /var/log/httpd
        * apache web service, written directly and not through rsyslog

    * some common log file fields
        * data, originating host, servie or process name, log message content
    
    * tail -f file.log



