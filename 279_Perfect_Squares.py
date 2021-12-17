''' https://leetcode.com/problems/perfect-squares/
    279. Perfect Squares
    Given an integer n, return the least number of perfect square numbers that sum to n.

    A perfect square is an integer that is the square of an integer; in other words, 
    it is the product of some integer with itself. For example, 
    1, 4, 9, and 16 are perfect squares while 3 and 11 are not.'''

class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        path = []
        queue = [(n, path)]
        min_path = n
        grid = []

        i = 0
        m = 1
        while i < n:
            grid.append(1)
            i += 1

        while m * m <= n:
            perfect_squares.append(m * m)
            m += 1

        grid[n - 1] == 0
        while queue and len(path) < min_path:
            curr, path = queue.pop(0)

            if curr == 0:
                if len(path) < min_path:
                    min_path = len(path)

            for num in perfect_squares[::-1]:
                if num <= curr and grid[curr - num - 1] == 1:
                    new_path = list(path)
                    new_path.append(num)
                    grid[curr - num - 1] = 0
                    queue.append((curr - num, new_path))
        
        return min_path

def main():
    sol = Solution()
    print(sol.numSquares(12))
    print(sol.numSquares(13))
    print(sol.numSquares(312))
    print(sol.numSquares(4))
    print(sol.numSquares(7168))
if __name__ == '__main__':
    main()