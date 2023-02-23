## Data
### Snowflake
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
* Democratizing data with data governance controls: INFORMATION_SCHEMA, object tagging, OBJECT_DEPENDENCIES, external tokenization, secure views and UDFs
  * Classification. category types: semantic, privacy(Identifier, quasi-identifier, sensitive information), EXTRACT_SEMANTIC_CATEGORIES, ASSOCIATE_SEMANTIC_CATEGORY_TAGS
  * Data masking. dynamic, conditional, static
  * Row access policies and row-level security
* Query performance: QUERY_HISTORY, micro-partition, cluster, search optimization service
* Secure data sharing: direct, private exchange, public exchange, data clean room.  
  `ALTER SESSION SET simulated_data_sharing_consumer='acct'; UNSET; SHOW GRANTS TO SHARE shared_name; SHOW GRANTS OF SHARE shared_name;`
* Snowsight: `SAMPLE (100 ROWS); TABLESAMPLE SYSTEM (0.1);

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
* 

## Concepts
* Memory: physical, virtual, shared (allows multiple programs to access the same data simultaneously).
* kernel space
* user space
* system call

* Encoding refers to the manner in which characters are translated to integer values.
* Concurrency and Parallelism  
  Concurrency means that two or more calculations happen within the same time frame. Parallelism means that two or more calculations happen at the same moment. Parallelism is therefore a specific case of concurrency. It requires multiple CPU units or cores.

## Algorithm
* Tail recursion (elimination)
* 
