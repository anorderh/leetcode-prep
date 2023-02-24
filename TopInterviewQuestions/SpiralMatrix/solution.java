class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int height = matrix.length;
        int width = matrix[0].length;
        List<Integer> res = new ArrayList<>();

        // use pointers denoting boundaries
        // different implementations for top, bottom, left, and right
        // increment/decrement pointers to mark as processed

        int top = 0;
        int left = 0;
        int bottom = matrix.length;
        int right = matrix[0].length;

        while (top < bottom && left < right) {
            // process top row
            for (int i = left; i < right; i++) {
                res.add(matrix[top][i]);
            }
            top++;
            // process right column
            for (int i = top; i < bottom; i++) {
                res.add(matrix[i][right-1]);
            } 
            right--;

            if (top >= bottom || left >= right) { 
                break; // spirals end after processing columns - w/o this, row elements are rpeeated
            }

            // process bottom row
            for (int i = right-1; i >= left; i--) {
                res.add(matrix[bottom-1][i]);
            }
            bottom--;
            // process left column
            for (int i = bottom-1; i >= top; i--) {
                res.add(matrix[i][left]);
            }
            left++;
        }

        return res;
    }
}
