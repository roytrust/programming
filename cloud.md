* webnar: https://aws.amazon.com/training/events/
* exam guide
* lab: https://aws.amazon.com/training/self-paced-labs/
* practice: https://aws.amazon.com/certification/certification-prep/
* youtube: https://www.youtube.com/user/AmazonWebServices
* lab: https://aws.amazon.com/training/self-paced-labs/

* across acount auth: STS (Security token service)
* user federation: AWS directory service. Active directory/LDAP
* Cognito


## Concepts
* EC2: Elastic Compute Cloud. Auto scaling: metrics, condition/schedule, cloudwatch.
* Cloud computing: on-demand delivery, pay-as-you-go pricing
* Well-Architectured framework. 5 pillars: operational excellence. secure, reliability, performance efficiency, cost optimization
* Region, availability Zone, data center. Region: legal, proximity, service, cost. Highly available, fault tolent, scale
* Interactive: console, cmd, sdk
* EBS: Elastic block store
* S3: object store. bucket, glacier
* VPC: virtual private cloud. Access Control list
* security group. outbond allowed
* Auto deployment: cloudFormation
* direct connect. Route 53
* serverless: lambda, SNS (Simple notification service), cloudFront, ElasticCache, BeanStalk (conf infra)
* Inspector, Shield
* Cost explorer
* Trust advisor: cost optimization, performance, security, fault tolerance, service limits.
* Container orchestrate: ECS - Elastic Container Service. EKS. Forgate.
* CAF (cloud adoption framework): business, people, governance, platform, security, operations
* Migration strategies: rehost, replatform, refactor/re-architecture, repurchase, retain, retire
* Benefits: trade upfront expense for variable expense, benefits from massive economies of scale, stop guessing capacity, stop spending money running and maintaining data centers, go global in minutes.


* Decouple (loosely coupled): fault tolerance, scalibility (scale up/down, in/out, auto scaling)
* Load balancer: network(high perf, tcm), app (routing)
* EFS: shared storage, multi available zone
* s3 access control: resource - object acl, bucket acl, bucket policy; usser - IAM policy
* Cache. CloudFront: edge location. 
* Operational excellence
* IAM users/groups, roles, federated 
* Network. security group, network ACL.

* Introduction to Amazon S3 Lab
* https://aws.amazon.com/architecture/well-architected/
* Introduction to Amazon EC2 Auto Scaling lab

## Networking
* public/private subnet. Internet gateway - open to public. Virtual Private Gateway - VPN. DirectConnect.
* Network ACL - check packet between subnet, stateless, sender/receiver. Security group - check between instance, stateful.

## Storage & Databases
* EBS
* S3
* EFS
* RDS
* DynamoDB
* Redshit: data warehouse service, big data analytics
* DMS: migration
* ElastiCache: db, memcached/redis.

## Security
* Shared responsibility: AWS - of the could. Customer - in the cloud.
* Policy: allow or deny permissions to services and resources.
* Compliance: Artifact
* DDOS: Shield, WAF (Web app firewall).
* Encryption (data at rest, data at transit). KMS 
* Inspector, GuardDuty



* http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html

* Exam details: https://aws.amazon.com/certification/certified-solutions-architect-associate/
* Training Self-Paced Labs: https://aws.amazon.com/training/self-paced-labs/ 
* Courses: https://aws.amazon.com/training/course-descriptions/ 
* Resources Whitepapers: https://aws.amazon.com/whitepapers/ 
* Architecture Center: https://aws.amazon.com/architecture/ 
* Documentation: https://docs.aws.amazon.com/index.html#lang/en_us







