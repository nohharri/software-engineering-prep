# Product of Array except self

**link:** https://leetcode.com/problems/product-of-array-except-self/

## Problem

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

### Example:
```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```

**Constraint:** It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

**Note:** Please solve it without division and in **O(n)**.

**Follow up:**
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## Solution

1. The biggest caveat of the problem is that division is not allowed. This problem would be easy with division. We should also recognize that we cannot use addition or subtraction. Both would be too slow. First step is recognizing a pattern. It may be easier to imagine the values as letters.

```
[1, 2, 3, 4] => [a, b, c, d]
```
2. Let's break down how the solution looks. We know that the result of the new array should be the product of the array except itself.
```
[24, 12, 8, 6] => [bcd, acd, abd, abc]
```
3. Let's break it down even further. Break it down by side.
```
[ bcd, a * cd, ab * d, abc] => [bcd, cd, d, 1] X [1, a, ab, abc]
```
4. From here, the pattern should be quite obvious. The first array shows that the values are increasing backwards while the second array shows the values are increasing forward. We can continuously have a running value that will get incremented to give us a running total. Then we can multiply both arrays to get our final answer.

```
1. backwards iterate through the array by grabbing the n + 1 value then multiplying it to a running total.
2. forwards iterate through the array by grabbing the n - 1 value then multiplying it to a running total.
3. Add these values together.
```

```javascript
var productExceptSelf = function(nums) {
    let ans = [];
    let mult = 1;
    
    for (let i = 0; i < nums.length; i++) {
        let oneBehind = i - 1 >= 0 ? nums[i - 1] : 1;
        mult *= oneBehind;
        
        ans.push(mult);
    }
    
    mult = 1;
    for (let i = nums.length - 1; i >= 0; i--) {
        let oneAhead = i + 1 < nums.length ? nums[i + 1] : 1;
        mult *= oneAhead;
        
        ans[i] *= mult;
    }
    
    return ans;
};
```

## Complexity

* The time complexity is O(N) where N is the size of the array. The array is iterated through twice.
* The space complexity is O(N) where we make an N sized array to store the values. The output array does not count towards the space in this problem so this solution is fine.
