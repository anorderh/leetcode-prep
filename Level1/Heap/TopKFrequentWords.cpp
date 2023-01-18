// https://leetcode.com/problems/top-k-frequent-words/description/

class Solution {
public:
    // My Solution, beats 49.77% CPU, beats 58% memory
    // Initializing word freq, then manually sorting keys into vector
    vector<string> topKFrequent(vector<string>& words, int k) {
        map<string, int> freq = {};
        vector<string> result;

        // init freq
        for (string word: words) {
            freq[word] += 1;
        }

        // init vector w/ 1st key & begin comparing later keys
        result.push_back(freq.begin()->first);
        for (map<string, int>::iterator it = next(freq.begin(), 1); it != freq.end(); it++) {
            int pos = 0;

            // new pos - based on ascending order
            // 'for' loop to avoid out of bounds indexing
            for (int i = 0; i < result.size(); i++) {
                if (freq[it->first] > freq[result[i]]) {
                    break;
                }
                pos++;
            }

            // sorting per lex order
            if (pos < result.size() && freq[it->first] == freq[result[pos]]) {
                pos += (it->first > result[pos]) ? 1 : 0;
            }
            result.insert(result.begin() + pos, it->first);
        }
        
        return {result.begin(), result.begin()+k};
    }

   // Leetcode solution,
   // Using priority queue w/ tuples & implementing custom Comparator for lexographical order
    
   vector<string> getTopKFreqStrings(vector<string> &words, int k) {
   	int n = words.size();

   	unordered_map<string, int> freq;

   	for(string word : words) {
     	   freq[word]++;
   	}

   	priority_queue<psi, vector<psi>, myComparator> pq;

   	for(auto it : freq) {
     	   pq.push({it.second, it.first});

     	   if(pq.size() > k) {
              pq.pop();
     	   }
   	}	 

   	vector<string> ans(k);
   	int m = k-1;

   	while(pq.size() > 0) {
           ans[m--] = pq.top().second;
           pq.pop();
   	}	 

        return ans;
   }	
};

class myComparator {
  public:
    bool operator() (const psi &p1, const psi &p2) {
      if(p1.first == p2.first) return p1.second < p2.second;
      
      return p1.first > p2.first;
    }
}    
