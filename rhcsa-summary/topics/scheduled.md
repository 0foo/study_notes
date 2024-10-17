
### Essentials/tips

* cron
    * cat /etc/crontab for cron formatting
    * don't need username for non-root jobs as they're already run by a user
    * view files in /etc/cron.* for examples
    * crontab


### Cron
* `crontab -l`
* `crontab -e`
* `crontab -r`
* `crontab -l -u username`
* `crontab -e -u username`
* `crontab -r -u username`
* `cat /etc/crontab`
* `ls /etc/cron.d`
* `man 5 crontab` shows cron configuration

* crontab -e
    * <time> <script-path>
    * Edit user-specific cron

* user vs root crontabs
    * crontab -u <user> -e
    * crontab -l / sudo crontab -l

```
/etc/
 ├── cron.d  
 ├── cron.daily  
 ├── cron.deny  
 ├── cron.hourly   
 ├── cron.monthly  
 ├── crontab 
 └── cron.weekly

```

* reading cron configuraion
    * do a `man /etc/crontab` to get a printout of all the cron settings
    * the key to remember is that * asterisk is every single item in that period
    * so by adding a number you will limit/filter the periodicity


### At

### at
*  at <runtime> at> <command-to-run> at> <EOT>
*  at <time> -f <script-filename>
* atq
* atrm <#job>

s

* `at 5:00 PM`
* `at 4:00 PM + 3 days` (run at 4pm 3 days from now)
* `atq`
    * gives job list
* `atrm job_number`
    * remove item from job list
* `at -c job_number`
    * display what the
* `at now + 1 minute`
* use ctrl + D to exit!!!









### Side notes: not on rhcsa
* anacron
    * Anacron, which is a service used to schedule periodic tasks on systems that are not always running (such as laptops). Unlike cron, which expects the system to be running continuously, Anacron is designed to ensure that scheduled tasks still get executed even if the system was powered off or suspended when the task was supposed to run.












### Cron test
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
