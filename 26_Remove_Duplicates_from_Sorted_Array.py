''' https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    Given an integer array nums sorted in non-decreasing order, 
    remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same.
    Since it is impossible to change the length of the array in some languages, 
    you must instead have the result be placed in the first part of the array nums. 
    More formally, if there are k elements after removing the duplicates, 
    then the first k elements of nums should hold the final result. 
    It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array. 
    You must do this by modifying the input array in-place with O(1) extra memory.

    Custom Judge:
    The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length
    int k = removeDuplicates(nums); // Calls your implementation
    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }

    If all assertions pass, then your solution will be accepted.'''

class Solution:
    def removeDuplicates(self, nums) -> int:
        length = len(nums)
        i = 1
        count = 0
        if len(nums):
            last = nums[0]
            while i < length: 
                if nums[i] == last:
                    nums.pop(i)
                    length -= 1
                else:
                    last = nums[i]
                    count += 1
                    i += 1
                
            

test = Solution()
test.removeDuplicates([1,1,2])