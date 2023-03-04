class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<HashMap<Character, Integer>, List<String>> fams = new HashMap<>();
        
        // Iterate through every string
        for (String str: strs) {
            HashMap<Character, Integer> fam = deriveCounter(str);

            if (fams.containsKey(fam)) { // Fam present, add str to list
                fams.get(fam).add(str);
            } else {    // Fam not present, allocate w/ new ArrayList
                fams.put(fam, new ArrayList<String>(Collections.singletonList(str)));
            }
        }

        // Create dynamic 'output' and add all values 
        List<List<String>> output = new ArrayList<>();
        output.addAll(fams.values());
        
        return output;
    }

    // Pulls associated frequency table with string
    public HashMap<Character, Integer> deriveCounter(String input) {
        HashMap<Character, Integer> freq = new HashMap<>();

        // Counts char occurence
        for (char letter: input.toCharArray()) {
            Character chr = Character.valueOf(letter);
            Integer count = freq.containsKey(chr) ? freq.get(chr) : 0;

            freq.put(chr, count+1);
        }
        return freq;
    }
}
