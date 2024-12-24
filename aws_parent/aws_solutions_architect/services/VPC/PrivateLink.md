* essneitally creating a VPC endpoint for your own custom service

* if want to share a single instance/service with another VPC (i.e. offering a customer a product)

* VPC peering would allow ALL instances in one VPC to talk to ALL instances in my VPC 
* NAT/internet GW...public internet has a bunch of problems


* a private link
    * Puts a network interface (ENI) on the consumer's VPC 
    * ENI is associated to a private link endpoing on producer VPC
    * private link endpoint associated with NLB on the producers VPC
    * NLB is associated with the instance(s) providing the service

* service <-> NLB <-> private link endpoint in producer side <producer-consumer> ENI on consumer side <-> consumer 


