// https://leetcode.com/problems/two-sum/description/?envType=study-plan&id=level-1

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> indices;

        // initializing indices
        for(int i = 0; i < nums.size(); i++) {
            indices[nums[i]] = i;
        }

        // iterating thru indices & finding complement
        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            // complement present AND complement mapping != current index
            if (indices.count(complement) && indices[complement] != i)
                return {i, indices[complement]};
        }

        return {0, 0};
    }
};
