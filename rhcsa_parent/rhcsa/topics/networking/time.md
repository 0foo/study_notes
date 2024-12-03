* Epoch time
    * number of seconds since January 1, 1970 in UTC

### Basic time

* timedatectl
    * set-time
    * list-timezones
    * set-timezone
    * Display system time

* date
    * --set
    * View system date


### NTP
* Series of time servers around the world

* arranged in a stratum
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



### timesyncd
* systemd time date service
* lightweight NTP client that is part of the systemd suite of system management tools. It is designed to provide basic time synchronization capabilities for Linux systems.
* `/etc/systemd/timesyncd.conf`


* `timedatectl`
```
nick ~/projects/study_notes (master) : timedatectl status
Local time: Fri 2024-05-17 15:29:32 CDT
Universal time: Fri 2024-05-17 20:29:32 UTC
RTC time: Fri 2024-05-17 20:29:32
Time zone: America/Chicago (CDT, -0500)
System clock synchronized: yes
NTP service: active
RTC in local TZ: no
```

* timedatectl status
    * to show current time settings.
* timedatectl list-timezones
    * to show a list of all time zone definitions.
* timedatectl set-timezone Europe/Amsterdam
* timedatectl show
    * a parameterized output of default timedatectl command
* timedatectl set-ntp 1 or sudo timedatectl set-ntp true
    * switch on NTP use
    * it does this via chrony daemon
* force ntp update by restarting systemd service
    * `sudo systemctl restart systemd-timesyncd`


### chronyd
* A daemon (chronyd) for network time synchronization.
* Provides high accuracy timekeeping in a variety of network environments.
* Suitable for systems that are frequently disconnected or have unreliable networks, Can correct large clock skews quickly.
* Includes tools like chronyc for monitoring and controlling the chrony daemon.
* It obtains measurements (e.g. via the network) of the system's offset relative to other systems, and adjusts the system time accordingly. For isolated systems, the user can periodically enter the correct time by hand (using chronyc). In either case, chronyd determines the rate at which the computer gains or loses time, and compensates for this. 
* can use host with chronyd as a local network time server to sync servers on network
    * good for security, performance, reliability/uptime, etc.

* /etc/chrony.conf
    * pool section is the ip/dns for the time server pool
    * server [hostname]: Specifies NTP servers to synchronize with.
    * driftfile [path]: Specifies the location of the file where chrony records the system clock's drift.
    * makestep [threshold] [limit]: Allows chrony to step the system clock if the adjustment is larger than the specified threshold during the first limit updates.
    * rtcsync: Enables synchronization between the system clock and the Real-Time Clock (RTC).
    * allow [subnet]: Allows NTP clients from the specified subnet to query the chrony server.
    * local stratum [number]: Configures chrony as a local NTP server with a specified stratum level.
    * logdir [path]: Specifies the directory where chrony stores log files.
        * log measurements statistics tracking: Enables logging of measurements, statistics, and tracking information.

```
server time.example.com iburst
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
allow 192.168.0.0/24
local stratum 10
logdir /var/log/chrony
log measurements statistics tracking
```

### NTPD

* `sudo apt install ntp`

/etc/ntp.conf
```
# Use public servers from the pool.ntp.org project.
server 0.pool.ntp.org iburst
server 1.pool.ntp.org iburst
server 2.pool.ntp.org iburst
server 3.pool.ntp.org iburst

# Drift file.
driftfile /var/lib/ntp/drift

# Access control restrictions.
restrict default kod nomodify notrap nopeer noquery
restrict 127.0.0.1
restrict ::1

# Enable logging.
logfile /var/log/ntp.log

```
* iburst option allows faster synchronization on initial start.



### Check system sync with NTP
1.  `ntpq`
* Use ntpq -p to see a list of NTP peers and their synchronization status.
* Look for a * next to one of the servers in the output. This indicates the server your system is currently synchronized with.

2. ntpstat
* install it with apt
```
nick ~/projects/study_notes/rhcsa (master) : ntpstat
synchronised to NTP server (65.100.46.166) at stratum 2 
   time correct to within 48 ms
   polling server every 64 s

```
3. `chronyc tracking`
4. `timedatectl status`



### drift file
Drift File
    * A file used by NTP daemons (ntpd, chronyd, etc.) to store the estimated frequency error of the system clock.
    * Helps the NTP daemon to adjust the system clock more accurately by accounting for the natural drift of the hardware clock.
    * Typically located at /var/lib/ntp/drift for ntpd and /var/lib/chrony/drift for chronyd.
    * When the NTP daemon is running, it periodically updates the drift file with the current estimate of the clock's frequency error.
    * On startup, the NTP daemon reads the drift file to get the last known frequency error estimate and uses this information to adjust the system clock more accurately.



### date command
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
* work with the actual hardware clock
* hwclock --systohc: Synchronizes current system time to the hardware clock
* hwclock --hctosys: Synchronizes current hardware time to the system clock

* To setup hwclock to NTP time you have to:
    1. ensure an ntp daemon running and working on system(timedated, chronyd, ntpd)
    3. sync SYSTEM time to NTP (see check system sync with NTP to ensure it's syncing)
    4. sync hardware clock time to systemtime with `hwclock --systohc` command

### set timezone
* 3 ways to set it systemwide:
1. create symlink from timezone file to /etc/localtime
    * ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
    * There's a bunch of timezone files in /usr/share/zoneinfo, one of which just needs to be symlinked to /etc/localtime
1. use tzselect utility, this configures via a menu selection tool
1. use timedatectl

* can set Timezone per user
* Append the line: `TZ='America/Denver'; export TZ` to the file '.profile' in your home directory


