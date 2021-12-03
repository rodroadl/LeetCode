''' 35. Search Insert Position https://leetcode.com/problems/search-insert-position/
    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.'''

def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return i
    return len(nums)