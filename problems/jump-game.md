# Jump Game

## Question

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index. 

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 ```

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i] <= 10^5

## Solution

1. We should first see if a greedy solution is possible. While this problem may look like a graph traversal problem at first, we should look at simple iteration first and see if we can solve it in linear time. When looking at linear solutions, we should try to find patterns, forward traversal, and backwards traversal. Let's try looking at the simplest case and see if we can solve it from there.

```
[2]
```

2. We know this will return true because the starting index is equal to the last index. We can consider the starting index === the last index is our terminating case.

```
[2, 0, 3]
```

3. Let's consider a more complex case. If you start backwards, we can see that the last index is not reachable from the second index, but reachable from the first index. We can say the last reachable index starts at index 2 and we can move backwards. We then check if we can get to index 2 from index 1. We cannot. We can continue iterating backwards. We then see on index 0 that we can get to our last reachable index 2. We update last reachable index to index 0. Because the first index === last index, we can determine that the index is reachable.

```javascript
var canJump = function(nums) {
    let lastReachableIdx = nums.length - 1;
    
    for (let i = nums.length - 1; i >= 0; i--) {
        if (nums[i] + i >= lastReachableIdx) {
            lastReachableIdx = i;
        }
    }
    return lastReachableIdx === 0;
};
```

## Complexity

**Time Complexity**: O(n) because we are only iterating through once.

**Space Compliexity:** O(1) because we do not store any values besides lastReachableIdx.
