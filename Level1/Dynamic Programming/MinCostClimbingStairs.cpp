// https://leetcode.com/problems/min-cost-climbing-stairs/description/
// Dynamic Programming
// creds @avval on leetcode.com
// Recursive -> Bottom-up Dp

class Solution {
public:
    // recursive, finding minCost of steps 1 & 2 back
    int minCostClimbingStairs(vector<int>& cost) {
        int size = cost.size();
        return min(minCost(cost, size-1), minCost(cost, size-2));
    }

    int minCost(vector<int>& cost, int n) {
        if (n < 0) {return 0;}
        if (n==0 || n==1) {return cost[n];}
        return cost[n] + min(minCost(cost, n-1), minCost(cost, n-2));
    }

    // iterative, same relation but removing recursive stack
    int minCostClimbingStairs(vector<int>& cost) {
        int length = cost.size();
        int first = cost[0];
        int second = cost[1];
        if (length <= 2) {return min(first, second);}

        for (int i = 2; i < length; i++) {
            int curr = cost[i] + min(first, second);
            first = second;
            second = curr;
        }

        return min(first, second);
    }
};
