# https://leetcode.com/problems/reverse-words-in-a-string-iii/?envType=study-plan&id=algorithm-i

# String splitting, list comprehension, and slicing reversal
# 80% speed, 10% space optimization
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split(" ")])

# Two Pointer per list<str> in split string
# 40% speed, 97% space optimization
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(w):
            start = 0
            end = len(w)-1

            while start < end:
                w[start], w[end] = w[end], w[start]
                start += 1
                end -= 1
            
            return "".join(w)
        
        words = s.split(" ")
        for x in range(len(words)):
            words[x] = reverse([*words[x]])

        return " ".join(words)

