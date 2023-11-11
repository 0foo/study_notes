### Log rotation


* the logrotate is started periodically via cron to rotate files
* when a file is rotated the old file is copied to a file that has the date in the filename
    * default weekly and keep 4 old files are stored

* /etc/logrotate.conf is configuration file for log rotate
* can create a logrotate config file in /etc/logrotate.d for specific logfiles that overrides /etc/logrotate.conf
