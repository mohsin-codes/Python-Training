def find_max(nums):
    max = nums[0]
    for number in nums:
        if number > max:
            max = number
    return max