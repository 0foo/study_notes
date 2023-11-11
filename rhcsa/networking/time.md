* Epoch time
    * number of seconds since January 1, 1970 in UTC

* stratum
    * levels of clock authority
    * it's a directed tree going downward from stratum 0 to stratum 15
        * same statum levels can peer with each other
        * downstream stratum can query numerous upstream servers
        * note queries only flows from downstream to up and never in reverse
    * 0: atomic clock, either one sat in a large scale physics laboratory, or those aboard GPS satellites, 
        * the TIME SOURCE
        * not directly connected to internet
    * 1: NTP time servers that get their source of time directly from these stratum 0 atomic clocks
        * i.e. the primary time servers for NTP

### date 

* viewing time
    * date 
        * Shows the current system time in human readable format in currently configured time zone
    * date +%d-%m-%y
        * Shows the current system day of month, month, and year
    * convert timestamp
        * date --date '@1420987251'
        * note the epoch string must start with @ symbol

* setting time
    * date -s 16:03
        * Sets the current time to 3 minutes past 4 p.m.
        * note:this only sets the SOFTWARE time i.e. system time hardware clock is different



### hwclock
* work with the actual hardware clok
* hwclock --systohc: Synchronizes current system time to the hardware clock
* hwclock --hctosys: Synchronizes current hardware time to the system clock


### chronyd

* It obtains measurements (e.g. via the network) of the system's offset relative to other systems, and adjusts the system time accordingly. For isolated systems, the user can periodically enter the correct time by hand (using chronyc). In either case, chronyd determines the rate at which the computer gains or loses time, and compensates for this. 

* /etc/chrony.conf
    * pool section is the ip/dns for the time server pool


### view NTP sources
* chronyc sources
* view /etc/chrony.conf 



### timedatectl
* default no parameters
    
        [root@server1 ~]# timedatectl
        Local time: Mon 2019-06-10 08:27:57 EDT
        Universal time: Mon 2019-06-10 12:27:57 UTC
        RTC time: Mon 2019-06-10 12:27:57
        Time zone: America/New_York (EDT, -0400)
        System clock synchronized: yes
        NTP service: active

* timedatectl status
    * to show current time settings.
* timedatectl list-timezones
    * to show a list of all time zone definitions.
* timedatectl set-timezone Europe/Amsterdam
* timedatectl show
    * a parameterized output of default timedatectl command
* timedatectl set-ntp 1 
    * switch on NTP use
    * it does this via chrony daemon


### set timezone
* 3 ways to set it systemwide:
1. create symlink from timezone file to /etc/localtime
    * ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
    * There's a bunch of timezone files in /usr/share/zoneinfo, one of which just needs to be symlinked to /etc/localtime
1. use tzselect utility, this configures via a menu selection tool
1. use timedatectl

* can set Timezone per user
* Append the line: `TZ='America/Denver'; export TZ` to the file '.profile' in your home directory