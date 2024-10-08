class Solution {
public:
    int characterReplacement(string s, int k) {
        int anc = 0;
        vector<int> count(128);
        int low = 0;
        int maxCnt = 0;
        for(int i = 0; i < s.length(); i++){
            count[s[i]] ++;
            maxCnt = max(maxCnt, count[s[i]]);

            if(i - low + 1 - maxCnt > k){
                count[s[low]] --;
                low ++;
            }
            anc = max(anc, i - low + 1);
        }
        return anc;
    }
};