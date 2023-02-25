class Solution {
    public int[][] merge(int[][] intervals) {
        // Sort.
        List<int[]> sorted = Arrays.asList(intervals);
        sorted.sort((a, b) -> Integer.compare(a[0], b[0]));

        // Merge overlaps.
        Stack<int[]> output = new Stack<>();
        int[] latest; int[] curr;

        output.push(intervals[0]);  // Init output with first interval.
        for (int i = 1; i < sorted.size(); i++) { // Iterate over remaining.
            latest = output.peek();
            curr = intervals[i];

            if (latest[1] >= curr[0]) {
                latest[1] = Math.max(latest[1], curr[1]);    // Overlap found, update latest interval.
            } else {                        
                output.push(curr);      // No overlap, add curr interval.
            }
        }

        return output.toArray(new int[output.size()][2]);
    }
}
