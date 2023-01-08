// https://leetcode.com/problems/climbing-stairs/description/

class Solution {
public:
    int climbStairs(int n) {
        if (n == 0) {
            return 0;
        }
        int stairsA = 0; int stairsB = 1; int temp;

        for (int i = 2; i <= n; i++) {
            temp = stairsA + stairsB;
            stairsA = stairsB;
            stairsB = temp;
        }

        return stairsA + stairsB;
    }
};
