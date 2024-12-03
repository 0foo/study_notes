### Know
* `hostnamectl`
* `/etc/hosts`
* `/etc/resolv.conf`
* `nmcli connection modify my_network ipv4.dns "1.1.1.1 8.8.8.8" ipv4.ignore-auto-dns yes`


#### DNS
* cat `/etc/resolv.conf  `
    * managed file
    * NEVER EDIT DIRECTLY!


* `nmcli connection modify <connection-name> ipv4.dns "<DNS-Server-IP>"  `
    * `nmcli connection reload`
    * `systemctl restart`

NetworkManager
* nmcli con mod test-lab ipv4.dns "8.8.8.8 8.8.4.4"
* nmcli connection modify MyWiFiNetwork ipv4.ignore-auto-dns yes
* nmcli con mod test-lab ipv6.dns "2001:4860:4860::8888 2001:4860:4860::8844"
* nmcli connection modify MyWiFiNetwork ipv6.ignore-auto-dns yes
* can use + or -
    * nmcli con mod test-lab +ipv4.dns "8.8.8.8 8.8.4.4"
* nmcli connection down MyWiFiNetwork
* nmcli connection up MyWiFiNetwork


#### Hostname
* hostnamectl
* hostname
* /etc/hosts file


### Resolvectl
* not on RHCSA
* alternative DNS manager to nmcli
* have to edit 
* `resolvectl status`
* `sudo resolvectl dns 1.1.1.1 8.8.8.8`
* sudo nano /etc/systemd/resolved.conf  && sudo systemctl restart systemd-resolved
