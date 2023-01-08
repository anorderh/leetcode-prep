// https://leetcode.com/problems/is-subsequence/solutions/?envType=study-plan&id=level-1

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int index = 0;
        int sub_size = s.length();

        for (int i = 0; i < t.length(); i++) {
            if (index > sub_size) {
                return true;
            } else if (s[index] == t[i]) {
                index++;
            }
        }

        return index >= sub_size;
    }
};
