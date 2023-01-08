# My solution, 33/49 testcases passed
# Iterative but did not account for "I" island patterns

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        edgeWater = None
        islands = 0

        for y in range(len(grid)):
            prev = None

            for x in range(len(grid[0])):
                if edgeWater is None or edgeWater[x] == "0":
                    if (prev is None or prev == "0") and grid[y][x] == "1":
                        islands += 1
                prev = grid[y][x]

            edgeWater = grid[y]
        
        return islands

# Leetcode answer, 49/49 passed
# Recursive, iterates over every coord & applies DFS, replacing grid value with '#' so not to iterate again

class Solution:
    def numIslands(self, grid):
        # if map empty, return 0
        if not grid:
            return 0
            
        count = 0
        # iterate through every coordinate
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # island found
                if grid[i][j] == '1':
                    # check adjacent coords
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#' # once checked, replace with '#' so repeated iteration does not occur
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1) 
