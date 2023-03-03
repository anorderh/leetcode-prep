class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): # If not same length, not an anagram
            return False

        freq = {}
        for c in s:     # Init map & increment freqs
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1

        for c in t:     # Decrement key freqs, return False if not present
            if c not in freq:
                return False
            else:
                freq[c] -= 1

        # If all values are not 0, freqs are diff. Return False, else True
        return not any(freq.values())
