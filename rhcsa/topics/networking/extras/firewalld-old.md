## Firewalld


* Zones
    * a cluster of settings that get's applied to an interface
    * includes ports, icmp blocking, etc
    * can define a custom zone
    * pre-defined zones exist as well
    * can match different zones to different interfaces

    * view all zones
        * firewall-cmd --get-zones
        * this is all available zones whether in use or not
        
    * see default zone
        * firewall-cmd --get-default-zone
        * the active zone if no other zone is configured as active
    
    * get all active zones
        * firewall-cmd --get-active-zones
        * all zones applied to an interface
    
    * get all info about a particular zone including services etc.
        * firewall-cmd --zone=home --list-all
            * if omit --zone parameter will get this info about default zones
                * sudo firewall-cmd --list-all
        * This is essentially the current configuration of the firewall
        * can add --permanant to find out if there's a diff from any services set with permanance and firewall hasn't been rebooted yet
        
    * get all info about all zones
        * sudo firewall-cmd --list-all-zones
        
    * change default zone
        * firewall-cmd --set-default-zone=home
        * note: this will also change any interface using the default zone to the new zone
    
    * apply interface to a zone
        *  sudo firewall-cmd --zone=home --change-interface=eth0
        * --remove-interfae 
            * will remove the interface from the specified zone
    * create new zone
        * firewall-cmd --permanent --new-zone=publicweb
        


* Services
    * the actual port to service name mapping
    * defined in files
        * the filename minus the xml is the service name used in firewall-cmd commands
        * /usr/lib/firewalld/services
            * default system pre-installed services
        * /etc/firewalld/services
            * custom user defined services
    * view services
        * firewall-cmd --get-services
            * all services that exist on the host that you can add to your firewall...even if not active or in a zone
        * firewall-cmd --zone=public --list-services
            * lists all services available in the currently active zone(s)
            * zone specific
            * leave out the --zone flag to view default zone info
        * view permanant services, note these may differ from result without permanant
            * firewall-cmd --zone=public --list-services --permanant
    * add/remove a service to a zone
        *  firewall-cmd --zone=public --add-service=http
            * can always leave out the --zone flag to apply the change to the default zone
        * --remove-service to remove
    


* Rule permanance
    * rules when added via firewall-cmd are not permanant unless
        * using --permanant flag
            * this is on a per command basis
        * --runtime-to-permanent
            * this sets any/all settings that are currently configured to be configured
    * must reload after typing --permanant flag to set permanant , must STILL reboot
        * firewall-cmd --reload 

    * sudo firewall-cmd --reload


* Add a port not connected to a service
    * sudo firewall-cmd --zone=public --add-port=5000/tcp
        * can use /tcp or /udp
        * can specify a range of ports: 
            *  --add-port=4990-4999/udp
    * verify this port added in either of these two ways:
        * sudo firewall-cmd --zone=public --list-ports
        * sudo firewall-cmd --zone=public --list-all




### firewall-cmd extras

* check state
    * sudo firewall-cmd --state





### Further reading
* https://docs.rockylinux.org/guides/security/firewalld-beginners/