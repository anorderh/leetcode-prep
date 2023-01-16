// https://leetcode.com/problems/last-stone-weight/description/

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq(stones.begin(), stones.end());
        int stoneA; int stoneB;

        while (pq.size() > 1) {
            stoneA = pq.top(); pq.pop(); // largest element
            stoneB = pq.top(); pq.pop(); // 2nd largest element

            if (stoneA != stoneB) { // if stoneA == stoneB, both stones destroyed and none added
                pq.push(stoneA-stoneB);
            }
        }
        
        return (!pq.empty() ? pq.top() : 0);
    }
};

