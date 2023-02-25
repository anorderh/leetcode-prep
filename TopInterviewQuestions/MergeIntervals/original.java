class Solution {
    public int[][] merge(int[][] intervals) {
        /*
        Merge overlapping intervals into 1 array
        Output of intervals w/ no overlap

        Tasks
        - Identify when overlap occurs
        - keep track of new max and upcoming min

        Brute-force appraoch
        - Check every interval for overalp
        
        Place elements in reverse onto a stack & pop 2 intervals
        Events...
        - If overlapping, merging and place onto stack
        - If not overallping, add 1st to output and add 2nd back to stack
      
        Time Complexities
        Time - O(2n) or O(2n * log(n))
        Space - O(2n)

        Unfortunately I can't realistically test this due to Java's primitive typing & conversion
        between Integer and int. This is not the solution.
        */

        Stack<Integer[]> stack = new Stack<>();
        List<Integer[]> output = new ArrayList<>();
        
        // put all intervals onto stack
        for (int i = intervals.length-1; i >= 0; i--) {
            stack.push(Arrays.stream(intervals[i]).boxed().toList());
        }

        // begin processing stack
        while (!stack.empty()) {
            if (stack.size() == 1) {    // only 1 interval, add to output
                output.add(stack.pop());
            } else {                    // >= 2 intervals, pop
                int[] startArr = stack.pop();
                int[] activeArr = stack.pop();

                if (startArr[1] > activeArr[0]) { 
                    // overlap found, combine & add back to stack
                    stack.push( new int[]{startArr[0], activeArr[1]} );
                } else { 
                    // isolated interval found, add & return activeArr
                    output.add(startArr);
                    stack.push(activeArr);
                }
            }
        }

        return output;
    }
}
