# Sorting

## Quicksort vs. Mergesort

* On average, quicksort is better than mergesort, especially in the context of arrays.
* Quicksort takes place in-place, while mergesort creates temporary arrays
* Merge sort is better for large data structures and adapted easily for linked lists
* Quicksorts are usually better for arrays and merge sort is better for linked lists.
    * Quicksort uses indices and merge sort requires adding an element between two elements. The array would need to be resized if implemented with merge sort, but a linked list can resize in O(1) time.


## Quicksort
* Pseudocode
    * if low < high:
        * pi = partition()
            * partition from low to high where the partition is high
            * If the value is lesser than partition, swap it to the idx, then increment idx
            * increment the index and return it as the partition
        * quicksort low to partition - 1
        * quicksort partition + 1 to high