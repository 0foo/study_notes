## Cron


* crond timer runs every minute
    * has a minute resolution
* default linux tasks that run on crond
    * logrotate

* systemctl status crond -l

* man 5 crontab shows cron configuration


* cron configuratio file is /etc/crontab
    * not to be modified

* to add root user crons, add files (names don't matter) to:
    * /etc/cron.d
    * /etc/cron.hourly, daily, weekly, monthly
        * bash scripts go in this that are executed at this period
        * these periodic cron uses /etc/anacron file for config

* crontab -e
    * crontab -e -u <username>
    * creates a cron file for each user in /var/spool/cron


### vieiwing a list of all cron jobs
* not easy to get a list of all scheduled cron's
* crontab -l 
    * only lists for the current user or specified user or root 

### Cron security
* can limit cron with:
    * /etc/cron.allow
    * /etc/cron.deny
* the user MUST be listed in allow if it exists 
* the user must NOT be listed in deny if it exists
    * cron.deny exists by default
* both files should not exist at the same time
* only root can use cron if neither files exist