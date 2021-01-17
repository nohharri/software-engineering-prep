# Valid Palindrome

## Question

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

**Example 1:**

```
Input: "A man, a plan, a canal: Panama"
Output: true
```

**Example 2:**

```
Input: "race a car"
Output: false
```

**Constraints:**

* s consists only of printable ASCII characters.

## Solution

1. When looking at palindromes, try to find a greedy solution. Then, there are two things to consider:
  * Check even and odd strings
  * Do we want to go middle out or outside in?
  
Before starting, consider the cleaning of the string before starting. One thing is ignoring case. Let's just convert to lowercase.

```
a man, a plan, a canal: panama
```

2. For this solution, let's go outside in. Let's use two pointers then go outside in. If the value is a space or a special character, we can skip it.

```javascript
var isPalindrome = function(s) {
    s = s.toLowerCase();
    let l = 0, r = s.length - 1;
    
    while (l < r) {
        if (!s[l].match(/^[a-z0-9]+$/i)) {
            l++;
        } else if (!s[r].match(/^[a-z0-9]+$/i)) {
            r--;
        } else if (s[l] !== s[r]) {
            return false;
        } else {
            l++;
            r--;
        }
    }
    
    return true;
};
```

## Complexity

**Time Complexity:** O(N) where N is the length of s. This is fairly straightforward. We are iterating through the length once. It would more accurately be N / 2.
**Space Complexity:** O(1) because we are not using any extra space. If we want to be technical, we are using O(N) space to recycle the space of s but we are not using extra space because we are just re-using the variable.
