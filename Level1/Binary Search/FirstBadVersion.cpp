// https://leetcode.com/problems/first-bad-version/description/

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long start, end, cur;
        start = 1;
        cur = end = n;
        
        while (!isBadVersion(cur) || isBadVersion(cur-1)) {
            if (isBadVersion(cur)) {
                end = cur-1;
            } else {
                start = cur+1;
            }
            cur = (end + start)/2;
        }

        return cur;

    }
};
