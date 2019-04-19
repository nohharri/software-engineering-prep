# Database Performance

## Database Indexing
* An index is a data structure used to quickly access data a database table
* Indexes are stored within the database

### Two types of indices
* **Ordered Indices**: Indices are sorted
* **Hashed Indices**: Values are distributed uniformally using a hash function

### Clustered Indexes
* Clustered index is an ordered data file
* They are sometimes created on non-primary key fields
* In such cases, they will be used to group two or more columns together.
    * For example, if there was a student database and what semester they're studying.
    * The semesters can be indexed such that each student is grouped by the semester.

| Student      | Semester Enrolled |
|--------------|-------------------|
| John Smith   | 1                 |
| David Kim    | 1                 |
| Deepak Kumar | 2                 |
| Cecilia Li   | 2                 |

* In the table above, we cluster index by the semester. So in this case, a query that factors in the semester will be quicker. John Smith and David Kim will be grouped together and so will Deepak Kumar and Cecilia Li.

### Primary Keys
* Whenever primary keys are created on your tables, they are already sorted and unique, making the performance very efficient. There are two types: *dense index** and **sparce index.**

