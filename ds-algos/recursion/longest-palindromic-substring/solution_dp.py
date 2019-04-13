def longest_palindromic_helper(s, start, end, lookup):
    if start > end:
        return ''
    if start == end:
        return s[start]

    # if we haven't seen this substring
    if (start, end) not in lookup:
        if s[start] == s[end]:
            lookup[(start, end)] = s[start] + longest_palindromic_helper(s, start + 1, end - 1, lookup) + s[end]
        else:
            substr1 = longest_palindromic_helper(s, start, end - 1, lookup)
            substr2 = longest_palindromic_helper(s, start + 1, end, lookup)
            if len(substr1) > len(substr2):
                lookup[(start, end - 1)] = substr1
                return lookup[(start, end - 1)]
            else:
                lookup[(start + 1, end)] = substr2
                return lookup[(start + 1, end )]

    return lookup[(start, end)]


def longest_palindrome(s):
    return longest_palindromic_helper(s, 0, len(s) - 1, {})


print(longest_palindrome("sssbababdddd")) # babab
print(longest_palindrome("tacocat")) # tacocat
