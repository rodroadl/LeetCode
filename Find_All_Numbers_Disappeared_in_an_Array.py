''' https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
    Find All Numbers Disappeared in an Array
    Given an array nums of n integers where nums[i] is in the range [1, n], 
    return an array of all the integers in the range [1, n] that do not appear in nums.'''
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ref = set()
        for i in range(len(nums)):
            ref.add(i + 1)
        set_nums = set(nums)
        result  = list(ref.difference(set_nums))
        result.sort()
        return result
        
            
def main():
    sol = Solution()
    print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(sol.findDisappearedNumbers([1,1]))

if __name__ == '__main__':
    main()

        