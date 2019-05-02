# Question

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

## Followup: (with duplicates)
How would you do this with duplicates allowed?
For example, given an array:

[0, 2, 4, 5, 7, 7, 7, 8, 8, 8, 10, 10], 20

How can you grab three elements given that **at least** one index is different?

For example, [5, 7, 8] and [5, 7, 8] are both viable because there are multiple 7s and multiple 8s. There are different indexes you can combine to create those solutiions. Indices [3, 4, 7] and [3, 5, 7] both have values [5, 7, 8] but should be counted twice because there is at least one index that is different.