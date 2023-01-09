# https://leetcode.com/problems/unique-paths/description/

class Solution:
    # Recursive, memoization approach, using DFS to find all right & down pathes
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def move(x: int, y: int):
            if (x > m or y > n):
                return 0
            elif (x == m-1 and y == n-1):
                return 1
            else:
                return move(x+1, y) + move(x, y+1)
        
        return move(0, 0)

    # Iterative approach, calculating pathes to reach all cells & progressively adding
    def uniquePaths(self, m, n):
        dp = [[1]*n for i in range(m)] # Only 1 way to reach 1st row & 1st column
        #Unique paths to reach 1 cell is just pathes of left cell & above cell added together
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

