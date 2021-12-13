''' https://leetcode.com/problems/number-of-islands/
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
    return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.'''

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        hash = []
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(0)
            hash.append(temp)
        queue = []
        num_of_islands = 0
        min_row = 0
        col = 0
        while True:
            conti= False
            row = min_row
            while row < rows:
                while col < cols:
                    if hash[row][col] == 0:
                        if row - 1 < 0:
                            min_row = 0
                        else:
                            min_row = row -1
                        break
                    col += 1
                if col < cols and hash[row][col] == 0:
                    break
                col = 0
                row += 1
            if row == rows:
                return num_of_islands
            queue.append((row, col))
            while queue:
                row, col = queue.pop(0)
                if not hash[row][col]:
                    hash[row][col] = 1
                    if grid[row][col] == '1':
                        if not conti:
                            num_of_islands += 1
                            conti = True
                        if row - 1 >= 0 and hash[row - 1][col] == 0 and (row - 1, col) not in queue:
                            queue.append((row - 1, col))
                        if col - 1 >= 0 and hash[row][col - 1] == 0 and (row, col - 1) not in queue:
                            queue.append((row, col - 1))
                        if row + 1 < rows and hash[row + 1][col] == 0 and (row + 1, col) not in queue:
                            queue.append((row + 1, col))
                        if col + 1 < cols and hash[row][col + 1] == 0 and (row, col + 1) not in queue:
                            queue.append((row, col + 1))

def main():
    sol = Solution()
#     print(sol.numIslands([
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]))
#     print(sol.numIslands([
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]))
#     print(sol.numIslands([["0","1","0"],["1","0","1"],["0","1","0"]]))
#     print(sol.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
    print(sol.numIslands([["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]))
if __name__ == '__main__':
    main()