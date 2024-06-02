### DNS 
* hostnamectl
    * set-hostname
    * View hostname

* change local hostname
    * nmtui
    * hostnamectl set-hostname
    * edit /etc/hostname

* view hostname
    * hostnamectl status
    * cat /etc/hostname

* /etc/hosts
    * first column: ip
    * second column: hostname
    * can have a third name with another alias, have to(?) put FQDN in second column

* set DNS resolvers
    * options:
        1. nmtui/nmcli 
        1. /etc/sysconfig/network-scripts
        1. DHCP server can set it on a dynamic DHCP configured interface
            * can ignore this part of DHCP setup with one of these options:
                1. edit ifcfg config file to include PEERDNS=no
                1. nmcli con mod <connection id> ipv4.ignore-auto-dns yes
        1. nmcli con mod <connection id> [+]ipv4.dns <ip of dns>

    * NetworkManager  stores DNS-resolver info in:
        * config file: /etc/sysconfig/network-scripts
        * then pushes to : /etc/resolv.conf
        * NEVER edit /etc/resolve.conf directly as will be overrwritten when restart neworkmanager
    * always setup 2 dns servers to use for redundancy
    * to verify a DNS host
        * getent hosts google.com