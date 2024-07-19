## Network Basics
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

* The primary network configuration files are as follows:
    * /etc/hosts
        The main purpose of this file is to resolve host names that cannot be resolved any other way. It can also be used to resolve host names on small networks with no DNS server. Regardless of the type of network the computer is on, this file should contain a line specifying the IP address of the loopback device (127.0.0.1) as localhost.localdomain. For more information, see the hosts(5) manual page. 
    * /etc/resolv.conf
        This file specifies the IP addresses of DNS servers and the search domain. Unless configured to do otherwise, the network initialization scripts populate this file. For more information about this file, see the resolv.conf(5) manual page. 
    * /etc/sysconfig/network
        This file specifies routing and host information for all network interfaces. It is used to contain directives which are to have global effect and not to be interface specific. For more information about this file and the directives it accepts, see Section D.1.14, “/etc/sysconfig/network”. 
        * can change hostname of machine here
        * restart networking service for to take effect
    * /etc/sysconfig/network-scripts/ifcfg-interface-name
        For each network interface, there is a corresponding interface configuration script. Each of these files provide information specific to a particular network interface. See Section 11.2, “Interface Configuration Files” for more information on this type of file and the directives it accepts. 
    * /etc/nsswitch.conf
        * https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap6sec71.html



## Network management tools

## nmcli
 * Configure IPv4 and IPv6 addresses using `nmcli`

 * Very important: In nmcli, a single network device can typically only be associated with one active connection profile at a time. This behavior is by design and aligns with how network management generally works in Linux systems.


- `nmcli con show --active`
* very important because `nmcli con show` doesn't have a field to show if a conn is active or not

- Enable connection on boot
```bash
nmcli con mod OLD_ACTIVE_CONNECTION connection.autoconnect no     # disable the old connection from starting on reboot 
nmcli con up MY_CONNECTION connection.autoconnect yes # automatically switch to new connection on reboot 
```


  **1. Basic `nmcli` Commands:**
- `nmcli` is a command-line tool for managing NetworkManager and can be used to create, display, edit, delete, activate, and deactivate network connections.

  **2. Viewing Network Connections:**
- List all connections:
```bash
nmcli con show
```
- Display details of a specific connection:
```bash
nmcli con show <connection_name>
```

  **3. Adding a New Connection:**
- Example to add an Ethernet connection with a static IPv4 address:
```bash
nmcli con add type ethernet con-name eth0 ifname eth0 ip4 192.168.1.100/24 gw4 192.168.1.1
nmcli con mod eth0 ipv4.dns "8.8.8.8 8.8.4.4"
nmcli con up eth0
```

  **4. Modifying an Existing Connection:**
- Example to modify an existing connection to use a static IP address:
```bash
nmcli con mod eth0 ipv4.method manual ipv4.addresses "192.168.1.100/24" ipv4.gateway "192.168.1.1"
nmcli con mod eth0 ipv4.dns "8.8.8.8 8.8.4.4"
nmcli con up eth0
```

  **5. Configuring DHCP:**
- To configure a connection to use DHCP for IPv4:
```bash
nmcli con mod eth0 ipv4.method auto
nmcli con up eth0
```

  **6. Configuring IPv6 Addresses:**
- Example to configure a static IPv6 address:
```bash
nmcli con mod eth0 ipv6.method manual ipv6.addresses "2001:db8::1/64" ipv6.gateway "2001:db8::fffe"
nmcli con mod eth0 ipv6.dns "2001:4860:4860::8888 2001:4860:4860::8844"
nmcli con up eth0
```

  **7. Enabling and Disabling Connections:**
- Bring up (activate) a connection:
```bash
nmcli con up eth0
```
- Bring down (deactivate) a connection:
```bash
nmcli con down eth0
```

  **8. Deleting a Connection:**
- Remove a network connection:
```bash
nmcli con delete eth0
```

  **9. Additional Useful Commands:**
- Display device status:
```bash
nmcli dev status
```
- Show device details:
```bash
nmcli dev show eth0
```
- Show active connection details:
```bash
nmcli con show --active
```

  **10. Example Workflow:**
- Add a new Ethernet connection with static IPv4 and IPv6 addresses:
```bash
nmcli con add type ethernet con-name test-eth0 ifname eth0 ip4 192.168.1.100/24 gw4 192.168.1.1
nmcli con mod test-eth0 ipv4.dns "8.8.8.8 8.8.4.4"
nmcli con mod test-eth0 ipv6.method manual ipv6.addresses "2001:db8::1/64" ipv6.gateway "2001:db8::fffe"
nmcli con mod test-eth0 ipv6.dns "2001:4860:4860::8888 2001:4860:4860::8844"
nmcli con up eth0
```

  **11. Verification:**
- Check the connection details to ensure the settings are applied correctly:
```bash
nmcli con show test-eth0
```

By mastering these `nmcli` commands, you can effectively manage network configurations on your Linux system, both for IPv4 and IPv6.




### Can a NIC Have More Than One Interface?

  **1. Understanding Network Interfaces and NICs:**
- A Network Interface Card (NIC) typically has one physical interface.
- However, it can be configured to handle multiple virtual interfaces.

  **2. Virtual Interfaces:**
- Virtual interfaces allow a single NIC to have multiple IP addresses and network configurations.

  **3. Configuring Multiple IP Addresses:**
- You can configure multiple IP addresses on a single NIC using the `ip` command or by editing network configuration files.

  **4. Using the `ip` Command:**
- Add multiple IPv4 addresses to a single NIC:
```bash
ip addr add 192.168.1.100/24 dev eth0
ip addr add 192.168.1.101/24 dev eth0
```
- Add multiple IPv6 addresses:
```bash
ip -6 addr add 2001:db8::1/64 dev eth0
ip -6 addr add 2001:db8::2/64 dev eth0
```

  **5. Editing Network Configuration Files:**
- Example configuration for multiple IPv4 addresses:
```
TYPE=Ethernet
BOOTPROTO=none
NAME=eth0
DEVICE=eth0
ONBOOT=yes
IPADDR0=192.168.1.100
PREFIX0=24
IPADDR1=192.168.1.101
PREFIX1=24
GATEWAY=192.168.1.1
DNS1=8.8.8.8
DNS2=8.8.4.4
```
- Example configuration for multiple IPv6 addresses:
```
TYPE=Ethernet
BOOTPROTO=none
NAME=eth0
DEVICE=eth0
ONBOOT=yes
IPV6ADDR0=2001:db8::1/64
IPV6ADDR1=2001:db8::2/64
IPV6_DEFAULTGW=2001:db8::fffe
DNS1=2001:4860:4860::8888
DNS2=2001:4860:4860::8844
```

  **6. Using Aliases:**
- Configure alias interfaces (eth0:0, eth0:1, etc.) for multiple IP addresses.
- Example for alias interfaces:
```bash
ifconfig eth0:0 192.168.1.100 netmask 255.255.255.0 up
ifconfig eth0:1 192.168.1.101 netmask 255.255.255.0 up
```

  **7. Using NetworkManager (`nmcli`):**
- Example to add multiple IP addresses using `nmcli`:
```bash
nmcli con add type ethernet con-name eth0 ifname eth0 ip4 192.168.1.100/24
nmcli con mod eth0 +ipv4.addresses 192.168.1.101/24
nmcli con up eth0
```

  **8. Summary:**
- A single NIC can indeed handle multiple interfaces through virtual configurations.
- These virtual interfaces can be managed using various tools such as `ip`, `ifconfig`, `nmcli`, and by editing network configuration files.

By utilizing these methods, you can effectively configure a single NIC to handle multiple network interfaces.



### Alias Interfaces with Tools Other Than `ifconfig`

  **1. Using `ip` Command:**
- The `ip` command can also be used to create alias interfaces by adding multiple IP addresses to the same physical interface.
- Example to add an alias interface with IPv4:
```bash
ip addr add 192.168.1.100/24 dev eth0
ip addr add 192.168.1.101/24 dev eth0 label eth0:0
```
- Example to add an alias interface with IPv6:
```bash
ip -6 addr add 2001:db8::1/64 dev eth0
ip -6 addr add 2001:db8::2/64 dev eth0 label eth0:0
```

  **2. Using `nmcli` Command:**
- `nmcli` can be used to add multiple IP addresses, effectively creating alias interfaces.
- Example to add multiple IPv4 addresses:
```bash
nmcli con add type ethernet con-name eth0 ifname eth0 ip4 192.168.1.100/24
nmcli con mod eth0 +ipv4.addresses 192.168.1.101/24
nmcli con up eth0
```
- Example to add multiple IPv6 addresses:
```bash
nmcli con mod eth0 +ipv6.addresses 2001:db8::1/64
nmcli con mod eth0 +ipv6.addresses 2001:db8::2/64
nmcli con up eth0
```

  **3. Editing Network Configuration Files:**
- Alias interfaces can be configured by editing network configuration files directly.
- Example for IPv4 in `/etc/sysconfig/network-scripts/ifcfg-eth0:0`:
```
DEVICE=eth0:0
BOOTPROTO=static
IPADDR=192.168.1.101
NETMASK=255.255.255.0
ONBOOT=yes
```
- Example for IPv6 in `/etc/sysconfig/network-scripts/ifcfg-eth0:0`:
```
DEVICE=eth0:0
BOOTPROTO=static
IPV6ADDR=2001:db8::2/64
ONBOOT=yes
```

  **4. Using `nmtui` Interface:**
- `nmtui` can also be used to configure multiple IP addresses, effectively creating alias interfaces.
- Launch `nmtui` and navigate to 'Edit a connection', then add additional IP addresses under the same connection profile.

  **5. Summary:**
- Alias interfaces can be configured using several tools besides `ifconfig`, such as `ip`, `nmcli`, and by editing network configuration files.
- These methods allow for flexible and versatile network configurations on a single NIC.

By utilizing these tools and methods, you can effectively manage and create alias interfaces on your Linux system.
