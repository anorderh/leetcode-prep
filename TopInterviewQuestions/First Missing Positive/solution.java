class Solution {
    public int firstMissingPositive(int[] nums) {
        int length = nums.length;
        
        // removing negatives
        for (int i = 0; i < length; i++) {
            if (nums[i] < 0) { // neg found, set to 0 
                nums[i] = 0;
            }
        }

        // mapping indices via negative signs
        for (int i = 0; i < length; i++) {
            int idx = Math.abs(nums[i]) - 1; // mapped index

            if (idx >= 0 && idx < length) { // check if valid range
                if (nums[idx] > 0) { // pos int, change to negative
                    nums[idx] *= -1;
                } else if (nums[idx] == 0) {  // 0, change to (-a+1), marks as exists
                    nums[idx] = -1 * (length+1); // by being > length, existing tracking is not altered!
                }
                // if negative already, duplicate element so ignore to maintain element tracking
            }
        }

        // checking element symbols
        for (int i = 1; i < length+1; i++) {
            if (nums[i-1] >= 0) { // positive or 0 means never mapped!
                return i;
            }
        }

        return length+1;
    }
}
