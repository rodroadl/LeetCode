''' https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/
    Height Checker
    A school is trying to take an annual photo of all the students. 
    The students are asked to stand in a single file line in non-decreasing order by height. 
    Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
    You are given an integer array heights representing the current order that the students are standing in. 
    Each heights[i] is the height of the ith student in line (0-indexed).
    Return the number of indices where heights[i] != expected[i].'''
class Solution:
    def heightChecker(self, heights: list[int]) -> int: 
        original_heights = heights.copy()
        heights.sort()
        expected = heights.copy()
        count = 0 
        for i in range(len(expected)):
            if expected[i] != original_heights[i]:
                count += 1
        return count

def main():
    test = Solution()
    print(test.heightChecker([1,1,4,2,1,3]))
    print(test.heightChecker([5,1,2,3,4]))
    print(test.heightChecker([1,2,3,4,5]))

if __name__ == '__main__':
    main()