class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Converting to lowercase & alphanumeric-only
        s = (''.join(c for c in s if c.isalnum())).lower()
        start, end = 0, len(s)-1

        # Two ptr approach
        while start < end:
            if (s[start] != s[end]): # Chars at opposite ends aren't == -> False
                return False
            else: # Chars are equal, incre/decre accordingly
                start += 1
                end -= 1

        return True
