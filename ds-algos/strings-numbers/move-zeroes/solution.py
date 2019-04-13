def move_zeroes(nums):
    if len(nums) <= 1:
        return

    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

move_zeroes([0,1,0,3,12])