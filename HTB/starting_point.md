ping
nmap -sV
    * -sV: Probe open ports to determine service/version info
    * -p: port range
        * -p- => all ports (also -allports)
    * control + v to see progress
    * --min-rate : This is used to specify the minimum number of packets that Nmap should send per second; it speeds up the scan as the number goes highe

telnet { target IP }
    * root
    * port 23


ftp { target IP }
    * anonymous
    * help

SMB
    * server message block
    * default port 445
    * uses NetBIOS over TCP/IP (NBT) for transport, so will see this running as well
    * smbclient (can install via package manager)
    * smbclient -L {target IP}
        * list shares
    * smbclient \\\\{target IP}\\{share name}


redis
    * redis-tools : via package manager
    * info -> get database info, see keyspace section for databases
    * select -> pick a database
    * keys -> view the keys in that database
    * get -> gets the value of a key

RDP
    * 3389 TCP and 3389 UDP
    * get an rdp viewer with: freerdp2-x11 via packagemanger



Mongo
    * curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.4.7.tgz
    * tar xvf mongodb-linux-x86_64-3.4.7.tgz
    * in bin folder:
        * ./mongo mongodb://{target_IP}:27017
    * commands:
        * show dbs;
        * use {database};
        * show collections;
        * dump a value: db.{collection}.find().pretty()

Rsync
    * rsync installed on almost all Linux machines
    * `rsync [OPTION] … [USER@][HOST]::[SRC] [DEST]`
        * SRC - source to copy from
        * DEST - destination to copy from
        * user@ is optional, can omit for an anonymous login
        

    * `rsync --list-only {target ip}::`
    * `rsync --list-only {target ip}::public`
        * paths go after the ::
        * just lists available files instead of copying


* dir busting
    * gobuster
        * run on a url and search a wordlist of paths
        * Web enumeration, specifically directory busting (dir busting), 


    * wordlists
        * sudo apt install wordlists
        * sudo apt install dirb
        * wordlists are located in: /usr/share/wordlists

* Can research ports
Port 135 TCP : https://www.speedguide.net/port.php?port=135
Port 139 TCP : https://www.speedguide.net/port.php?port=139
Port 445 TCP : https://www.speedguide.net/port.php?port=445
Port 3389 TCP : https://www.speedguide.net/port.php?port=3389
Port 5357 TCP : https://www.speedguide.net/port.php?port=5357