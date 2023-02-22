class Solution {

    public String countAndSay(int n) {
        if (n==1) {     // Base case
            return "1";
        }

        String prev = countAndSay(n-1); // Recurse until base case met

        StringBuilder sb = new StringBuilder();
        int quantity = 1;
        int str_length = prev.length();

        // Iterate through string's characters
        for (int i = 0; i < str_length; i++) {
            // If last element or next char is different...
            if (i == str_length-1 || prev.charAt(i) != prev.charAt(i+1)) {
                sb.append(Integer.toString(quantity) + prev.charAt(i) + ""); // Append to string and reset quantity
                quantity = 1;
            } else {    // If not, increment quantity
                quantity += 1;
            }
        }
        
        // Return formed string to prev executions until finished
        return sb.toString();
    }
}
