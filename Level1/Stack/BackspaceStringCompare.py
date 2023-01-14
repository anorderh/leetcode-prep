# https://leetcode.com/problems/backspace-string-compare/description/?envType=study-plan&id=level-1

# Backspace Compare String
# Use 2 stacks & pop if '#' character found

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for x in range(max(len(s), len(t))):
            if x < len(s):
                s_stack.append(s[x]) if s[x] != '#' else (s_stack.pop() if s_stack else None)
            if x < len(t):
                t_stack.append(t[x]) if t[x] != '#' else (t_stack.pop() if t_stack else None)
        
        return s_stack == t_stack


