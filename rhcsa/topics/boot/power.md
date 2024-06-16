### Power

* all power commands are simply aliases of the `systemctl` command in systemd systems


* `shutdown` 
    * `lrwxrwxrwx  1 root root  14 Apr  8 20:51 shutdown -> /bin/systemctl*`
    * flags: `-r : reboot`,  `-h : halt`, `-c : cancel a shutdown`
    * like poweroff but gracefully shuts off machine
    * can pass a time frame in minutes from now i.e. 5 minutes
        * `sudo shutdown +5` 
        * time format can be: +20 to shutdown in 20 min or actual time 05:00
    * -r  will reboot after shutdown
    * shutdown NOW
        * `sudo shutdown -h now`
        * note: pass `-h` explicitly otherwise it will use the default which is not deterministic between different systems
    * allows sending a wall message string notifying all users on the system
    * `sudo shutdown -r +10 "System upgrade"`
    * cancel a scheduled shutdown
        * `sudo shutdown -c "Cancelling reboot"`


* `poweroff` , sends ACPI command
    * `lrwxrwxrwx  1 root root          14 Apr  8 20:51 poweroff -> /bin/systemctl*`
* `halt` shuts down system without powering off, does not shutoff power
    * `lrwxrwxrwx  1 root root          14 Apr  8 20:51 halt -> /bin/systemctl*`

* other power commands:
    * note: most, if not all of these, are simply symlink aliases to systectl
    * `poweroff`
        * talks to power management on the machine to shutoff power
        * send ACPI signal to power off the machine immediately
    * `systemctl reboot`
    * `reboot`
    * `systemctl halt`
    * `halt`
    * `systemctl poweroff`
    * `poweroff`
    * `shutdown -r now`
    * `init 6`
    * `sudo systemctl start reboot.target`
* `echo b > /proc/sysrq-trigger`




* https://unix.stackexchange.com/questions/8690/what-is-the-difference-between-halt-and-shutdown-commands/196471#196471
* https://superuser.com/questions/108704/how-to-shutdown-a-computer-instantly-1-to-5-secs-without-using-a-physical-swit