# https://leetcode.com/problems/combinations/?envType=study-plan&id=algorithm-i

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # range [1,n] -> numbers to be chosen
        # k -> spaces available

        # start programming for k = 2
        # make more obvious
        output = []

        # Recursion method
        def recurse(start: int, combo: List[int]):
            if (len(combo) == k):           # Check if combo is filled
                output.append(combo.copy()) # Get copy of reference variable
            else:                          
                # To get all combinations, each element must be greater than last during iteration
                for i in range(start, n+1): 
                    combo.append(i)         # Use 1 array as ref parameter, constantly append()/pop() to save space
                    recurse(i+1, combo)
                    combo.pop()
        
        recurse(1, [])
        return output
        
