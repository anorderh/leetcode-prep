# https://leetcode.com/problems/fibonacci-number/description/?envType=study-plan&id=level-1

# Recursive implementation, ~800 ms
class Solution:
    def fib(self, n: int) -> int:
        return n if n <= 1 else self.fib(n-1) + self.fib(n-2)

# Iterative implementation, ~30 ms
class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1

        for x in range(2, n+1):
            a, b = b, b+a
        
        return b if n != 0 else 0
