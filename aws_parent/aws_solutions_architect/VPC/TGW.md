
* Transit Gateway solves these problems 
    * allows edge connectivity for VPC's
    * allows transitivity of VPC's
    * hub and spoke
    * connect a bunch of VPC's, VPN'x, Direct Connects, NAT, Gateways, etc. to centralized Transit Gateway
    * have to define routing tables



* Locations
    * Transit gateway is REGIONAL
    * Can share single TGW cross account using RAM(resource access manager) but only to resources in same region!!
        * Cross-region sharing: TGWs are regional, so sharing is limited to accounts within the same region.

    * For cross region:
        * Can create multiple TGWS in multiple regions and PEER them (non-transitive, requires TGW in ea. region, uses AWS backbone)


* TGW supports IP multicast


* TGW allows transitivity of:
    * NAT GW
    * NLB
    * PrivateLink
    * EFS
    * VPN
    * Direct Connect
    * Internet GW
    * NAT GW
    * Gateway VPC endpoint (s3 and dynamo)
    * more?



Example Scenario:
-------
    Account A has VPCs in us-east-1 and us-west-2.
    Account B also has VPCs in us-east-1 and us-west-2.

For each region:

    Within us-east-1:
        Create a TGW in us-east-1 and share it between the accounts using RAM.
        Attach all us-east-1 VPCs to this TGW.

    Within us-west-2:
        Create another TGW in us-west-2 and share it similarly.

To enable communication between VPCs across us-east-1 and us-west-2, set up TGW Peering between the TGWs in the two regions.




----
* Further info
AWS Transit Gateway supports inter-region peering, enabling seamless connectivity between VPCs and on-premises networks across AWS regions. Here’s an explanation of how Transit Gateway works across regions:
Key Features of Inter-Region Transit Gateway Peering:

    Peering Connections:
        Transit Gateways in different regions can be connected via a peering connection.
        Traffic is routed through the AWS global network backbone, ensuring low latency and high performance.

    High Availability:
        Transit Gateways are regionally redundant and fault-tolerant.
        The inter-region peering connection is also highly available and scales automatically.

    Non-Transitive Routing:
        Like VPC peering, inter-region Transit Gateway peering is non-transitive.
        If you connect Transit Gateway A to Transit Gateway B, and Transit Gateway B to Transit Gateway C, traffic cannot flow from A to C.

    Encrypted Communication:
        All traffic over inter-region peering connections is encrypted using AWS backbone infrastructure.
        No need to configure additional encryption mechanisms.

    No Bandwidth Charges for Peering:
        You pay for data transfer costs (based on inter-region data transfer rates) but there are no separate charges for peering connections.