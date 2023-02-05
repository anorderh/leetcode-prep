# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    # Queue implementation
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {        
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if not digits:
            return []
        queue = mapping[digits[0]].copy()
        i = 1

        while i < len(digits):          # Iterate through entire digit string
            end = len(queue)                # Store length - end signaling start of new combo-level
            letters = mapping[digits[i]].copy()    # Store new letters

            for _ in range(end):     # Iterate through all current combos   
                combo = queue.pop(0)

                for letter in letters:      # Create new combo
                    queue.append(combo + letter)
            
            i += 1
        
        return queue

