# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    # Bruteforce, direct comparison, TLE exceeded
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []

        p_len = len(p)
        for x in range(len(s)):
            temp = s[x:x+p_len]
            result = True

            for c in p:
                if c not in temp:
                    result = False
                    break
                else:
                    temp = temp.replace(c, "", 1)
            indices.append(x) if result else None
        
        return indices


    # Bruteforce, tracking ASCII total, incorrect
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        p_len = len(p)
        p_val = sum([ord(c) for c in p])

        for x in range(len(s)):
            if (sum([ord(c) for c in s[x:x+p_len]]) == p_val):
                indices.append(x)
        return indices

    # Sliding Window with HashMap, correct
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashMap, result, p_len, s_len = defaultdict(int), [], len(p), len(s)
        if p_len > s_len: return []

        # "Sliding Window" is hashmap of all corresponding frequencies
        # build hashmap
        for char in p: hashMap[char] += 1

        # initial full pass over the window
        for i in range(p_len-1):
            if s[i] in hashMap: hashMap[s[i]] -= 1
            
        # slide the window with stride 1
        for i in range(-1, s_len-p_len+1):
            if i > -1 and s[i] in hashMap:
                hashMap[s[i]] += 1
            if i+p_len < s_len and s[i+p_len] in hashMap: 
                hashMap[s[i+p_len]] -= 1
                
            # check whether we encountered an anagram
            if not any(hashMap.values()): 
                result.append(i+1)
                
        return result

