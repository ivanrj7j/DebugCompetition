def min_sub_array_len(target: int, nums: list[int]) -> int:
    """
    Given an array of positive integers nums and a positive integer target, 
    return the minimal length of a subarray whose sum is greater than or equal to target. 
    If there is no such subarray, return 0 instead.
    """
    l = 0
    curr_sum = 0
    res = float('inf')
    
    for r in range(len(nums)):
        curr_sum += nums[r]
        while curr_sum >= target:
            res = min(res, r - l)  # Bug: Off-by-one in window length calculation
            curr_sum -= nums[l]
            l += 1
            
    return res if res != float('inf') else 0
