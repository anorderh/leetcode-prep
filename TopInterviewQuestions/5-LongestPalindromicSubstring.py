# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    # Brute force & starting w/ longest substr to skip iterations
    # O(n^3) time complexity
    def longestPalindrome(self, s: str) -> str:
        # implementations...
        # iterate through str and check if reversal is same
        size = len(s)
        longest = ""

        for l in range(size):   # Iterate through every index
            if size-l < len(longest):    # If available space is less then longest pd already found
                break   

            for r in range(size, l, -1):    # Iterate through ending indices
                curr = s[l:r]

                if curr == curr[::-1] and len(longest) < r-l:     # Valid palindrome
                    longest = curr
                    break
        
        return longest

    # Recursive approach, expanding from middle for palindrome
    # Time complexity - O(n^2)
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):    # Iterating through every index
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res): 
                res = tmp

            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]: # While l & r are within bounds and s[l] == s[r]
            l -= 1; r += 1
        return s[l+1:r]
