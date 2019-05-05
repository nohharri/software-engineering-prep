# Designing a URL Shortening Service like Bitly

![](/assets/bitly.png)

## 1. Clarify Scope of the Problem

* Clarify the requirements and scope of the url shortening service.
* Functional Requirements
    * Given a URL, our service should generate a shorter and unique alias of it. This is called a short link.
    * When users access a short link, our service should redirect them to the original link.
    * Users should optionally be able to pick a custom short link for their URL.
    * Links will expire after a standard default timespan. Users should be able to specify the expiration time.
* Non-functional Requirements
    * The system should be highly available. This is required because, if our service is down, all the URL redirections will start failing.
    * URL redirection should happen in real-time with minimal latency.
    * Shortened links should not be guessable (not predictable).
* Extended Requirements
    * Analytics; e.g., how many times a redirection happened?
    * Our service should also be accessible through REST APIs by other services.

## Capacity Estimates and Costs

* There are usually three main points to estimate:
    * Storage
    * Bandwidth (Speed)
    * Memory
    
* If specifications are not given, then rough estimates are typically ok.
* Traffic estimates
    * Let's assume we have 500M new URL shortenings per month. Our application will be a lot more read heavy than write heavy. This is because our write happens once per url, then users will user the link repeatedly.
    * Let's say we have a 100:1 read/write ratio. This means with 500M writes, there are around 50B writes per month.
    ```
    # Read and writes per month
    500M writes * 100 reads = 50B reads per month
    # Queries per second
    500 million / (30 days * 24 hours * 3600 seconds) = ~200 URLs/s
    # URL Redirections per second
    100 * 200 URLs/s = 20K/s
    # 5 year estimate
    500 million * 5 years * 12 months = 30 billion

    ```
    * Let's just assume each url shortened takes about 500B. 
    * This doesn't have to be super accurate, but should be at least reasonable. Remember that 1 character takes up 1 byte. Consider appropriate storage based off this.
    ```
    30 billion * 500 bytes = 15 TB
    ```

* Bandwidth
    * Since we expect 200 write requests per second, our total data incoming will be:
    ```
    200 * 500 bytes = 100 KB/s
    ```
    * For read requests, we expect around 20K read requests per second
    ```
    20K * 500 bytes = ~10 MB/s
    ```

## Memory Estimates

* Let's follow the 80-20 rule and say 20% of urls generate 80% of the traffic. This means we want to cache 20% of the urls.
* Our total requests per day can be calculated as such:
```
20K * 3600 seconds * 24 hours = ~1.7 billion
```
Let's cache 20% of these requests.
```
0.2 * 1.7 billion * 500 bytes = ~170GB
```
* One thing to note is that there will be a lot of duplicate requests so 170GB will be the upper bound of requests.

## Define System APIs

We should always define what is expected out of the system.
```
createURL(api_dev_key, original_url, custom_alias=None, user_name=None, expire_date=None)

deleteURL(api_dev_key, url_key)
```

## Designing our Data Model

* We know a few things already.
    * We need to store billions of records.
    * Each object we store is small (less than 1K).
    * There are no relationships between records—other than storing which user created a URL.
    * Our service is read-heavy.

![bitly db model](/assets/db_model.png)

* Since we anticipate storing billions of rows, and we don’t need to use relationships between objects – a NoSQL key-value store like DynamoDB, Cassandra or Riak is a better choice. A NoSQL choice would also be easier to scale. Please see SQL vs NoSQL for more details.

## High Level Design / Specifics of Design

* There are many things you can touch upon, but some key things come to mind when dealing with this specific problem. Let's begin by defining how are API is going to function at a high level. The interviewer might ask you to implement it for real so be prepared to code if asked.
```
http://bit.ly/jlg8zpc
```
* Let's say this is the output of our function. What are some key problems this problem needs to address?
    * Let's say we hash the value. How do we handle collisions? (two distinct urls hitting the same value) Let's say we use a unique hash, for example MD5 of SHA256.
        * Appending user id - problem with this is user might not be logged in. To address this, we could have the user pick a unique key. They will continue to pick a key until it is unique.
        * Add increasing sequence of numbers - problem is sequence might overflow

![](/assets/encode.png)

### Data Partitioning

* We need to come up with a partitioning scheme that can store up to billions of URLs.
    * Range based partitioning
        * Let's say we divide all the urls based off the first letter of the URL or the hash key. We could also combine the partition of less frequent keys into one partition.
        * The problem with this is that it might lead to unbalanced servers. For example, if there are a lot of hashes/urls that start with the letter A, then A would slow down more than other databases.
    * Hash based partitioning
        * We take a hash of the object we are storing. This can also lead to overloaded partitions. This can be solved with consistent hashing.

### Caching

* Cache urls can be used to quickly access data without going into the backend storage.
* Let's stick with our 80-20 rule. This means 80% of our traffic will come from 20% of the users. We should reference the memory we used from the earlier calculation to determine how much cache space we'll need.

```
0.2 * 1.7 billion * 500 bytes = ~170GB
```

* Since we need 170GB, we can easily store it into one cache.
* We can use a LRU cache policy for our eviction policy.

## Load Balancing

* We can define a load balancer in three parts of the system:
    * Between Clients and Application servers
    * Between Application Servers and database servers
    * Between Application Servers and Cache servers
* We could use simple round robin to distribute our load.


## DB Cleanup
* How do we want to handle removing old urls?
* There are a few scenarios:
    * We create a separate cleanup service that runs periodically to delete old links. We can set up a server that will check the database at a time when the database is not being used and then clean them up. For example, if a timestamp has reached the 2 year mark, we can delete the entry.
    * We keep the links forever. Storage is very cheap and users even after 2 years might want to return to the site.

## Telemetry

* How many times a short URL has been used, what were user locations, etc.? How would we store these statistics? If it is part of a DB row that gets updated on each view, what will happen when a popular URL is slammed with a large number of concurrent requests?
* Some statistics worth tracking: country of the visitor, date and time of access, web page that refers the click, browser, or platform from where the page was accessed.

## Security
* Can users create private URLs or allow a particular set of users to access a URL?
* We can store permission level (public/private) with each URL in the database. We can also create a separate table to store UserIDs that have permission to see a specific URL. If a user does not have permission and tries to access a URL, we can send an error (HTTP 401) back. Given that we are storing our data in a NoSQL wide-column database like Cassandra, the key for the table storing permissions would be the ‘Hash’ (or the KGS generated ‘key’). The columns will store the UserIDs of those users that have permissions to see the URL.