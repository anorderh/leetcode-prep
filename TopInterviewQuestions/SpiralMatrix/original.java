class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int height = matrix.length;
        int width = matrix[0].length;

        // gets first row
        // gets 2nd row
        // - change 2nd row into last column

        // process:
        // 1st row
        // last column
        // last row
        // 1st column
        // THEN REPEAT

        int cycles = 0; // For switching between row & column
        int offset = 0; // For calculating row offset
        boolean rowEnd = false;
        boolean columnEnd = false;

        // Process 1st row with no boudnaries
        rowEnd = getRow(0, 0, 0, false);
        cycles++;

        while (!rowEnd &&  !columnEnd) {
            if (cycles%2) { // process row
                if (cycles == 0) { // deciding 'right' or 'left'
                    rowEnd = getRow(x, 1+offset, offset, false)
                } else {
                    rowEnd = getRow(x, 1+offset, offset, true)
                }
            } else {        // process column
                if (cycles == 1) { // deciding 'down' or 'up'
                    columnEnd = rowEnd = getRow(x, 1+offset, offset, false)
                } else {
                    columnEnd = rowEnd = getRow(x, 1+offset, offset, true)
                }
            }

            cycles++;
            offset = cycles/4; // incrementing offset every complete trip
        }
    }

    public boolean getRow(int i, int start, int end, bool reverse) {
        if (!reverse) {
            for (int j = 0+start; j < width-end; j++) {
                add(matrix[i][j])
            }
        } else {
            for (int j = width-1-start; j >= 0+end; j--) {
                add(matrix[i][j])
            }
        }
    }

    public boolean getColumn(int i, int start, int end, bool reverse) {
        if (!reverse) {
            for (int j = 0+start; j < height-end; j++) {
                add(matrix[j][i])
            }
        } else {
            for (int j = height-1-start; j >= 0+end; j--) {
                add(matrix[j][i])
            }
        }
    }   
}
