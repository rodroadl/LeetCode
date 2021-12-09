''' https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
    Find All Numbers Disappeared in an Array
    Given an array nums of n integers where nums[i] is in the range [1, n], 
    return an array of all the integers in the range [1, n] that do not appear in nums.'''
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
            if len(res) != 0 and nums[i] == res[0]:
                res.pop(0)
        return res
            
        
            
def main():
    sol = Solution()
    print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(sol.findDisappearedNumbers([1,1]))

if __name__ == '__main__':
    main()

        
