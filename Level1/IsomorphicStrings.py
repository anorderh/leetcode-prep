# https://leetcode.com/problems/isomorphic-strings/solutions/?envType=study-plan&id=level-1
# 1. start by how to recognize strings are in same format
# 2. start by how to recognize that multiple chars aren't mapped to one

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        results = []

        for curr in [s, t]:
            logged = {}
            counter = 'a'
            output = ""
            
            for x in curr:
                if logged.get(x, "") == "":
                    logged[x] = counter
                    output += counter
                    counter = chr(ord(counter) + 1)
                else:
                    output += logged[x]
            results.append(output)
        
        return results[0] == results[1]
