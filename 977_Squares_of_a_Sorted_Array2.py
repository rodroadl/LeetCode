''' https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/
    Squares of a Sorted Array
    Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order.
    Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        i = 0
        n = len(nums)
        res = []

        while i < n:
            if nums[0] * nums[0] > nums[len(nums) - 1] * nums[len(nums) - 1]:
                temp = nums.pop(0)
                res.insert(0, temp * temp)
            else:
                temp = nums.pop(len(nums) - 1)
                res.insert(0, temp * temp)
            i += 1
        return res

def main():
    sol = Solution()
    print(sol.sortedSquares([-4,-1,0,3,10]))
    print(sol.sortedSquares([-7,-3,2,3,11]))

if __name__ == '__main__':
    main()
    