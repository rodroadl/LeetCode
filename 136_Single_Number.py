''' https://leetcode.com/problems/single-number/
    136. Single Number

    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.'''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        port = 0
        ship = 1
        while port < len(nums) and ship < len(nums):
            if nums[port] == nums[ship]:
                nums.pop(ship)
                nums.pop(port)
                ship = 0
            ship += 1
        return nums[port]

def main():
    sol = Solution()
    # print(sol.singleNumber([2,2,1]))
    # print(sol.singleNumber([4,1,2,1,2]))
    # print(sol.singleNumber([1]))
    print(sol.singleNumber([1,1,2,3,4,5,4,5,3,-1,2]))

if __name__ == '__main__':
    main()