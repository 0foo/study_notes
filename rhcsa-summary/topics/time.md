### Time

* timedatectl
    * Display system time
    * doesn't interact with NTP servers directly, needs an NTP daemon for NTP

    * `tzselect` to help figure out what timezone!!
    * `list|set timezone`
        * timedatectl list-timezones
        * timedatectl set-timezone
        * this changes the symlinked file at /etc/localtime
        * can do this manually as well

    * manually set time
        * `timedatectl set-time "YYYY-MM-DD hh:mm:ss"`
        * `timedatectl set-time "hh:mm:ss"`

    * turn ntp on or off
        * timedatectl set-ntp 1 or timedatectl set-ntp true
            * switch on/off NTP use


* chrony 
    * chronyd
    * chronyc sources -v (to check the sources Chrony is using)
    * chronyc tracking 

    * add servers to chrony.conf file
    ```
    /etc/chrony.conf
    server ntp1.example.com iburst
    server ntp2.example.com iburst
    ```
    * restart chronyd if you change the config file


-----------------------
### not on rhcsa

* systemd-timesyncd
    * simple build in systemd program for NTP
    * config file
    * * `/etc/systemd/timesyncd.conf`
    * force ntp update by restarting systemd service
        * `sudo systemctl restart systemd-timesyncd`



* ntp
    * install with dnf
    * start with systemd: ntpd
    * add to /etc/ntp.conf file
    ```
    server ntp1.example.com iburst
    server ntp2.example.com iburst
    ```
* don't forget to add to firewall
sudo firewall-cmd --add-service=ntp --permanent
sudo firewall-cmd --reload
