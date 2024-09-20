### journald
* journalctl

* Flags:
    * -f: Follow new log entries
    * -b: View logs for the current boot
    * -b -1: View logs for a specific boot
    * --since "2023-07-11 10:00:00" --until "2023-07-11 11:00:00": Filter by time
    * -p err: Filter by priority
    * -u sshd.service: Filter by service
    * _UID=1000: Filter by user
    * -r: Show logs in reverse order
    * -n 50: Limit the number of displayed entries
    * > /path/to/output.log: Export logs to a file
    * -k: Show kernel messages
    * _PID=1: Query specific fields
    * --since "15 minutes ago": View system logs from the last 15 minutes
    * -u nginx.service --since "2023-07-11" --until "2023-07-12": Check logs related to a service crash
    * -f -p warn: Monitor logs in real-time with specific priority
    * -x: Show explanations for log entries




### Rsyslogd
* ???

### Journald
* `journalctl`
* `journalctl -f`
* `journalctl -b`
* `journalctl -b -1`
* `journalctl -k`
* `journalctl --since "2023-07-11 10:00:00" --until "2023-07-11 11:00:00"`
* `journalctl --since "15 minutes ago"`
* `journalctl -p err`
* `journalctl -u sshd.service`
* `journalctl _UID=1000`
* `journalctl -n 50`
* `journalctl _PID=1`
* `journalctl -r`
* `journalctl -x`
* `journalctl > /path/to/output.log`
* 
    * `sudo mkdir -p /var/log/journal`
    * `sudo systemctl restart systemd-journald`
* `journalctl -u nginx.service --since "2023-07-11" --until "2023-07-12"`
* `journalctl -b -1`
* `journalctl -f -p warn`


### Audit logs
* `ausearch -a all`
* `ausearch -a event_id`
* `ausearch -a 12345`
* `ausearch -ua uid`
* `ausearch -ua 1000`
* `ausearch -ua username`
* `ausearch -ua alice`
* `ausearch -ts start_time -te end_time`
* `ausearch -ts recent`
* `ausearch -ts 07/01/2024 08:00:00 -te 07/01/2024 17:00:00`
* `ausearch -k key_name`
* `ausearch -k login`
* `ausearch -sc syscall`
* `ausearch -sc execve`
* `ausearch -m message_type`
* `ausearch -m AVC`
* `ausearch -ua username -ts recent -m message_type`
* `ausearch -ua alice -ts recent -m AVC`
