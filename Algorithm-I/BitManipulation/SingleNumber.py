# https://leetcode.com/problems/single-number/description/?envType=study-plan&id=algorithm-i

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        start = 0

        for num in nums: 
            start ^= num # XOR operator
            # Returns 1 if operands are different, 0 if they're the same
            # Tracks numbers via bits, to remove duplicates once iterated over
        
        return start
