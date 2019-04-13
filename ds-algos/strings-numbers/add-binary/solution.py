def add_binary(a, b):
    a_idx = len(a) - 1
    b_idx = len(b) - 1
    carry = 0
    ans = ''

    while a_idx >= 0 or b_idx >= 0 or carry > 0:
        a_int = int(a[a_idx]) if a_idx >= 0 else 0
        b_int = int(b[b_idx]) if b_idx >= 0 else 0

        summed = a_int + b_int + carry
        carry = 1 if summed > 1 else 0
        ans = str(summed % 2) + ans

        a_idx -= 1
        b_idx -= 1
    return ans
