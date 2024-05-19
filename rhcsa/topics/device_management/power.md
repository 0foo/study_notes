### Power

* Power off
    * `shutdown` [flags] [now | {time format}] [any message string]
        * like poweroff but gracefully shuts off machine
        * -r  will reboot after shutdown
        * allows a delay string
            * time format can be: +20 to shutdown in 20 min or actual time 05:00
        * message string notifys all users on the system
        * sudo shutdown -r +10 "System upgrade"
        * cancel a scheduled shutdown
            * `sudo shutdown -c "Cancelling reboot"`
    * commands:
        * `systemctl reboot`
        * `reboot`
        * `systemctl halt`
        * `halt`
        * `systemctl poweroff`
        * `poweroff`
        * `shutdown -r now`
        * `init 6`
        * `sudo systemctl start reboot.target`
    * `poweroff` talks to power management on the machine to shutoff power, sends ACPI command
    * `halt` shuts down system without powering off, does not shutoff power
    * `echo b > /proc/sysrq-trigger`




