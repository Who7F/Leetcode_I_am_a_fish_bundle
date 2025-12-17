class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        set<char> j(jewels.begin(), jewels.end());
        int cnt = 0;
        for (auto s : stones)
            if (j.find(s) != j.end()) 
                cnt++;
        
        return cnt;
    }
};