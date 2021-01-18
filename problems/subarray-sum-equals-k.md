# Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

**Example 1:**

```
Input: nums = [1,1,1], k = 2
Output: 2
```

**Example 2:**

```
Input: nums = [1,2,3], k = 3
Output: 2
```

**Constraints:**

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

# Solution

1. Questions we should ask the interviewer:
* Can we have negative values? - yes
* What do we do about k if k = 0?

2. We should first rule out strategies we cannot use. We cannot use the sliding window algorithm because of the negative values. We should also note the inefficient solution prior to finding the optimized solution. We know we can do this in O(N^2) time so that will be our upper bound. This implies we can find a solution in O(N) or O(logN) time. We are not using any tree structure, so we can assume our solution will be O(N). The reason we can do this in O(N) time is because we can check every subarray with two for loops and then add to the count if the subarray that's looked at.

* We find the worst case for this as O(N^2). Now the interviewer will probably want something better than this.
* We know we cannot use sliding window because of the negative values. Let's also rule out sorting because this problem looks at continuous subarrays.
* Keep in mind that the problem does not ask for the contents of the subarray, just the total count. This should simplify things.

3. Let's look at the following array.

```
[1, 4, 1, 6, -2, 2, 1, 5] k = 6
```

Let's just write out our solution.

```
[1, 4, 1] [6] [6, -2, 2] [1, 5] ans = 4
```

We know that looking at the first three values gets us the k value. But how do we determine what to do when we get to 6? Let's say we've been calculating a cumulative sum the whole time. If we take the value of the first three indices away from that sum, we can determine that the subarray [6] is equal to our answer. Our cumulative sum by this point is 12. If our whole array were only [1, 4, 1, 6], we can see here that taking away the sum of [1, 4, 1] from the sum of 12 gives us 6, which is our k value.

Now how would we determine this number for the remaining array? We can see that our next array can be found by removing [1, 4, 1] as well. This gives us [6, -2, 2], which is equal to k. How would we take away [1, 4, 1]?

The answer here is quite simple. We can see that the cumulative sum is 12 again, so we can once again see that the cumulative sum 12 - 6 == k.

4. Now how do determine this when the cumulative values don't seemingly fit nicely? We know that 1 and 5 are in the array. By 5, our cumulative sum is 18. **This is where our logic comes together.** We know that 18 - 6 = 12. We know that [1, 4, 1, 6, -2, 2] has a cumulative value of 12. This means that we know that 1 and 5 work because we can just remove the value of 12 from our subarray and we know that we can increment 1 to our count.

We can do this by using a map. If a cumulative value has not been seen before, we can just mark it as seen.

Looking at our example, we can start with a map with { 0 }. 
```
map = { 0 }
[]
```

When we get to 1, we can simply add the cumulative sum to the map.
```

map = { 0, 1 }

[1]
```

Now we see that 1, 4, 1 equals 6. 6 - 6 === 0. We see 0 in the map. We increment 1 to count.
```
map = { 0, 5, 6 }

[1, 4, 1]
```

Let's look at [1, 4, 1, 6]. We can add it to the map because we have not yet seen 12. We see that 12 - 6 == 6 which is in the map. We increment to count once more. This logic makes sense because we know that the cumulative value of [1, 4, 1] is 6. Our current sum is 12. If we take away [1, 4, 6], we just get 6. We then always know our cumulative map value.

```
map = { 0, 5, 6, 12 }

[1, 4, 1, 6]
```

Our final solution will have a presum computation that looks like this.
```
[1, 4, 1, 6, -2, 2, 1, 5] k = 6

presum: [1, 5, 6, 12, 10, 12, 13, 18]

map: { 0, 1, 5, 6, 12, 10, 12, 13 }

check { 0 - 6 = false, 1 - 6 = false, 5 - 6 = false, 6 - 6 = true, 12 - 6 = true, 10 - 6 = false 12 - 6 = true, 13 - 6 = false, 18 - 6 = true }

count: 3
```

If we stored all the presums in a map and then see if we take k away from the current presum, we should see that the calculation is in the map. If it is, then we can increment to the count.

```javascript
var subarraySum = function(nums, k) {
    const map = { 0: 1 };
    let currSum = 0;
    let count = 0;
    
    for (let i = 0; i < nums.length; i++) {
      currSum += nums[i];
      if (currSum - k in map) {
          count += map[currSum - k];
      }
      map[currSum] = currSum in map ? map[currSum] + 1 : 1;
    }
    
    return count;
};
```

The reason we have ```map[currSum] = currSum in map ? map[currSum] + 1 : 1;``` is because we need to account for the scenario where a value is cancelled out. For example, consider ```[6, -6, 6]```. We need to get the cumulative value of as many times we've seen the value 6 because we have [6], [6, -6, 6] and [6]. if we only got one from it everytime, we would fail to consider [6, -6, 6] scenario.
