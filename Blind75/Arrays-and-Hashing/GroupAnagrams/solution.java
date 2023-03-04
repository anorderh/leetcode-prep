class Solution {

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>(); // families
        
        List<List<String>> res = new ArrayList<>();
        if (strs.length == 0) return res;
        
        // Iterate through strings
        for (String s : strs) {
            int[] hash = new int[26]; // Create freq array
            for (char c : s.toCharArray()) {
                hash[c - 'a']++; // Update freq, use char ASCII for indexing
            }
            
            // While an array can't be used itself as a key, it can
            // be converted into a String. 
            String key = new String(Arrays.toString(hash));

            // Initializes new ArrayList if key not present
            map.computeIfAbsent(key, k -> new ArrayList<>());
            map.get(key).add(s);
        }
        
        // Add values to result
        res.addAll(map.values());
        return res;
    }
}
