// https://leetcode.com/problems/bulls-and-cows/description/?envType=study-plan&id=level-1

// Bulls & Cows
// Using map w/ queue to track char's available indices

class Solution {
public:
    string getHint(string secret, string guess) {
        map<char, queue<int>> freq = {}; // char -> (Indices)
        int bulls = 0;
        int cows = 0;

        // Adding indices to 'freq'
        for (int i = 0; i < secret.size(); i++) {
            if (secret[i] == guess[i]) { // If bull found, index ignored & char in 'guess' excluded
                bulls++;
                guess.replace(i, 1, "X");
            } else {
                freq[secret[i]].push(i);
            }
        }

        // Checking if 'guess[i]' exists at another index
        for (int i = 0; i < guess.size(); i++) {
            if (!freq[guess[i]].empty()) { // If empty, no other occurrences found
                cows++;
                freq[guess[i]].pop();
            }
        }

        return to_string(bulls) + "A" + to_string(cows) + "B";
    }
};
