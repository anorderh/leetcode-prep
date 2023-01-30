# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Robbing houses, but can't pick adjacent
        # Starting at 'i' index
        # Can pick 2 over so (i, i+2, i+4, i+6)
        # Can pick 3 over (i, i+3, i+5, i+7...)
        # Can pick 4 over (i, i+4, i+6, i+8...) -> This is same as picking 2 over, but removing i+2

        size = len(nums)
        if size == 1: return nums[0]
        # Array holding past indices' maxs
        memory = [-1]*size

        #Recurrence relation
        def decide(idx):
            if idx < 0: # Base case, return 0 if invalid idx
                return 0

            if memory[idx] != -1: # If index max already found, return that
                return memory[idx]
            
            # Find max considering both idx-2 & idx -1
            res = max(decide(idx-2) + nums[idx], decide(idx-1))
            memory[idx] = res # Add max to index
            
            return res
        
        return decide(size-1) # Start from last index
