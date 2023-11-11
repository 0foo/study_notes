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
        * this journal is not persistent between reboots
        * also forwards messages to rsyslogd


* to investigate a system have to:
    1. monitor /var/log folders
    1. use journalctl to get info from the journal
    1. use systemctl status <unit> to get info on the specific units in systemd

* common log files
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
    
    * tail -f file.lgo


    ### write to logfile from bash
    * can use logger command to write to rsyslogd from bash or script
    * logger <message>
    * sends message to /var/messages
    * add -p for an error priority 
    * logger writes to /dev/log which is a socket via udp 
        * journald is listening on that socket
        * journald records then forwards the message to rsyslog
    * https://unix.stackexchange.com/questions/464361/examining-dev-log
    * https://serverfault.com/questions/959982/is-rsyslog-redundant-on-when-using-journald
    