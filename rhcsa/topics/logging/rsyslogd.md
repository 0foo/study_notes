## Rsyslogd
* classic logging system whereas journald is a subsystem of systemd
* stores log in plain text typically in /var/log
* can be configured in depth over formatting routing and filtering and more
* can send logs via network
* follow the syslog standard so can be integrated with old tools
* relies on external tools like logrotate for rotation, compression,  cleanup

### Files
*  /etc/rsyslog.d
    * config directory for applications using rsyslogd
    * this is where many application put their logging configuration
    * many rpms put configurations in here

* /etc/sysconfig/rsyslog
    * Used for setting environment variables and startup options.
    * Contains shell variable assignments.
    * can pass rsyslog options to the command when the daemon is starting or restart
    * this file contains a single line to pass option to the command which is used by systemd
    * Used by the init scripts or systemd service files to start the rsyslog service with specific options.
    * Modifying this file usually requires a restart of the rsyslog service for changes to take effect.

*  /etc/rsyslog.conf
    *  Used for defining the logging rules, log destinations, and log processing logic.
    *  Contains rsyslog configuration directives and syntax.

* rsyslog.conf sections
    * modules: can add modular functionality  to enhance rsyslogd
    * global parameters: specify global parameters like timestamp format and more
    * rule: what needs to be logged to what location

### Configuring rsyslog
* to specify what needs to be logged where rsyslogd uses facilities, priorities, and destinations

* facility
    * category of information that is logged
    * can view all facilities with `man 5 rsyslog.conf`
    * facilities are a legacy idea and are kept for backwards compatibility
    * no new facilities can be added for backwards compatibility
    * if a service doesn't have it's own facility can use:
        1. generic daemon facility
        1. local0 through local7 facility
    * while many programs can use the same facility, you can differentiate their logs using other syslog attributes like the program name, severity levels, or custom tags.
    * this can be passed in from the program via metadata (see below) 

* priority
    * define severity of message to be logged

* destination
    * where a message should be written
    * can be files or also modules that write to another location like database

* a log message type is specified as: <facility>.<priority>     <location>
* rsyslog files configure where to log based on these

* examples:
    * `daemon.* /var/log/daemon.log`
        * logs all of the generic daemon message to the /ver/log/daemon.log

    * `kern.*      /dev/console`
        * log all kern source messages to /dev/console

    * `\*.info      /var/log/messages`
        * log all info messages from any source to /var/log/messages

    * `news.crit     /var/log/spooler`
        * log all critical news messages to /var/log/spooler

    `\*.info      -/var/log/messages`
        * can put a hyphen in front of log file to buffer messages first

### What happens if have more programs then generic or local log facilities?

* not on the RHCSA but for edification

* When you have a large number of programs each requiring its own logging facility, but only eight local facilities (local0 through local7) available, you will need to consider alternative strategies for effectively managing and distinguishing between their logs. 

* Here are several approaches you can take:

1. Combine Multiple Programs under One Facility

* You can categorize similar types of programs under the same facility and use additional properties such as program names or tags within the logs to differentiate them. 

* This requires configuring your logging **within each program** to include identifiable information.

Example Configuration in rsyslog:

```
if $programname == 'program1' and $syslogfacility-text == 'local0' then /var/log/program1.log
if $programname == 'program2' and $syslogfacility-text == 'local0' then /var/log/program2.log
```

* This approach uses the same facility (local0) but filters logs into different files based on the program name.
* you can pass in metadata when making the rsyslog call 
* `logger -t program1 -p local0.info "This is a test message from program1"`
* this adds program1 to allow access by the $programname variable in rsyslog
* also most programming languages have rsyslog packages that can pass this metadata

2. Use Structured Logging
* Enhance log messages with structured data (like JSON), which can include specific fields identifying the program, module, or any other context needed. rsyslog supports parsing and filtering based on structured data.

3. Dynamic File Paths
* Configure rsyslog to dynamically write logs to different files based on message content, such as program names or tags.

4. Centralized Log Management
* Consider using a centralized log management system that can handle more complex filtering, parsing, and querying, such as ELK Stack (Elasticsearch, Logstash, Kibana) or Graylog. These systems can intake logs from rsyslog and allow you to define very granular processing rules and visualizations.
