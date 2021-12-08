''' https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
    Sort Array By Parity
    Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
    Return any array that satisfies this condition.'''
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        start = 0
        end = len(nums) - 1
        while start < len(nums):
            if nums[start] % 2 == 1:
                found = False
                while start < end < len(nums) and not found:
                    if nums[end] % 2 == 0:
                        temp = nums[start]
                        nums[start] = nums[end]
                        nums[end] = temp
                        found = True
                    end -= 1
            start += 1
        return nums
        
def main():
    test = Solution()
    nums = [3,1,2,4]
    print(test.sortArrayByParity(nums))
    
    nums = [0]
    print(test.sortArrayByParity(nums))

    nums = [1,3]
    print(test.sortArrayByParity(nums))

    nums = [0,1,2]
    print(test.sortArrayByParity(nums))

if __name__ == '__main__':
    main()