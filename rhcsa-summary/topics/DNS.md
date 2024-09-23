
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