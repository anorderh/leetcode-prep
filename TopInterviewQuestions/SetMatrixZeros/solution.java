class Solution {
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        boolean firstRow = false; // Constant memory, tracking 1st row's 0 status

        // Check for 0s and modify 1st row & 1st column accordingly
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    
                    // Mark ROW - for tracking columns
                    matrix[0][j] = 0;

                    // Mark COLUMN -  for tracking rows (use 'firstRow' if [0][0])
                    if (i == 0) {
                        firstRow = true;
                    } else {
                        matrix[i][0] = 0;
                    }
                }
            }
        }

        // Process matrix values EXCLUDING 1st row & column
        // [ X X X ]
        // [ X 0 0 ]
        // [ X 0 0 ]
        for (int i = 1; i < rows; i++) {
            for (int j = 1; j < cols; j++) {
                if (matrix[0][j] == 0 || matrix[i][0] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Check if 1st column contains 0 
        if (matrix[0][0] == 0) {
            for (int i = 0; i < rows; i++) {
                matrix[i][0] = 0;
            }
        }

        // Check if 1st row contains 0
        if (firstRow) {
            for (int j = 0; j < cols; j++) {
                matrix[0][j] = 0;
            }
        }
    }
}
