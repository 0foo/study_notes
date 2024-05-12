## Rsyslogd

* config file at /etc/rsyslog.conf
* config directory is at /etc/rsyslog.d
    * many rpms put configurations in here
    
* /etc/sysconfig/rsyslog
    * can pass rsyslog options to the command when the daemon is starting or restart
    * this file contains a single line to pass option to the command which is used by systemd

* rsyslog.conf sections
    * modules: can add modular functionality  to enhance rsyslogd
    * global parameters: specify global parameters like timestamp format and more
    * rule: what needs to be logged to what location


* to specify what needs to be logged where rsyslogd uses facilities, priorities, and destinations

* facility
    * category of information that is logged
    * can view all facilities with `man 5 rsyslog.conf`
    * facilities are a legacy idea and are kept for backwards compatibility
    * no new facilities can be added for backwards compatibility
    * if a service doesn't have it's own facility can use:
        1. generic daemon facility
        1. local0 through local7 facility
* priority
    * define severity of message to be logged
* destination
    * where a message should be written
    * can be files or also modules that write to another location like database

* a log message type is specified as: <facility>.<priority>     <location>
* rsyslog files configure where to log based on these

* kern.*      /dev/console
    * log all kern source messages to /dev/console

* \*.info      /var/log/messages
    * log all info messages from any source to /var/log/messages


* news.crit     /var/log/spooler
    * log all critical news messages to /var/log/spooler

\*.info      -/var/log/messages
    * can put a hyphen in front of log file to buffer messages first

