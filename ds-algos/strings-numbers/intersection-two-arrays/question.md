# Question

Given two arrays, write a function to compute their intersection.

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```

## Solution
* Iterate through the first list and increment a count dictionary where the value is a count of the number of times the number has been seen.
* Iterate through the second list and decrement the times the number from nums2 has been seen in nums1
* Every time you decrement, append it to the result.
* Do not append if the count of the number in dict is 0.

## Complexity
* O(N + M) time and O(N) space
* O(N + M) time because two passes through both nums lists/
* O(N) space where N is the size of the first list

## Logistics
* From LeetCode
* Asked by Facebook
* Easy Problem