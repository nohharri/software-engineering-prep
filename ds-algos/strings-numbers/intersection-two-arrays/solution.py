def intersect(nums1, nums2):
    count_dict = {}
    ans = []

    for num in nums1:
        count_dict[num] = count_dict[num] + 1 if num in count_dict else 1

    for num in nums2:
        if num in count_dict and count_dict[num] > 0:
            ans.append(num)
            count_dict[num] -= 1
    return ans
