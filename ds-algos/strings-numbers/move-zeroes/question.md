# Question

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

## Solution
* iterate through the list once. If there is a non zero in the current position, then swap it with the last zero position. If the iteration marker is on the same index, nothing will swap. The zero index will move up and will continue to keep moving until a zero is found. This will ensure that the zero_pos will always either be pointing to the current iteration marker or a zero.

#### Complexity
* O(N) time and O(1) space

#### Logistics
* Asked by Facebook