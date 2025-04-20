* AWS Wavelength is a service designed to bring AWS compute and storage resources closer to end-users by running AWS infrastructure at the edge of mobile carrier networks.

* Wavelength Zones are AWS infrastructure deployed directly in the data centers of telecommunication providers (like Verizon, Vodafone, and SK Telecom).

* It's a zone inside of a parent region(AZ)

* These zones are physically closer to mobile devices, reducing the round-trip time for data sent from devices to the application backend.

* By minimizing the distance between users and compute resources, applications can achieve single-digit millisecond latencies.

* Note: It's just a subset of AWS services in these zones that are getting the extremely low latency.
    * AWS Wavelength is designed for low-latency edge use cases, so it only includes the most critical compute, storage, and networking services needed for processing data and handling latency-sensitive workloads.
    * compute: EC2, ECS, EKS
    * storage: EBS
    * networking: VPC, ELB
    * No direct support for RDS, DynamoDB, or Aurora in Wavelength Zones. These can be accessed via the parent AWS region.
    * Services like AWS Lambda, Step Functions, or SageMaker are not available directly in Wavelength Zones.
    * No direct support for Amazon S3 or Glacier in Wavelength Zones, but you can connect to these in the parent region.
    * Services like Amazon Athena, EMR, or Redshift are not natively supported in Wavelength.
    * Applications in Wavelength Zones can connect back to the full suite of AWS services in the parent region, such as databases, analytics, and machine learning services.

* essentially having an AWS zone with AWS service access on the edge of a 5G network
* really low latency for people accessing AWS resources from a 5G network
* traffic never leaves the netw


* because it's 5G use cases are numerous
    * smart cities, connected vehicles, live streams, AR/VR, real time gaming, etc