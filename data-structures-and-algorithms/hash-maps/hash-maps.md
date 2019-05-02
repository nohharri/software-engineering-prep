# Hash Maps

Hash maps are a data structure used to store key-value pairs. There are a few important properties that all hash maps require:

* **key-value store**: Each element in the array must store both the original key and value.
* **hash function**: 

## Complexity

|        | Average Case | Worst Case |
|--------|--------------|------------|
| space  | O(N)         | O(N)       |
| lookup | O(1)         | O(N)       |
| insert | O(1)         | O(N)       |
| delete | O(1)         | O(N)       |

## Benefits 

* Faster average lookups than arrays and lists (O(1))
* Hashable functions

## Negatives

* Slow worst-case lookups
* Unordered
* Hash map can be O(N) time if hash function is implemented poorly.
* Resizing array takes O(N) time and hash to resolve must be recalculated for all existing values.

# Collision Resolution

* Collisions occur when two hashed keys return the same result. There are two main types of collision resolution methods.

## Open Addressing

* Looking for available spaces within the array.
* Benefits:
    * Does not grow vertically.

### Types of Open Addressing

* Linear Probing
    * Use of a linear function to hash.
* Quadratic Probing
    * Use of a quadratic function to hash.
* Double hashing
    * Hashing x amount of times using two different hash functions

## Closed Addressing

### Types of Closed Addressing

* Use of linked lists to stored hashed values
* Benefits:
    * Does not grow horizontally as often as open addressing.
    * On average quicker inserts than open addressing.