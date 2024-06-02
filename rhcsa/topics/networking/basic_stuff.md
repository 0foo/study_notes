### Network
* ip
    * ip addr : configure/monitor network addresses
    * ip route: configure/monitor routing info
    * ip link: configure/monitor link state
        * ip link show
        * show the link state(a subset of info of ip addr show)
        * ip -s link show
            * can get stats on packets transferred, sent, recieved

    * ip addr show
        * show's current network settings 
    
    * ip addr add
        * add an ip to an interface
        * non-persistent
            * for persistent use nmcli/nmtui

* Check ports
    * ss
        * ss -ltp
    * netstat
        * netstat -tulanep
    * note: use sudo with these

    * if proc is listening on localhost loopback @ 127.0.0.1 
        * cannot be accessed by machines off network
        * completely on localmachine
    
    * if proc is listening with an local IP/port and the remote/peer is: 0.0.0.0:* it means it doesn't have a connection to a remote host to populate that value


* nmcli/nmtui
    * nmcli 
        * nmcli gen permissions
            * lets one check their networking permissions
        * nmcli con show
            * shows all active/inactive sessions
            * note: this is INTERFACE connections NOT tcp/udp connections
        * nmcli con show <cnx name>
            * can view the legend for these settings at: man 5 nm-settings
        * can view device settings
            * nmcli dev show/ nmcli dev show <device name>
        * man nmcli-examples
    * nmtui

* network connection config files
    * stored in /etc/sysconfig/network-scripts
    * can modify these files instead of using network config commands
    * after making changes, to make it take effect:
        *  nmcli con up


### General concepts 

* private addy ranges
    * 172.16.0.0 / 16 
    * 192.168.0.0 / 24
    * 10.0.0.0 / 8


* NAT
    * Private addy's need NAT to communicate off network
    * a socket is an ip:port to ip:port connection
    * single public IP on router that maps a IP:port -> internal private IP:port
    * has a NAT table the keeps track of all of these mappings


* IPV6
    * 128 bit addy's
    * FE80:CD00:0000:0CDE:1257:0000:211E:729C
    * can omit leading zero's and sequences of all zeros and shorten the addy
    * FE80:CD00::CDE:1257::211E:729C


* Network masks
    * show which network a host is on
    * google this if you don't understand it, it involves converting to binary


* MAC address
    * permanant hardware address
    * 12 digits
    * used at layer 2 communication
    * first 6 bytes is vendor id and second 6 bytes is unique node ID


* red hat interface naming consists of parts:
    1. type of interface
        * ethernet = en
        * wan = wl
    2. type of adaptor
        * o = onboard
        * s = hotplug spot
        * p = PCI location
        * x = based on mac address
    3. a number for an index
    * if the above cannot be formulated will use the traditional names like:
        * eth0, eth1, etc.
    * eno16777734
        * means ethernet
        * onboard 
        * index: 16777734
    * note: possible to see interfaces named after bios nnaming system if biosdevname package installed

* loopback interface 
    * used for local networking
    * interface that is only accessible on the local machine
    * also process can use to communicate


* an interface can have both a dynamic address and a static address
    * this is good for having internal static ip and external dynamic ip for accessing yum repo's and internet and whatnot

* networking in redhat managed by NetworkManager
    * sudo systemctl status NetworkManager


* Each Linux network interface has an ifcfg configuration file located in /etc/sysconfig/network-scripts. The device name is added to the end of the filename. So, for example, the configuration file for the first Ethernet interface is called ifcfg-eth0.

    
### Important network files

     The primary network configuration files are as follows:

/etc/hosts
    The main purpose of this file is to resolve host names that cannot be resolved any other way. It can also be used to resolve host names on small networks with no DNS server. Regardless of the type of network the computer is on, this file should contain a line specifying the IP address of the loopback device (127.0.0.1) as localhost.localdomain. For more information, see the hosts(5) manual page. 
/etc/resolv.conf
    This file specifies the IP addresses of DNS servers and the search domain. Unless configured to do otherwise, the network initialization scripts populate this file. For more information about this file, see the resolv.conf(5) manual page. 
/etc/sysconfig/network
    This file specifies routing and host information for all network interfaces. It is used to contain directives which are to have global effect and not to be interface specific. For more information about this file and the directives it accepts, see Section D.1.14, “/etc/sysconfig/network”. 
    * can change hostname of machine here
    * restart networking service for to take effect
/etc/sysconfig/network-scripts/ifcfg-interface-name
    For each network interface, there is a corresponding interface configuration script. Each of these files provide information specific to a particular network interface. See Section 11.2, “Interface Configuration Files” for more information on this type of file and the directives it accepts. 