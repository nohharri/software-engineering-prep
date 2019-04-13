# recursive
def longest_palindrome_helper(s, start, end):
    if start > end:
        return ''
    if start == end:
        return s[start]
    if s[start] == s[end]:
        return s[start] + longest_palindrome_helper(s, start + 1, end - 1) + s[end]
    # s[start] != s[end]
    substr1 = longest_palindrome_helper(s, start, end - 1)
    substr2 = longest_palindrome_helper(s, start + 1, end)
    if len(substr1) >= len(substr2):
        return substr1
    else:
        return substr2


def longest_palindrome(s):
    return longest_palindrome_helper(s, 0, len(s) - 1)


print(longest_palindrome("sssbababdddd")) # babab
print(longest_palindrome("tacocat")) # tacocat
