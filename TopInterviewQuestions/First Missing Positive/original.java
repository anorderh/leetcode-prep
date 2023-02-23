class Solution {
    public int firstMissingPositive(int[] nums) {
        // Smallest missing positive integer

        // When iterating, can't ignore the number if its larger since, smaller may come later
        // But... can ignore negative umbers

        // Possible approaches:
        // Use Counter and return smallest - X, Not constant memory
        // Finding min then returning "min-1" - X, Won't be *smallest* missing positive
        // Using linked list and connecting smallest terms, find the integer gap - X, Not constant memory
        // Tracking number of digits and using array to represent 10 digits, X - Doesn't check smaller terms w/ less digits than minimum
        
        int digitCount = null;
        int[] places = null;

        for (int num: nums) {
            if (digit > 0) { // Positive number
                int newCount = countDigit(num);

                if (digitCount == null or newCount < digitCount) { // If num has less digits than count
                    // Update and initialize new array
                    digitCount = newCount;
                    places = new int[10]
                }

                // Otherwise place into existing array
                places[num%10] = num;
            }
        }

        // Find and return missing number
        for (int = 0; i < places.length(); i++) {
            if (places[i] == null) {
                return (digitCount * 10) + i
            }
        }

        return null;
    }

    public int countDigit(int x) {
        int count = 0
        while (x != 0) {
            x = x/10;
            count++;
        }
        return count;
    }
}
