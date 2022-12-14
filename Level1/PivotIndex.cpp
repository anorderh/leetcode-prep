// https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan&id=level-1
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum, leftSum;
        sum = leftSum = 0;

        for(int num: nums) { sum += num; }

        for(int i = 0; i < nums.size(); i++) {
            if (leftSum == (sum-leftSum-nums[i])) {
                return i;
            }
            leftSum += nums[i];
        }

        return -1;
    }
};
