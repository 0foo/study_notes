## user,groups 
* add, remove, modify, search for a user: 
* add, remove, modify, search for a group
* add/remove user from a group (tricky)
* view all groups a user is in
* view id's of user 
* change password for users/root
* set password age
* set password complexity requirements

### performance profiles
* change, view current, list all profiles, list reccomended

## compression
* compress/uncompress files 
* create archive of file
* know tar command parameter order of source and destination !!

### scheduled
* at
    * know how to create at's
    * view all at's
    * remove an at

* cron
    * create/view cronjobs for root and users
    * resources:
        * cat /etc/crontab to view format of cron and 
        * can view files in /etc/cron.* for examples
        * man 5 crontab
    * note: don't need username if using a user crontab
    * logfile in /var/log: either syslog or cron

### ssh 
* serverside: install/enable sshd on a server and open firewall and allow rootlogins
* userside: create a key, get key on remote server (2 ways), login via ssh
