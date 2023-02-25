class Solution {

    public boolean canJump(int[] nums) {
        int goal = nums.length - 1;

        // iterate nums in reverse, starting at 2nd last idx
        for (int i = nums.length - 2; i >= 0; i--) {
            // if jumps+idx can reach goal, idx is new goal
            if (nums[i] + i >= goal) {
                goal = i;
            }
        }

        // if a path exists, goal should be 0
        // else goal is > 0 i.e. no path present
        return goal == 0;
    }
}
