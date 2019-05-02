'''
# 3sum

'''

def three_sum_w_dups(arr, sum):
    num_sums, i, j, k = 0, 0, 0, 0
    arr.sort()

    for i in range(len(arr)):
        j = i + 1
        k = len(arr) - 1
        
        while j < k:
            curr_sum = arr[i] + arr[j] + arr[k]
            if curr_sum == sum:
                j_dup, k_dup = 1, 1
                while j + 1 < k and arr[j] == arr[j + 1]:
                    j += 1
                    j_dup += 1
                while k - 1 > j and arr[k] == arr[k - 1]:
                    k -= 1
                    k_dup -= 1
                num_sums += (j_dup * k_dup)
                print num_sums
                j += 1
                k -= 1
            elif curr_sum < sum:
                j += 1
            else:
                k -= 1
    return num_sums


print(three_sum_w_dups([0, 2, 4, 5, 7, 7, 7, 8, 8, 8, 10, 10], 20))