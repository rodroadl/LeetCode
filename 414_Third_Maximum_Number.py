''' https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
    Third Maximum Number
    Given an integer array nums, return the third distinct maximum number in this array. 
    If the third maximum does not exist, return the maximum number.'''
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        largest = max(nums)
        nums2 = set(nums)
        nums2.discard(largest)
        if len(nums2):
            nums2.discard(max(nums2))
        if not len(nums2): return largest
        else: return max(nums2)
    
def main():
    test = Solution()
    print(test.thirdMax([3,2,1]))
    print(test.thirdMax([1,2]))
    print(test.thirdMax([2,2,3,1]))
    print(test.thirdMax([1,1,1]))

if __name__ == '__main__':
    main()