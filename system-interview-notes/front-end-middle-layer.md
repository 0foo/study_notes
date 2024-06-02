**<span style="text-decoration:underline;">Large Scale System Architecture</span>**



* <span style="text-decoration:underline;">Process to go through</span>
1. User Requirements
    1. Functional Requirements: what the service does for the user
2. Figure out Technical requirements
    2. Back of napkin calculations-how many users, files, how much resources needed
    3. QPS, Storage, Bandwith, Memory(cache)
        1. Example:
            1. Let’s assume we have 300M total users, with 1M daily active users. 2M new photos every day, 23 new photos every second.
            2. Average photo file size => 200KB
            3. Total space required for 1 day of photos = 2M * 200KB
        2. 500M new URL shortenings per month, with 100:1 read/write ratio, we can expect 50B redirections during the same period:
            4. What would be Queries Per Second (QPS) for our system? New URLs shortenings per second:
                1. 500 million / (30 days * 24 hours * 3600 seconds) = ~200 URLs/s
            5. Considering 100:1 read/write ratio, URLs redirections per second will be:
                2. 100 * 200 URLs/s = 20K/s
    4. RCLASPS: redundancy, caching, load balancing, availability, scaling, partitioning, storage
    5. predicts resource requirements i.e. mem, cpu, network, disk
    6. Can do this with storage, bandwidth, connection pools etc.
3. Sketch out rough high level overview of components
4. Identify potential bottlenecks/tradeoffs
    7. single points of failure
    8. no autoscaling in certain areas of the app
    9. etc.
5. Monitoring/Alerts

----------------------------------



* (optional) can sketch out high level data relationships
    10. Entities/Relationships: User, Tweet,  User &lt;-> Tweet, User &lt;-> User

<span style="text-decoration:underline;">Distributed system theories</span>



* CAP theorem:
    * when something is partitioned: i.e. a communications break occurs between replicas you have two options, 
        * be Available and serve stale data until partition is fixed
        * be Consistent and not return anything until partition is fixed
    * [http://blog.thislongrun.com/2015/03/the-cap-theorem-series.html](http://blog.thislongrun.com/2015/03/the-cap-theorem-series.html)
    * ACID (Atomicity, Consistency, Isolation, Durability) databases chose consistency
        * ACID are therefore CP systems
    * BASE (Basically Available, Soft-state, Eventually consistent) databases chose availability (respond with local data without ensuring it is the latest with its peers).
        * BASE are therefore AP systems
* PAC-ELC
    * extension to the CAP theorem
    *  Based on the idea that: As soon as a distributed system replicates data, a trade-off between consistency and latency arises EVEN if operating normally.
    * PAC = CAP (same as CAP)
    * ELC means else latency consistency
    * system operation divided into two modes — 
        * ELC: operation without partitioning- i.e. operating normally
            *  one must choose between reduced response time and consistency.
            * it still takes time to update replicas which add latency
        * PAC: operation with partitioning - broken communications
            * one must choose between availability and consistency, 
    * even when the system is running normally in the absence of partitions, the system has to tradeoff between latency (‘L’) and consistency (‘C’).
    *  high availability requirement implies that the system must replicate data.
* 12 factor App: 
    * 12 software development ideas when developing a software
    * [https://12factor.net/](https://12factor.net/)
* 3 tier app
    * typically the starting core of any web application
* defined by 3 layers
    * presentation tier
        * views/UI
    * application tier
        * Holds biz logic
    * data storage tier
        * Holds ALL of the state
* Presentation and application should hold no state and should be able to be killed or horizontally scaled effortlessly with no state issues

<span style="text-decoration:underline;">Redundancy vs Replication</span>



* Redundancy is a duplication of components, Replication is a duplication of data
* [Redundancy](https://en.wikipedia.org/wiki/Redundancy_(engineering)) is the duplication of critical components or functions of a system with the intention of increasing the reliability of the system
    * if one fails can failover to the other
* [Replication](https://en.wikipedia.org/wiki/Replication_(computing)) means sharing information to ensure consistency between redundant resources, such as software or hardware components, to improve reliability, [fault-tolerance](https://en.wikipedia.org/wiki/Fault_tolerance), or accessibility.

<span style="text-decoration:underline;">Constraints</span>



* Server resource limits
    * CPU, Memory, etc
* Connection pools/limits
    * number per second
    * duration of requests
* Network
* Storage
* System Failure
* Lost Data

<span style="text-decoration:underline;">Solutions</span>



* load balancing/autoscaling
    * scale vertically and horizontally
    * solves most of the above problems as it distributes the load 
* Partitioning
    * Split up servers into different use groups
        * i.e. read group and a write group
        * balances the connection pools and load
        * allows to optimize architecture for different uses
    * Can partition the data into different servers
        * various partitions strategies as discussed later
* System Failure/Lost Data:
    * database: 
        * redundancy
        * failover
        * replicas
    * web servers
        * auto-scaling
        * stateless
        * load balancing
    * types:
        * redundancy
        * failover
        * replicas
        * auto-scaling
        * stateless
        * load balancing
    * **Availability zone** distribution to avoid large scale disasters

<span style="text-decoration:underline;">Heartbeat</span>



* In decentralized system, servers check in with other servers to validate that they’re still alive and working
* Typically a unique heartbeat endpoint
* If no heartbeat the check in server can take corrective actions
* What value should we choose for a quorum? More than half of the number of nodes in the cluster: (N/2) + 1  where N is the total number of nodes in the cluster
    * Note: odd and even both require the same 
* _R_+_W_>_N \
 \
_

<span style="text-decoration:underline;">Quorum</span>



* the minimum number of servers on which a distributed operation needs to be performed successfully before declaring the operation’s overall success.
* Quorum enforces the consistency requirement needed for distributed operations.

<span style="text-decoration:underline;">Data Encoding</span>



* Hashing/Encryption
* hashing: SHA(1,256,512), MD5
* encryption: RSA, AES, Blowfish
* Encryption-cipher the data and it’s recoverable
* Hash-generate a key that matches that data uniquely
* Checksum
    * since the string is unique to the data can verify data integrity by calculating a hash and checking it matches the original source’s hash
* Base Encoding of Data
* Base64, Base8
* Uses:
    * can s
* Character encoding
    * Ascii, Unicode

<span style="text-decoration:underline;">Proxies</span>



* Proxy server is an intermediate server between the client and the back-end server and acts as an intermediary for requests from clients seeking resources from other servers.
* Examples of uses:
    *  filter requests
    * log requests
    *  transform requests (by adding/removing headers, encrypting/decrypting, or compressing a resource).
    * caching 
    * hide identity
* Reverse Proxy
    * in front of a server
    * Masks server 
    * Bastion Host or Load Balancer
* Forward Proxy
    * in front of a client
    * masks the client
    * VPN

<span style="text-decoration:underline;">Load Balancer</span>



* Can exist at all levels of the 3 tier architecture
    * front end LB, Application LB, storage tier
* Types of load distribution
    * Round Robin - one packet per server in round robin approach
    * Server Load -  maintain all servers with equal resource usage
        * LB needs to query servers for load periodically	
    * additional TBI
* Application Load balancer
    * ‘smart’ load balancer
    * can look at http packet and make decisions
    * can handle a ton of RPS but not as many as the TCP/Network LB
* DNS load balancer
    * use for enormous sites
    * note: this gives no feedback for services going down!
    * can adjust the TTL but then you get continued repeated requests to DNS servers and switch the load balancing problem there
    * can terminate SSL here
* TCP(Network) load balancer
    * only sees layer 4 packets, does not inspect http at layer 7
    * FAST and HANDLE virtually unlimited connections
    * number of connections not a limit
    * For load balancer the number of TCP connections is not **_THE_** limiting factor: that limit is so high that you'll hit other limitations of your environment before you hit that one. For example, if your load balancer is handling SSL encryption for your environment you'll probably hit a CPU/RAM limitation from that before you hit the TCP connections limit.

<span style="text-decoration:underline;">Security and Permissions</span>



* secure at rest AND secure in transit
* ssl

<span style="text-decoration:underline;">Ajax vs Long Poll vs Web Socket</span>



* Ajax
    * The basic idea is that the client repeatedly polls (or requests) a server for data.The client makes a request and waits for the server to respond with data. If no data is available, an empty response is returned.
    * Alot of overhead as there’s a lot of empty responses
* Long Poll
    * BASICALLY keeping the TCP request open for long period of time
    *  allows the server to push information to a client whenever the data is available.
    *  the client requests information from the server exactly as in normal polling, but with the expectation that the server may not respond immediately. 
    * If the server does not have any data available for the client, instead of sending an empty response, the server holds the request and waits until some data becomes available.
    * The client then immediately re-request information from the server so that the server will almost always have an available waiting request 
* Web Socket
    * WebSocket provides [Full duplex](https://en.wikipedia.org/wiki/Duplex_(telecommunications)#Full_duplex) communication channels over a single TCP connection. It provides a persistent connection between a client and a server that both parties can use to start sending data at any time.

<span style="text-decoration:underline;">References:</span>



* educative.io/courses/grokking-the-system-design-interview/m2G48X18NDO
* [https://github.com/donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)
* [https://github.com/shashank88/system_design](https://github.com/shashank88/system_design)
* [https://tianpan.co/notes/2016-02-13-crack-the-system-design-interview](https://tianpan.co/notes/2016-02-13-crack-the-system-design-interview)

<span style="text-decoration:underline;">Questions</span>



* You will be shown several architecture diagrams and asked various questions, like "what happens when database X goes down?", or "How to speed up requests from service Y?". Caching plays a big role in almost all responses.
* facebook asked me design to reboot the world.. i.e. push an update to every machine in a 10,000 node cluster and reboot it in the new update with zero downtime
* for linked in, a guy on my team interviewed me, I'll be sitting right behind him, it was design an image sharing system that also can support video (like vine)
* Scale a ride-hailing application so that it handles ~10,000 requests/minute. This was a 1.5-hour-long discussion with follow-ups, including Consistent Hashing. They also challenged multiple of my design claims which I had to think about on the spot.