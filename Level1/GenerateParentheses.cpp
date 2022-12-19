// https://leetcode.com/problems/generate-parentheses/description/?envType=study-plan&id=1826693
// Generate Parentheses (Medium Leetcode difficulty in C++)
// - Requires recursion for binary branching with '(' and ')' characters
// - Pass vector<string> as ref varaible
// - Use counters to track open & closing parentheses, and desired string length

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> results;
        generate(results, "", n, 0, 0);
        return results;
    }

    void generate(vector<string>& results, string cur, int max, int open, int close) {
        // cout << cur << endl;

        if (cur.length() == max*2) {
            results.push_back(cur);
            return;
        } else {
            if (open < max) {
                generate(results, cur + "(", max, open+1, close);
            }

            if (close < open) {
                generate(results, cur + ")", max, open, close+1);
            }
        }
    }
};
