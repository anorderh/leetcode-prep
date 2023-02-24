class Solution {
    public int maxSubArray(int[] nums) {
        int sum = nums[0];
        int largest = sum;

        for (int i = 1; i < nums.length; i++) {
            // check prefix's sum
            if (sum < 0) {
                sum = 0;
            }

            // adjoin element
            sum += nums[i];

            // check sum
            if (sum > largest) {
                largest = sum;
            }
        }

        return largest;
    }
}
