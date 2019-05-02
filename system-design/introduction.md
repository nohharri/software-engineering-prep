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
