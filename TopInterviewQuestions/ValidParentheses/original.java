class Solution {
    public boolean isValid(String s) {
        // Parentheses stack & mappings
        Stack<String> stack = new Stack<>();
        HashMap<String, String> pairs = new HashMap<>();
        pairs.put("(", ")");
        pairs.put("{", "}");
        pairs.put("[", "]");

        String[] parts = s.split("");

        // Iterate through every char
        for (String letter: parts) {
            if (pairs.containsKey(letter)) {    // Opening paren. found, add ending to stack
                stack.push(pairs.get(letter));
            } else {                            // Closing paren. found, compare with stack's top
                if (stack.empty()) {   // No open pairs
                    return false;
                }

                String popped = stack.pop();
                if (!letter.equals(popped)) { // If not equal, improper paren. pair present
                    return false;
                }
            }
        }

        // True if stack empty, False if open pairs present
        return stack.empty();
    }
}
