# https://leetcode.com/problems/permutations/?envType=study-plan&id=algorithm-i

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        size = len(nums)

        def recurse(combo: List[int], rem: List[int]):
            if len(combo) == size:  # All numbers used
                output.append(combo.copy())
            else:                   
                for x in range(len(rem)): # Iterate through all available number via indices
                    combo.append(rem.pop(x))        # Pop element at 'x' index & append to combo
                    recurse(combo, rem)
                    rem.insert(x, combo.pop())      # Pop element from combo & insert to 'x' index
                    
        recurse([], nums.copy())

        return output
