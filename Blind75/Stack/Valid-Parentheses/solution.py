class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for b in s:
            if b not in pairs: # Open bracket
                stack.append(b)
            else:  # Closing bracket
                # No open pairs present OR non-corresponding brackets
                if not stack or stack.pop() != pairs[b]:
                    return False
        
        # True if list empty, False if values present
        return not stack
