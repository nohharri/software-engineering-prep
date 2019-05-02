# Question
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

```
Input: "cbbd"
Output: "bb"
```

## Process
* Clarifying questions:
    * Are spaces and uppercase used? -> No.
* Custom Test cases
    ```
    "a" -> one character
    "tacocat" -> odd palindrome
    "xhaabbaazxp" -> palindrome inside non-palindrome
    ```

## Solution
Begin with the **naive recursive solution.** It is not efficient and should not be your final answer, as there is a quicker solution using loops (N^3). solution_recursive has the recursive answer.

#### Complexity
Our solution takes **O(N^2)** time. Lines 10 and 11 branch into two possible recursive paths. Because 2 branches are created at every iteration, this solution will grow exponentially at each iteration.

#### Optimization
Because we have overlap in our branches, we must deduce that this is a dynamic programming question. 

First, we must decide what to store as our key and values to implement a lookup table. This will prune branches that we have already looked through.

Our key will be the markers that indicate substrings. We will now store the substrings isntead of recalculating it every time.

This solution is N^2. The space used is N^2. The tradeoff for this algorithm is increased space. The previous algorithm doesn't require extra space. 