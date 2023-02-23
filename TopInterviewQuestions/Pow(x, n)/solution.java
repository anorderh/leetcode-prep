class Solution {
    public double myPow(double x, int n) {
        double result = myPowRecurse(x, Math.abs(n));
        result = n < 0 ? 1.0/result : result;
        return result;
    }

    public double myPowRecurse(double x, int n) {
        // Base cases
        if (x == 0) { // 0 base, will always be 0
            return 0.0;
        }
        if (n == 0) { // 0 exponent, will always be 1
            return 1.0;
        }

        // Recursive step
        double result = myPowRecurse(x, n/2); // find half
        result *= result;                     // multiple by itself to get whole

        if (n % 2 != 0) {  // Factoring in any multiple remainders
            result *= x;
        }

        return result;
    }
}
