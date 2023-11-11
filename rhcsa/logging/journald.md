### Journald

* listens on UDP on /dev/log
* forwards messages to rsyslog


* writes it's data in a binary format in the location: /run/log/journal
* use journalctl to examine this file


* journalctl
    * reports starting from oldest to newest
    * -f : latest 10 messages
    * -r : view in newest to oldest
    * G will go to end
    * / and ? work to search
    * --no-pager : shows output without a pager i.e. like a cat


* journal file persistence
    * by default all journal  data stored in /run/log/journal as binary data
    * the entire /run directory is cleansed each reboot due to /run being a memory based tempfs
    * in /etc/systemd/journald.conf a setting `Storage=`
        * `man 5 journald.conf`
        * auto: journal written to /var/log/journal IF this directory exists
            * this is the default
            * be sure this directory is also owned by root:systemd-journal and 2755 permission with guid set
        * volatile: never persist to /var/log/journal is wiped every restart
        * persistent: will create /var/log/journal for you and always save the data
        * none: will never write to the journal but forwarding to other targets still works
    * journal has built in logrotation used monthly
    * journal will will begin dropping older entries if if:
        * it reaches 10% of file system size
        * the file system only has 15% of it's space left
    * can adjust all of these setting in journald.conf

* journalctl -xb
    * shows boot logs