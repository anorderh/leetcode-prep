# https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bitwise trick, applying AND to prev number
        ans = 0
        while n:        # While not 0
            n &= n-1    # Apply bitwise, removing trailing 1
            ans += 1
        return ans

