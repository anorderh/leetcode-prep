# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        size = len(s)
        total = 0
        l = 0

        # Stop at size-1,to prevent idnex error
        while l < size-1:
            val_a, val_b = convert[s[l]], convert[s[l+1]]

            if val_a >= val_b:  # Left value greater, 1 digit considered
                total += val_a
                l += 1
            else:               # Right value greater, 2 digits considered
                total += val_b - val_a
                l += 2
        
        return total if l != size-1 else total + convert[s[l]]
