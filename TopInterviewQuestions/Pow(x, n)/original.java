class Solution {
    // 301/305 cases solved, Constant memory but O(n) runtime
    public double myPow(double x, int n) {
        // Implement exponent function
        // X can be negative, up to 100
        // N can be negative
        // N is always an integer

        // Exponents...
        // Can be positive
        // - Normal use case
        // Can be negative
        // - Divide 1 by term
        // Can be 0 
        // - Equal to 1

        // Base...
        // Can be positive
        // - No effect
        // Can be negative
        // - If exponent is even, keep positive. Else odd
        // Can be 0
        // - Return 0

        // Account for '0' exponent
        if (n == 0) {
            return 1.0;
        }
        // Account for '1' base
        if (x == 1) {
            return x;
        }

        double base = x;
        long limit = Math.abs((long)n);
        boolean negativeExp = n < 0 ? true: false;

        // Getting value
        for (int i = 1; i < limit; i++) { // Accounting for n = 1, ex: 5^1 = 5
            x *= base;
        }
        x = negativeExp ? 1.0/x : x;

        return x;
    }
}
