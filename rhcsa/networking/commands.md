### ip
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

### Check ports
    * ss
        * ss -ltp
    * netstat
        * netstat -tulpn
    * note: use sudo with these



    * if proc is listening on localhost loopback @ 127.0.0.1 
        * cannot be accessed by machines off network
        * completely on localmachine
    
    * if proc is listening with an local IP/port and the remote/peer is: 0.0.0.0:* it means it doesn't have a connection to a remote host to populate that value



### nmcli/nmtui
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

### network connection config files
    * stored in /etc/sysconfig/network-scripts
    * can modify these files instead of using network config commands
    * after making changes, to make it take effect:
        *  nmcli con up
     