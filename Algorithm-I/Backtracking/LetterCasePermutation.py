# https://leetcode.com/problems/letter-case-permutation/?envType=study-plan&id=algorithm-i

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = []
        size = len(s)

        def recurse(curr: str, idx: int):

            if idx >= size: # Base case, entire string iterated
                output.append(curr)
            else:
                if s[idx].isdigit(): # Skipping digits
                    recurse(curr + s[idx], idx+1)      # No tree change, continuing recursion
                else:
                    recurse(curr + s[idx].lower(), idx+1) # Recursing to lower char tree
                    recurse(curr + s[idx].upper(), idx+1) # Recursing to upper char tree

        recurse("", 0)

        return output

