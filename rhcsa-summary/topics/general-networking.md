## Important note:

* on test type `nmcli con show` and then hit tab twice to see all the top level options
* can type an option then hit tab twice and get the suboptions


#### General info
* `traceroute`, `ping`, `ip route`, `host`

#### DNS
* `/etc/hosts`, `/etc/resolv.conf`, `host`, `hostname`, `hostnamectl`, `nmcli con mod ipv4.dns`

#### Connection
* `/etc/sysconfig/network-scripts/ifcfg-name`
* nmcli
* nmcli general reload
* nmcli device status
* nmcli device show
* sudo nmcli -p connection show SETUP-6860    (p is for pretty print/ t is for terse)
* nmcli con show
* nmcli con add
* nmcli con delete
* nmcli connection add <connection-name> ifname <interface> type <ethernet/wireless>  ipv4 <IP address>/24 gw4 <GatewayIP>
* nmcli connection up/down <connection-name>
* nmcli connection modify
    * very important: after modify, have to bring connection down then back up again to activate new settings
* nmcli connection modify <connection-name> ipv4.method manual 
* nmcli connection modify <connection_name> ipv4.addresses <ip_address>/<prefix>
* nmcli connection modify <connection_name> ipv4.gateway <gateway>
* nmcli connection modify <connection_name> ipv4.dns <dns_servers>
* nmcli connection modify <connection_name> ipv4.method manual
* nmcli connection down MyWiFiNetwork
* nmcli connection up MyWiFiNetwork
* nmcli 
    * connection [ show | up | up <connection name> | down <connection name> ]
    * device [ status | show | show <device>  | delete ]
* create new connection:
    * nmcli connection add  con-name <connection-name> ifname <interface> type <ethernet/wireless>  
* Use ipv6 and gw6 if configuring IPv6 otherwise same command
* nmcli connection modify <connection-name> <setting> <value> 
    * then take it down and up again!
* disable dhcp: nmcli connection modify <connection-name> ipv4.method manual 

* make a connection autoconnect when it detects
    * nmcli connection modify <connection-name> connection.autoconnect yes

* con create
    * con-name
    * ifname
    * type
    * ipv4.method
    * ipv4.address

### Man
* can use man cli and search(/) for examples


#### Connection autostart at boot
* systemctl enable <service>
* nmcli connection modify <connection-name> connection.autoconnect yes

 * https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/networking_guide/sec-configuring_ip_networking_with_nmcli#sec-Adding_and_Configuring_a_Static_Ethernet_Connection_with_nmcli