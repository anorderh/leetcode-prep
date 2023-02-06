# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    # given a string, determine if parentheses are valid
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:   # If odd number, open parentheses will exist -> Invalid
            return False
        
        parentheses = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []

        for c in s:     # Through every char
            # If not present, open parentheses -> add to stack
            if c not in parentheses: 
                stack.append(c)
            # Closing parentheses - If stack empty (none open) or stack's top does not match -> Invalid
            elif not stack or stack.pop() != parentheses[c]: 
                return False
        
        return not stack        # True if stack is empty, False otherwise (open parentheses)
