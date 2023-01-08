// https://leetcode.com/problems/longest-palindrome/description/?envType=study-plan&id=level-1

class Solution {
public:
    int longestPalindrome(string s) {
        int length = 0;
        bool oddFound = false;
        int library[58] = {0};

        for (char a: s) {
            library[a - 65] += 1;
        }

        for (int count: library) {
            if (count % 2 == 0) {
                length += count;
            } else {
                oddFound = true;
                length += count-1;
            }
        }

        return oddFound ? length+1 : length;
    }
};
