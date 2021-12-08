''' https://leetcode.com/problems/maximum-subarray/
    53. Maximum Subarray
    Given an integer array nums, find the contiguous subarray 
    (containing at least one number) which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.'''

def maxSubArray(nums):
    largest = max(nums)
    total = 0
    i = 0
    start_adding = False
    while i < len(nums):
        if nums[i] > 0:
            start_adding = True
            temp_start = i
        while start_adding and total + nums[i] > nums[i-1]:
            total += nums[i]
            i += 1
            temp_end = i
        if total > largest:
            largest = total
            start = temp_start
            end = temp_end
            total = 0
        start_adding = False
        i += 1
    return nums[start:end]

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
