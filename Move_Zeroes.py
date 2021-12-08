''' https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
    Move Zeroes
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.'''
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        readPointer = 0
        count = 0
        while readPointer < len(nums) and count < len(nums):
            if nums[readPointer] == 0:
                nums.append(nums.pop(readPointer))
                count += 1
            else:
                readPointer += 1
                count += 1

def main():
    test = Solution()
    nums = [0,1,0,3,12]
    test.moveZeroes(nums)
    print('after moveZeroes', nums)
    nums = [0]
    test.moveZeroes(nums)
    print('after moveZeroes', nums)

if __name__ == '__main__':
    main()