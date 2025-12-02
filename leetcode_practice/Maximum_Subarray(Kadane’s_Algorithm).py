def maxSubArray(nums):
    current_sum = nums[0]     # 1
    max_sum = nums[0]         # 2

    for num in nums[1:]:      # 3
        current_sum = max(num, current_sum + num)  # 4
        max_sum = max(max_sum, current_sum)        # 5
    
    return max_sum            # 6
