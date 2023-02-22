# https://leetcode.com/problems/two-sum/

class Solution:
    # Two-Pointer is inefficient bc original indicing needs to be remembered
    # Using dictionary to track complement presence is more effective
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for idx, num in enumerate(nums): 
            if freq.get(target-num, -1) == -1:    # If complement not present, 
                freq[num] = idx                 # Map current num & idx
            else:                               # If present,
                return [freq[target-num], idx]  # Return comp's idx & num's idx
