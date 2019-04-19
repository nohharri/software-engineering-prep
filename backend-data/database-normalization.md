# Databases

## Database Normalization
* Technique used in relational databases
* Systematic approach to:
    * **reducing data redundancy**
    * **ensuring logical data dependency**
    
#### Benefits of Database Normalization
* uses extra memory space
* difficult logically to update database
 
### 5 Normal Forms
1. First Normal Form
2. Second Normal Form
3. Third Normal Form
4. BCNF
5. Fourth Normal Form

#### First Normal Form (1NF)
1. Values should only have single (atomic) valued attributes.
```
StudentID | Name | Classes
123       | John | Computer Science, Linear Algebra

-- Breaks atomic values since classes has multiple values
```
2. Columns in a table should have unique names
3. Values stored in a column have to be of the same domain.
4. Order of data stored should not matter

#### Second Normal Form
