class Solution {
    public int maxSubArray(int[] nums) {
        // Find a subarray within given array
        // To maintain subarray, order must be preserved in orig structure

        // Possible approaches:
        // - Calculating net gain/loss over certain indices
        // - Sorting? X, remove order of array
        // - Total sum?

        // checking if element is greater than 1 to the right

        int sum = Arrays.stream(nums).sum();
        int largest = sum;
        int start = 0; int end = nums.length-1;

        while (start < end) { // If equals, 1 element is considered. Past this is invalid.
            // compare both ends
            if (nums[start] < nums[end]) {
                sum -= nums[start];
                start += 1;
            } else {
                sum -= nums[end];
                end -= 1;
            }

            // compared with stored largest
            if (sum > largest) {
                largest = sum;
            }
        }

        return largest;
    }
}
