''' https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3295/
    Max Consecutive Ones
    Given a binary array nums, return the maximum number of consecutive 1's in the array.'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        curr = 0
        largest = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            if curr > largest:
                largest = curr
        return largest
    
def main():
    test = Solution()
    print(test.findMaxConsecutiveOnes([1,1,0,1,1,1]))

if __name__ == '__main__':
    main()