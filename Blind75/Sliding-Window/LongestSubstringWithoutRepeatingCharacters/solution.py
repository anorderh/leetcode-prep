class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        freq = {}
        start = 0

        for i in range(len(s)):
            if s[i] in freq:  # Repeat char
                longest = max(longest, len(freq))

                # Store dupes location
                loc = freq[s[i]]

                # Pop all terms before & at location
                for j in range(start, loc+1):
                    freq.pop(s[j])
                start = loc+1 # Update start
            
            freq[s[i]] = i
        
        return max(longest, len(freq))
