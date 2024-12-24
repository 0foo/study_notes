#### NAT gateway
* Attached to SUBNET (not entire VPC)
* Always attached via managed ENI(therefore: can monitor via via flow logs)
* will see inbound traffic on the NAT public IP (if SG and NACL allows) but that's the demarcation and it's dropped there

#### Traffic restriction

Outbound Traffic to the Internet:
A NAT Gateway is designed to allow instances in a private subnet to initiate outbound connections to the internet or other AWS services. This is its primary use case.

Inbound Traffic Restrictions:

    NAT Gateways block inbound traffic initiated from the internet.
    Even if there is a public IP address associated with the NAT Gateway, it will not accept unsolicited inbound connections.

NAT Gateways are stateful. This means they will allow return traffic for connections that were initiated by instances in the private subnet.

#### NATGW is 1:N NAT model

AWS NAT Gateway aligns with the 1:N NAT model:

    One Elastic IP Address (EIP):
    The NAT Gateway uses a single public IP (or more in High Availability setups) to handle outbound traffic from multiple private IP addresses in a private subnet.

    Port Translation:
    NAT Gateway dynamically maps each outbound connection from a private IP to a unique combination of the public IP and a port number.

    Return Traffic:
    The NAT Gateway tracks the state of outbound connections and allows return traffic based on these mappings.



#### NAT Theory
Yes, you're describing the two main types of NAT (Network Address Translation) configurations: 1:1 NAT and 1:N (or many-to-one) NAT. These are common in networking scenarios and are relevant to how NAT is implemented in various environments, including AWS.
1:1 NAT (Static NAT or One-to-One Mapping)

    How It Works:
    Each private IP address is mapped to a unique public IP address. This is a direct, one-to-one relationship between internal and external IPs.
    Use Case:
        Scenarios where a consistent public IP is needed for a specific internal resource (e.g., hosting a service that requires the same IP for client access or whitelisting).
        Typically used in setups where there are enough public IPs available for each internal device requiring external access.
    Example in AWS:
    Not directly supported by AWS NAT Gateway, but it can be achieved with an Elastic IP (EIP) and routing rules for specific instances.

1:N NAT (Dynamic NAT or Many-to-One Mapping)

    How It Works:
    A single public IP address is shared among multiple private IP addresses. The NAT device differentiates traffic by dynamically assigning a unique port number to each connection.
    Use Case:
        Most common for internet access in private networks (e.g., home routers, enterprise networks, AWS NAT Gateway).
        Optimizes the use of public IPs by allowing many private devices to access the internet using one or a few public IPs.
    Example in AWS:
    The AWS NAT Gateway operates in a 1:N model, using a single Elastic IP address to manage traffic for multiple private subnet resources.


