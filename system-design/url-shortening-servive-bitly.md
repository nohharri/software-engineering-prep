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
    * This doesn't have to be super accurate, but should be at least reasonable. Remember that 1 byte takes about 