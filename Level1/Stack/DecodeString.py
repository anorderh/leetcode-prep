#https://leetcode.com/problems/decode-string/description/

class Solution:

    def decodeString(self, s: str) -> str:
        stack = []; # Stack used incase of "repititions inside repititions""
        curNum = 0; 
        curString = ''

        for c in s: # Iterate over each char
            if c == '[': # repeating substr - START
                stack.append(curString) # store existing string
                stack.append(curNum) # store new string's recurrences

                # Reset values
                curString = ''
                curNum = 0
            elif c == ']': # repeating substr - END
                num = stack.pop()
                prevString = stack.pop()

                # properly updating w/ old string & new string's recurrences
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c) # accounts for numbers of multiple digits
            else:
                curString += c # char found, add into string
        return curString
