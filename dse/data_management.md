## Fundamental
### Data Monetize
* Pricing strategies: cost pricing and value pricing
* Value pricing: value of the data from a customer's perspective: 
  * uniqueness
  * the level of difficulty required to obtain the data
  * How many competitors already offer the same data
  * How frequently the data is updated and the amount of historical data
  * Scope: global rather than local
  * Sell as a set or as a subscription
  * Charge based on usage
* Freemium pricing structure: limited amount for free, basic charge for standard access, premium charge for additional service features

## Snowflake
* [Architecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts.html)
* Zero-copy cloning
* Time travel, fail safe, data masking, INFORMATION_SCHEMA, ACCOUNT_USAGE
* Caches: query result, virtual warehouse, metadata
* Tables: permanent, transient, hybrid, temporary, external, dynamic/materialized
* Stages: Internal (named, user, table), external. Access: file URLs, scoped URLs, presigned URLs (GET_PRESIGNED_URL).
* **Pipes** are objects that contain a `COPY` command that is used by Snowpipe. **Snowpipe** is used for continuous, serverless loading of data into a Snowflake target table. 
* **Streams** - aka CDC (change data capture), keep track of certain changes made to a table including inserts, updates, and deletes. Update another table.
* **Tasks** - on schedule or triggered by predecessor task.
* `show variables`
* Unstructured data - stage file URLs, scoped URLs, presigned URLs. 
* **Data load/unload** - put, copy, variant, get
* Democratizing data with data governance controls: INFORMATION_SCHEMA, object tagging, OBJECT_DEPENDENCIES, external tokenization, secure views and UDFs
  * Classification. category types: semantic, privacy(Identifier, quasi-identifier, sensitive information), EXTRACT_SEMANTIC_CATEGORIES, ASSOCIATE_SEMANTIC_CATEGORY_TAGS
  * Data masking. dynamic, conditional, static
  * Row access policies and row-level security
* Query performance: QUERY_HISTORY, micro-partition, cluster, search optimization service
* Secure data sharing: direct, private exchange, public exchange, data clean room.  
  `ALTER SESSION SET simulated_data_sharing_consumer='acct'; UNSET; SHOW GRANTS TO SHARE shared_name; SHOW GRANTS OF SHARE shared_name;`
* Snowsight: `SAMPLE (100 ROWS); TABLESAMPLE SYSTEM (0.1);

### Access Controls
* System-defined roles: sysadmin, `show roles`
* Functional-level business and IT Roles
* System-level service account and object access roles 
* User management, role management, Multi-Account strategy, SCIM 2.0 (System for Cross-domain Identity management spec).
* RBAC (role-based access control), DAC (discretionary access control). 
