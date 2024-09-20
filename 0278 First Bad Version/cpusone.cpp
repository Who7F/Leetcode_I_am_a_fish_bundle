// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int lit = 0;
        while(lit < n){
            int anc = lit + (n - lit)/2;
            if(isBadVersion(anc))
                n = anc;
            else
                lit = anc +1;
        }
        return n; 
    }
};