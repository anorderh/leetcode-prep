# https://leetcode.com/problems/power-of-two/?envType=study-plan&id=algorithm-i

class Solution:
    # All powers of 2 in binary have 1(0...) format
    # Using bitwise '&' (AND operator), n & n-1 is 1(0...) & 0(1...)
    # Meaning bitwise of n and n-1 results in 0 IF it is a power of 2
    # EX:
    # 1000 -> 8, n
    # 0111 -> 7, n-1
    # 1000 & 0111 = 0000 = 0. Power of 2!
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n-1) == 0
