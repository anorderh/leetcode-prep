class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        # Iterate through strings
        for s in strs:
            char_freq = [0] * 26 # Track char freq via mapping ASCII to indexes
            for c in s:
                char_freq[ord(c) - ord('a')] += 1

            freq_str = str(char_freq) # Convert arr into str to be hashed

            if freq_str in freq: # If freq_str exists, append s
                freq[freq_str].append(s)
            else:                 # Else, use as new key
                freq[freq_str] = [s]
        
        return freq.values()
