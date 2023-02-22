class Solution {
    // Steps:
        // 1. Split string into minimal number of substrings
        // 2. For each substring, say # of digits & digit
        // 3. Concentate every said digit

        // countAndSay(n) is way you would say digit string from (n-1)
        // countAndSay(n) - you SAY the digit string from n-1

        // Ex:
        // countAndSay(1) = 1
        // countAndSay(2) = "one 1" = 11
        // countAndSay(3) = "two 1s" = 21
        // countAndSay(4) = "one 2 one 1" = 1211
        // countAndSay(5) = "one 1 one 2 two 1s" = 111221

        // Process:
        // 1. Recurse to first case
        // 2. Represent value as literal string
        // 3. Consider string as value & progressively convert to literal. (recurse)

    public String countAndSay(int n) {
        String literal = "";

        // Recurse until 2, return "1" if 1
        if (n == 1) {
            return "1";
        } else if (n != 2) {
            literal = countAndSay(n-1);
        } else {
            literal = "1";
        }

        // Convert 'literal' to 'spoken'
        ArrayList<String[]> occurences = new ArrayList<>();
        String[] group = new String[2];
        int quantity = 0;

        for (int i = 0; i < literal.length(); i++) {
            String val = literal.charAt(i) + "";

            if (!val.equals(group[1])) { // New char
                if (group[1] != null) { // Prev char isn't null
                    // Adding to reccurences and reallocating
                    occurences.add(group);
                    group = new String[2];
                }
                group[1] = String.valueOf(val);
                quantity = 0;
            }

            // Updating group
            quantity++;
            group[0] = Integer.toString(quantity);

            if (i+1 == literal.length()) { // Last char, add group
                occurences.add(group);
            }
        }

        // Convert occurences structuire to String
        StringBuilder sb = new StringBuilder("");
        for (String[] pair: occurences) {
            sb.append(pair[0] + pair[1] + "");
        }
        return sb.toString();
    }
}
