* [SaaS vs PaaS vs IaaS](https://www.bmc.com/blogs/saas-vs-paas-vs-iaas-whats-the-difference-and-how-to-choose/)
* [Microsoft Certified: Azure Fundamentals](https://docs.microsoft.com/en-us/learn/certifications/azure-fundamentals/)
* [CAF; Cloud Adoption Framework](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/overview)

### [Cloud benefits and considerations](https://docs.microsoft.com/en-us/learn/modules/fundamental-azure-concepts/benefits-of-cloud-computing)
* High availability
* Scalability
* Elasticity
* Agility
* Geo-distribution
* Disaster recovery

* Lower operating cost
* Run infra more efficiently
* Scale as business needs change
* Limitless pool of raw compute, storage and networking components
* Cognitive services, Analytics services

### Core architectural components
* Management groups, subscriptions, resource groups, resources, resource manager, [management groups](https://docs.microsoft.com/en-us/learn/modules/azure-architecture-fundamentals/management-groups-subscriptions).
* Regions, Availability zones, (Zonal services, Zone-redundant services, Non-regional services), region pairs.
* Subscriptions: billing boundary, access control boundary. Environments, organizational structures, billing, 

### [Azure services](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/tour-of-azure-services)
* Compute
* Networking
* Storage
* Mobile
* Databases
* Web
* IoT (Internet of Things): Hub, Central, Sphere
* Big data
* AI: machine learning, cognitive, bot.
* DevOps services, GitHub (GitHub actions), DevTest Labs.

### [Azure compute services](https://docs.microsoft.com/en-us/learn/modules/azure-compute-fundamentals/overview)
* VMs, container instances, app services, functions (serverless computing)
* VM scale sets: create and manage a group of identical, load-balanced VMs
* Azure Batch: enables large-scale parallel and high-performance computing (HPC) batch jobs with the ability to scale to tens, hundreds, or thousands of VMs.
* VM virtualize hardwares, contrainers virtualize OS. 
* Serverless. Benefits: no infra management, scalability, only pay for what you use. Abstraction of servers, event-driven scale, micro-billing.
* Azure functions (stateless, statefull-Durable functions); logic apps execute workflows that are designed to automate business scenarios and are built from predefined logic blocks.

### [Azure networking services](https://docs.microsoft.com/en-us/learn/modules/azure-networking-fundamentals/azure-virtual-network-fundamentals)
* Isolation and segmentation. Internet communications. 
* Communicate between Azure resources: Virtual networks, service endpoint. 
* Communicate with on-premises resources: Point-to-site / site-site virtual private networks, Azure ExpressRoute. 
* Route network traffic: route tables, border gateway protocol - BGP.  
* Filter network traffic: network security groups, network virtual appliances
* Connect virtual networks: peering, UDR - user-defined routing.
* vnet setting: address space (CIDR classless interdomain routing). 
* VPN Gateway. IKE Internet Key Exchange, IPSec. Policy-based, Route-based.
* **Network security groups (NSG)** can contain multiple inbound and outbound security rules that enable you to filter traffic to and from resources by source and destination IP address, port, and protocol.
* **Private endpoint** – a network interface connected to your virtual network, assigned with a private IP address.
* **Private Link Service** – your own service, powered by Azure Private Link that runs behind an Azure Standard Load Balancer, enabled for Private Link access.
* A **service tag** represents a group of IP address prefixes from a given Azure service.
* **Azure Bastion** - VM inside the VNet, sometimes called a jump box.

### Storage services
* Blob, disk, file
* SAS: Shared Access Signature
* Access tier: hot, cool, archive

### [General security and network security features](https://docs.microsoft.com/en-us/learn/paths/az-900-describe-general-security-network-security-features/)
* Azure Security Center provides visibility of your security posture across all of your services, both on Azure and on-premises.
* Azure Sentinel aggregates security data from many different sources, and provides additional capabilities for threat detection and response.
* Azure Key Vault stores your applications' secrets, such as passwords, encryption keys, and certificates, in a single, central location.
* Azure Dedicated Host provides dedicated physical servers to host your Azure VMs for Windows and Linux.
* 
### Role based access control (RBAC)
* Authorizes users based on their role
* Four elements: security principal, role, scope, role assignments
* Common built-in roles: owner, contributor, reader
* **Azure Active Directory (Azure AD)** for authentication and/or communication between other Azure cloud resources. cloud-based identity and access management service. Authentication: Interactive, Service principal, Azure CLI session, Managed identity
* **Managed Identities**: System-assigned, User-assigned
