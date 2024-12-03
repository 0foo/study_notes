# DNS 

## Set hostname
* `hostnamectl set-hostname SOME-NAME`
    * Can pass blank string: "" to reset hostname to whatever the default is 

* ways to change local hostname
    * hostnamectl set-hostname
    * nmtui
    * edit /etc/hostname
        * note: this works but doesn't change several other needed files as well, prefer the commands

* view hostname
    * hostnamectl status
    * cat /etc/hostname


## Hosts file
* /etc/hosts
    * first column: ip
    * second column: hostname
    * can have a third name with another alias, have to(?) put FQDN in second column


## DNS resolvers
* set DNS resolvers per connection basis
    * NEVER edit /etc/resolve.conf directly as will be overrwritten when restart neworkmanager
    * use nmcli: `nmcli connection modify my-connection ipv4.dns "8.8.8.8 8.8.4.4"`    
    * NetworkManager  stores DNS-resolver info in:
        * config file: /etc/sysconfig/network-scripts
        * then pushes to : /etc/resolv.conf
    * always setup 2 dns servers to use for redundancy
    * to verify a DNS host
        * getent hosts google.com


    * options:
        1. nmtui/nmcli 
        1. /etc/sysconfig/network-scripts
        1. DHCP server can set it on a dynamic DHCP configured interface
            * can ignore this part of DHCP setup with one of these options:
                1. edit ifcfg config file to include PEERDNS=no
                1. nmcli con mod <connection id> ipv4.ignore-auto-dns yes
        1. nmcli con mod <connection id> [+]ipv4.dns <ip of dns>



