

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


### journalctl
    * reports starting from oldest to newest
    * -f : latest 10 messages
    * -r : view in newest to oldest
    * -u : log of a specific unit/process/daemon
    * G will go to end
    * / and ? work to search
    * --no-pager : shows output without a pager i.e. like a cat
    * journalctl -xb
        * shows boot logs