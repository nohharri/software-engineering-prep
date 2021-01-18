Dot Product of Sparse Vectors

https://leetcode.com/problems/dot-product-of-two-sparse-vectors/solution/

# Question

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?


Example 1:

```
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
```

Example 2:

```
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
```

Example 3:

```
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
```

# Solution
1. At first, we can come up with the primitive solution, which would just involve grabbing the values. Remember to mention the primitive solution to the interviewer.

```javascript
var SparseVector = function(nums) {
    this.nums = nums;
};

// Return the dotProduct of two sparse vectors
/**
 * @param {SparseVector} vec
 * @return {number}
 */
SparseVector.prototype.dotProduct = function(vec) {
    const nums2 = vec.nums;
    return this.nums.map((val, idx) => {
       return val * nums2[idx]; 
    }).reduce((a, b) => a + b);
};
```
This answer is O(N). It's not necessarily bad, but we can improve upon this.

2. The key to this solution is to pick up on hints and specifications. We know a **sparse** vector is a vector with **mostly** zeroes. Could we save on space if we just didn't store the zeroes?

3. We could consider using a hash map. This way, we can ignore zeroes.

```
var SparseVector = function(nums) {
    this.map = {};
    this.length = nums.length;
    for (const [idx, val] of nums.entries()) {
        if (this.val !== 0) {
            this.map[idx] = val;
        }
    }
};

// Return the dotProduct of two sparse vectors
/**
 * @param {SparseVector} vec
 * @return {number}
 */
SparseVector.prototype.dotProduct = function(vec) {
    let ans = 0;
    
    for (let i = 0; i < vec.length; i++) {
        let num1 = i in vec.map ? vec.map[i] : 1;
        let num2 = i in this.map ? this.map[i] : 1;
        ans += num1 * num2;
    }
    
    return ans;
};

```
Ignoring zeroes saves us on space.

# Complexity

### Time

O(N): We are iterating through twice.
O(N): We are using less space but the space complexity would still be O(N) given that our worst case would be no zeroes.
