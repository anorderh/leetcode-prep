# https://leetcode.com/problems/permutation-in-string/submissions/884643802/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ctr = Counter(s1) # s1 char freq
        length = len(s1)

        for i in range(len(s2)): # iterating through s2
            if (s2[i] in ctr): # char in s1, decrement freq
                ctr[s2[i]] -= 1
            
            # if window expands past length, 1st char must be removd.
            # if in ctr, ctr must be incremented
            # if not in ctr, ignore bc s1 freq not affected
            if i >= length and s2[i-length] in ctr:
                ctr[s2[i-length]] += 1
            
            # all freqs are 0, valid permutation
            if not any(ctr.values()):
                return True
        
        return False
