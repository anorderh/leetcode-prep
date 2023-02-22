class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<>();
        Map<Character, Character> bracketLookup = new HashMap<>();
        
        // Bracket mapping
        bracketLookup.put(')', '(');
        bracketLookup.put('}', '{');
        bracketLookup.put(']', '[');
        
        // Iterate through string, use toCharArray
        for (char c : s.toCharArray()) {
            if (bracketLookup.containsKey(c)) { // Closing paren.
                // If stack not empty && matching char, pop()
                if (brackets.size() != 0 && brackets.peek() == bracketLookup.get(c)) {
                    brackets.pop();
                } else {
                    return false;
                }
            } else { // Opening paren
                brackets.push(c);
            }
        }

        if (brackets.size() == 0) return true;
        return false;
    }
}
