''' https://leetcode.com/problems/pascals-triangle/
    118. Pascal's Triangle
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:'''

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal_triangle = [[1]]
        if numRows >= 2:
            pascal_triangle.append([1,1])
        for i in range(3, numRows + 1):
            next = []
            next.append(1)
            for j in range(i - 2):
                next.append(pascal_triangle[i-2][j] + pascal_triangle[i-2][j + 1])
            next.append(1)
            pascal_triangle.append(next)
        return pascal_triangle
        
def main():
    sol = Solution()
    print(sol.generate(1))    
    print(sol.generate(2))
    print(sol.generate(3))

if __name__ == '__main__':
    main()