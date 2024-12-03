## Cron


* crond timer runs every minute
    * has a minute resolution
* default linux tasks that run on crond
    * logrotate

* systemctl status crond -l

* `man 5 crontab `shows cron configuration

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


### Definition
* Minute(0-59) Hour(0-23) Day(1-31) Month (1-12 or jan-dec) DayOfWeek(0-6 or sun-sat)
* Asterisk means EVERY!

* The Cron Job `* 7 * * * /path/to/command` Means:
    * The command will run every minute during the 7 AM hour, every day, regardless of the day of the month or the month of the year.

* ranges
    * can use dash to specify a range
    * for example 0-23 means every hour

* step values
    * Following a range with "/<number>" specifies skips of the number's value through the range.  For example, "0-23/2" can be used in the 'hours' field to specify command execution for every other hour

### Special strings
* Instead of specifying the exact time, you can use special strings:
    * `@reboot`    Run at startup.
    * `@yearly`    Run once a year, i.e., `0 0 1 1 *`.
    * `@annually`  (same as @yearly)
    * `@monthly`   Run once a month, i.e., `0 0 1 * *`.
    * `@weekly`    Run once a week, i.e., `0 0 * * 0`.
    * `@daily`     Run once a day, i.e., `0 0 * * *`.
    * `@midnight`  (same as @daily)
    * `@hourly`    Run once an hour, i.e., `0 * * * *`.


### Test Questions
### Cron Job Definition Test Questions

1. **What time does the following cron job run?**
    * `0 5 * * * /path/to/command`
    * Answer: 5:00 AM every day.

2. **What does the following cron job do?**
    * `30 23 * * 1 /path/to/command`
    * Answer: Runs the command at 11:30 PM every Monday.

3. **When will this cron job execute?**
    * `* 14 * * * /path/to/command`
    * Answer: Every minute during the 2 PM hour every day.

4. **How often does the following cron job run?**
    * `0 */4 * * * /path/to/command`
    * Answer: Every 4 hours at the top of the hour.

5. **Interpret the schedule for this cron job:**
    * `0 0 1 1 * /path/to/command`
    * Answer: At midnight on January 1st every year.

6. **When will this cron job run?**
    * `15 9 * * * /path/to/command`
    * Answer: At 9:15 AM every day.

7. **What is the frequency of this cron job?**
    * `0 22 * * 5 /path/to/command`
    * Answer: At 10:00 PM every Friday.

8. **What does the following cron job do?**
    * `0 8 1 * * /path/to/command`
    * Answer: Runs the command at 8:00 AM on the 1st of every month.

9. **Interpret this cron job schedule:**
    * `*/10 * * * * /path/to/command`
    * Answer: Every 10 minutes.

10. **When will this cron job execute?**
    * `0 6 * * 1-5 /path/to/command`
    * Answer: At 6:00 AM Monday through Friday.

11. **What time does the following cron job run?**
    * `0 0 * * * /path/to/command`
    * Answer: At midnight every day.

12. **When will this cron job run?**
    * `30 6 1 1 * /path/to/command`
    * Answer: At 6:30 AM on January 1st every year.

13. **How often does the following cron job run?**
    * `0 12 15 * * /path/to/command`
    * Answer: At noon on the 15th of every month.

14. **Interpret the schedule for this cron job:**
    * `0 18 * * 0 /path/to/command`
    * Answer: At 6:00 PM every Sunday.

15. **What is the frequency of this cron job?**
    * `0 5 * * 2 /path/to/command`
    * Answer: At 5:00 AM every Tuesday.

16. **When will this cron job run?**
    * `15 14 1 * * /path/to/command`
    * Answer: At 2:15 PM on the 1st of every month.

17. **What does the following cron job do?**
    * `0 22 * * 1-5 /path/to/command`
    * Answer: Runs the command at 10:00 PM Monday through Friday.

18. **Interpret this cron job schedule:**
    * `45 23 * * * /path/to/command`
    * Answer: At 11:45 PM every day.

19. **When will this cron job execute?**
    * `0 7 * * 1-5 /path/to/command`
    * Answer: At 7:00 AM Monday through Friday.

20. **What time does the following cron job run?**
    * `0 3 * * 7 /path/to/command`
    * Answer: At 3:00 AM every Sunday.
