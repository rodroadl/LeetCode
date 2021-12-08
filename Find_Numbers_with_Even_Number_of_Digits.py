''' https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
    Find Numbers with Even Number of Digits
    Given an array nums of integers, return how many of them contain an even number of digits.'''

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                result += 1
        return result

def main():
    test = Solution()
    print(test.findNumbers([12,345,2,6,7896]))
    print(test.findNumbers([555,901,482,1771]))

if __name__ == '__main__':
    main()