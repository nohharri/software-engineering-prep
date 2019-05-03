# System Design Interviews

## Step 1: Require clarification

* System design questions will usually be intentionally kept vague so that the interviewee will be prompted to ask clarifying questions.
* Clarifying ambiguity is **critical** since the nature of system design questions are already so vague.

## Step 2: Define the API of the System Interface

* Define the APIs that are expected out of the system. This means asking the interviewee what certain functions are expected out of the system. For example, if we were to design Twitter:
```java
postTweet(userId, tweetData, tweetLocation, userLocation, timestamp, ...)

generateTimeline(userId, currentTime, userLocation, ...)

markTweetFavorite(userId, tweetId, timestamp, ...)
```

### Step 3: Clarify Scope of the Problem in relation to the Problem

* It is important we understand the scope of the problem. This will help define if we need load balancing, caching, partitioning, etc.
* For example, what is the scale of the tweets, number of tweets, etc.
* How much storage will we need?
* How much network bandwidth?

### Step 4: Defining our Data Model

Define the data model early. The candidate should be able to identify various entities of the system. Example database structure:
```
User: UserID, Name, Email, DoB, CreationData, LastLogin, etc.
Tweet: TweetID, Content, TweetLocation, NumberOfLikes, TimeStamp, etc.
UserFollowo: UserdID1, UserID2
FavoriteTweets: UserID, TweetID, TimeStamp
```

### Step 5: High Level Design

* Draw a block diagram with 5-6 boxes representing the core components of our system.
* The block diagram below shows how a client will interact with our application. Because we'll have to handle millions of requests per second, we will use a load balancer to go through a cluster of application servers which will then acccess our file storage and database.
* 

![](/assets/system-design-intro.png)

### Step 6: Specifics and Detail of Design

* Dig deeper into 2 or 3 components of the design
* The interviewer's feedback is the **most important** thing to consider. For example, if they ask or lead questions directed towards how the database is structured, this should be the component stressed throughout the interview.
    * With massive amounts of users, how do we partition our data?
    * How do we handle users that tweet frequently?
    * How do we store our data such that the most recent and relevant tweet of users are optimized?
    * At which layer should we introduce caching?
    * What components need load balancing?

### Step 7: Idenfity Bottlenecks

* Are there any single points of failure in our system?
* Do we have enough replicas such that a failure in the system won't result in a total shutdown of our app?
* How are we monitoring the performance of our application?

## Things to Know Before Going In
```
1 char = 1 byte
```
```
1 byte = 0.001 kilobytes
1 kilobyte = 0.001 megabytes
1 megabyte = 0.001 gigabytes
1 gigabyte = 0.001 terabytes
```

### 80-20 Rule
* This is a general rule saying that 20% of posts generate 80% of the traffic.

## Caching

* A modern day cache can store up to 256 GB of storage. This number is important to know when dealing with how much we can store in a cache.

## Databases: NoSQL vs. SQL

* Knowing the diferentiation and choosing the correct database type is crucial to system design questions.

* SQL Databases:
    * **structured**.
    * Each row represents exactly one entity
* NoSQL Databases:
    * Key-value stores:
        * Data is stored in an array of key-value pairs. The ‘key’ is an attribute name which is linked to a ‘value’. Well-known key-value stores include Redis, Voldemort, and Dynamo.
    * Document Databases:
        * In these databases, data is stored in documents (instead of rows and columns in a table) and these documents are grouped together in collections. Each document can have an entirely different structure. Document databases include the CouchDB and MongoDB.
    * Wide-Column Databases: 
        * Instead of ‘tables,’ in columnar databases we have column families, which are containers for rows. Unlike relational databases, we don’t need to know all the columns up front and each row doesn’t have to have the same number of columns. Columnar databases are best suited for analyzing large datasets - big names include Cassandra and HBase.
    * Graph Databases: 
        * These databases are used to store data whose relations are best represented in a graph. Data is saved in graph structures with nodes (entities), properties (information about the entities), and lines (connections between the entities). Examples of graph database include Neo4J and InfiniteGraph.

### High Level Differences

* Stores data in exclusively tables. Each row in a SQL database represents a single entity. For example, a car could be a row within a SQL database and columns could be make, model, year.
* NoSQL databases store data in different types of storage models, listed above.
* Schemas
    * SQL databases have fixed schemas. While columns can be altered, this requires modifying the whole database and at times, must shut down the database.
    * NoSQL databases have dynamic schemas. Columns can be added on the fly.
* Querying
    * SQL databases have a structured querying language.
    * NoSQL does not have a structured SQL language, sometimes called UnQL.
* Scalability
    * SQL databases are vertically scalable, which is usually more expensive than horizontal scaling. This means if we need to increase the size or speed, it can be expensive. Scaling vertically can be a time consuming process.
    * NoSQL databases are horizontally scalable. This means any cheap commodity or cloud instance can host NoSQL databases, thus making it far more cost effective than vertical scaling. 
* Reliability (ACID, Atomicity, Consistency, Isolation, Durability)
    * This is one of the largest benefits that SQL has over NoSQL. Most SQL databases are ACID compliant, meaning when it comes to data reliability and safe guarantee of performing transactions, SQL databases are the better set.
    * NoSQL databases usually sacrifice ACID compliance for **durability and scalability.**

### Why Use SQL?

* ACID Compliance - If your data needs to be consistent, reliable, and hold integrity, then SQL databases are still the best for ACID principles. This is important for a financial institution or e-commerce where losing data is not an option.
* Your database is very structured. If your business is not constantly changing and is in a very stable state, there would be little need to be constantly changing the structure of the database.

### Why use NoSQL?

* NoSQL databases prevent data from being the bottleneck. Big data is contributing to a large success for NoSQL databases, mainly because it handles data differently than the traditional relational databases.
* Storing large volumes of unstructured data
    * There are no limits on the types of data so we can add data that can be easily changed. 
* NosQL databases take advantage of cloud computing. Because they scale through cloud servers quite easily, NoSQL databases can scale quite quickly and cost-effectively.
