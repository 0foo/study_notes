### Just know this for the test
* firewall-cmd
* primary commands
    * `sudo firewall-cmd --list-all`
    * `sudo firewall-cmd --add-service=http --permanent --zone=public`



* `sudo firewall-cmd --zone=home --change-interface=eth0`
* `sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent`


## more info:
* https://github.com/jdelgit/rhcsa-notes/blob/master/07.%20Manage%20Basic%20Networking.md#restrict-network-access-using-firewall-cmdfirewall


### basics
* firewalld is a mapping of "network interfaces" to "zones"
* an empty zone is a deny all of all traffic
* add services, ports, rich rules, to allow access

* `sudo firewall-cmd --list-all`

### zones
* default zone is the catchall zone for any interface not specifically mapped to a zone
* `sudo firewall-cmd --get-default-zone`
* `sudo firewall-cmd --set-default-zone=public`
* `sudo firewall-cmd --get-zones`
* `sudo firewall-cmd --get-active-zones`
    * has an interface assigned to it
* `sudo firewall-cmd --zone=public --add-interface=eth0`
    * adds interface to zone


### service
* a service is a file that defines ports that will be opened when adding to a zone
* there's a ton of already defined default services, i.e. ssh, https, http, etc.
* can see these already defined in /usr/lib/firewalld/services
* Can define another one by simply creating a file in this folder and following the dsl of an existing service
    * the filename will be the name of the service
    * will need to reload firewalld configuration: `sudo firewall-cmd --reload`

* example file:
```
<?xml version="1.0" encoding="utf-8"?>
<service>
    <short>MyService</short>
    <description>My custom service</description>
    <port protocol="tcp" port="12345"/>
    <port protocol="udp" port="12345"/>
</service>
```

* `sudo firewall-cmd --get-services`
    * gets all defined zones(each one maps to file as discussed above)
* `sudo firewall-cmd --zone=public --list-services`
* `sudo firewall-cmd --zone=public --add-service=http`
* `sudo firewall-cmd --zone=public --remove-service=http`



### adding a port 
* can add a port outside of a service
* `sudo firewall-cmd --zone=public --add-port=8080/tcp`
* `sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent`


### rich rule
*  allows for more complicated access logic
* `sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.1.100" service name="http" accept'`
* `sudo firewall-cmd --zone=public --remove-rich-rule='rule family="ipv4" source address="192.168.1.100" service name="http" accept'`



### source
* can limit access to an ip or range of ips by adding a source to a zone
* `sudo firewall-cmd --zone=home --add-source=192.168.1.0/24`

### permanance
* will need to specifically declare a command as permanant or when reboot the modifications will be lost
* permanant vs non-permanant
    * `sudo firewall-cmd --zone=public --add-service=http`  
    * `sudo firewall-cmd --zone=public --add-service=http --permanent`
* can bulk make all non permanant rules permanant
    * `sudo firewall-cmd --runtime-to-permanent`
