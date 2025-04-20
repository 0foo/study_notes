* IAM Role:
    * An IAM role is an identity within AWS that provides permissions for accessing AWS services.
    * It contains a set of permissions defined by policies (e.g., S3 access, DynamoDB access).
    * When an EC2 instance profile is used, the IAM role is assumed by the instance.

* EC2 instance profile
    * An instance profile is essentially a container for the IAM role.
    * You create an instance profile and attach the IAM role to it.
    * The profile is then associated with an EC2 instance, enabling applications running on the instance to use the role's permissions.