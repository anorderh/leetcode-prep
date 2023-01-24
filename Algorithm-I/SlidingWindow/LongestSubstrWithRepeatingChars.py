# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan&id=algorithm-i

# My solution, using 2 pointerse & dict to track frequencies
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: # edge case
            return len(s)
        length = 1

        start = end = 0 # two pointers
        freq = {s[end]:1} # Sliding Window

        while end < len(s): # While end not reached
            maxFreq = max(freq.values()) # max freq

            print(f"s: {start}, e: {end}, max: {length}, maxFreq: {maxFreq}")

            if maxFreq > 1: # invalid string -> increment start
                freq[s[start]] = freq.get(s[start], 0) - 1
                start += 1
            else: # valid string
                if (end+1-start > length): # check if max length
                    length = end+1-start
                end += 1 # increment end ptr
                if (end != len(s)): # if end not reached, add next freq
                    freq[s[end]] = freq.get(s[end], 0) + 1

        return length

    # Leetcode solution, dict tracking indices -- not frequencies
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # Dict tracking indices
        l = 0 # Start of window
        output = 0
        for r in range(len(s)):
            # If new char, check for max length
            if s[r] not in seen:
                output = max(output,r-l+1)
            else:
                if seen[s[r]] < l: # If outside window, check for max length
                    output = max(output,r-l+1)
                else: # If inside window, initialize start w/ char's index + 1
                    l = seen[s[r]] + 1
                     
            seen[s[r]] = r # Add index to dict
        return output

