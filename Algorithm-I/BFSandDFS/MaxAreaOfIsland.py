# https://leetcode.com/problems/max-area-of-island/?envType=study-plan&id=algorithm-i

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxCols = len(grid)
        maxRows = len(grid[0])

        def calcArea(y: int, x: int): # Recursive method for DFS
            # End condition, if y & x exceed bounds or if [y][x] is water or visited
            if x >= len(grid[0]) or y >= (len(grid)) or x < 0 or y < 0 or grid[y][x] != 1:
                return 0
            grid[y][x] = -1 # Mark as visited

            print(f"y:{y}, x:{x} is valid land")

            # Visit all proximal spaces
            sum = 1
            sum += calcArea(y+1, x)
            sum += calcArea(y, x+1)
            sum += calcArea(y-1, x)
            sum += calcArea(y, x-1)

            return sum
        
        # Check for land at every square & find max
        maxArea = 0
        for y in range(maxCols):
            for x in range(maxRows):
                maxArea = max(maxArea, calcArea(y, x))
        return maxArea
