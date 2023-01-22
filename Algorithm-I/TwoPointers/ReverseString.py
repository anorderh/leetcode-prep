# https://leetcode.com/problems/reverse-string/?envType=study-plan&id=algorithm-i

class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s)-1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
