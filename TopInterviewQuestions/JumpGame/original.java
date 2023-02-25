class Solution {
    public boolean canJump(int[] nums) {
        /*
        Constraints:
        - max # of jumps at each index can be 0
        - num length must be atleast 1

        Goal:
        Figure out if you can reach end.
        Initially at index 0

        [2,3,1,1,4]

        Val is max # of jumps, 'm'
        But you can travel to any point [1, m]
        Meaning [1,m] points open up
        */
        return recurse(nums, 0);
    }

    // Time - O(n^2), varying based on checking shorter jumps or larger jumps fit the input array
    // Memory - O(m) where m is recursive calls on stack
    public static boolean recurse(int[] nums, int index) {
        if (index >= nums.length-1) { // idx is at or exceeds last index
            return true;
        }

        boolean res = false;
        int jumps = nums[index]; // finding jumps available
        while (jumps > 0 && !res) { // recursing to furthest indices 
            res = recurse(nums, index+jumps); // if true, exit for-loop
            jumps--;
        }


        return res;
    }
}
