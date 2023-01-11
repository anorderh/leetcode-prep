# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# Sliding Window
# 24/37 testcases passed, using Dict to track char freq and tracking swaps
# TLE exceeded for large input, likely "max(freq.values())"

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        s_len = len(s)

        for start in range(s_len):
            end = start+1
            
            freq = {}
            freq[s[start]] = 1

            while len(s[start:end]) - max(freq.values()) <= k and end <= s_len:
                if end-start > length:
                    length = end-start
                if end == s_len:
                    break
     
                end += 1 
                freq[s[end-1]] = freq.get(s[end-1], 0) + 1

        return length

# Sliding Window, user solution @lee215
class Solution:
    def characterReplacement(self, s, k):
        maxf = i = 0
        count = collections.Counter()
        for j in range(len(s)):
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])
            if j - i + 1 > maxf + k:
                count[s[i]] -= 1
                i += 1
        return len(s) - i
