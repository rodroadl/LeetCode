'''https://leetcode.com/problems/majority-element/
    169. Majority Element
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        temp = nums[0]
        size = len(nums)
        count = 0
        while True:
            try:
                nums.remove(temp)
                count += 1
                if count > size // 2:
                    return temp
            except ValueError:
                count = 0
                temp = nums[0]



def main():
    sol = Solution()
    print(sol.majorityElement([3,2,3]))        
    print(sol.majorityElement([2,2,1,1,1,2,2]))    

if __name__ == '__main__':
    main()