''' https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
    Squares of a Sorted Array
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.'''

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        new_list = []
        for num in nums:
            new_list.append(num * num)
        new_list.sort()
        return new_list

def main():
    test = Solution()
    print(test.sortedSquares([-4,-1,0,3,10]))
    print(test.sortedSquares([-7,-3,2,3,11]))

if __name__ == '__main__':
    main()