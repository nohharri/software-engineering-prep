# Question
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

```
Input: a = "11", b = "1"
Output: "100"
```

```
Input: a = "1010", b = "1011"
Output: "10101"
```

## Complexity
* O(N) time and O(N) space.
* O(N + 1) is the worst case where N is the longer of the two input strings. It will continue to iterate until the end and then if there is a 1 needed to be carried, it will loop one more time.
* Extra space is needed for the output string. Worst case is O(N + 1) where N is the longer of the two inputs strings.