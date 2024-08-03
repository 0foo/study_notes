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

### At
* `at 5:00 PM`
* `atq`
* `atrm job_number`
* `at -c job_number`
* `at now + 1 minute`


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
