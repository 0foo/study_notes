
#### Connection
* nmcli
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


#### DNS
* resolvectl status
* sudo resolvectl dns 1.1.1.1 8.8.8.8
* cat /etc/resolv.conf -> managed file
* sudo nano /etc/systemd/resolved.conf  && sudo systemctl restart systemd-resolved
* nmcli connection modify <connection-name> ipv4.dns "<DNS-Server-IP>" #  nmcli connection reload #  systemctl restart NetworkManager
* nmcli con mod test-lab ipv4.dns "8.8.8.8 8.8.4.4"
* nmcli con mod test-lab ipv6.dns "2001:4860:4860::8888 2001:4860:4860::8844"
* nmcli con mod test-lab +ipv4.dns "8.8.8.8 8.8.4.4"
* nmcli connection modify MyWiFiNetwork ipv4.ignore-auto-dns yes
* nmcli connection modify MyWiFiNetwork ipv6.ignore-auto-dns yes
* nmcli connection modify MyWiFiNetwork ipv4.dns "1.1.1.1 8.8.8.8"
* nmcli connection modify MyWiFiNetwork ipv6.dns "2606:4700:4700::1111 2001:4860:4860::8888"
* nmcli connection down MyWiFiNetwork
* nmcli connection up MyWiFiNetwork


#### Hostname
* hostnamectl
* hostname
* /etc/hosts file


#### Connection autostart at boot
* systemctl enable <service>
* nmcli connection modify <connection-name> connection.autoconnect yes

 * https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/networking_guide/sec-configuring_ip_networking_with_nmcli#sec-Adding_and_Configuring_a_Static_Ethernet_Connection_with_nmcli