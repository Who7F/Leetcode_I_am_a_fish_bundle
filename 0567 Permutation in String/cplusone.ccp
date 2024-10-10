class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.size() > s2.size())
            return false;

        vector<int> cntS1(26, 0), cntS2(26, 0);
        
        for(int i = 0; i < s1.size(); i++){
            cntS1[s1[i] - 97]++;
            cntS2[s2[i] - 97]++;
        }

        if(cntS1 == cntS2)
            return true;

        for(int i = s1.size(); i < s2.size(); i++){
            cntS2[s2[i] - 97]++;
            cntS2[s2[i - s1.size()] - 97]--;
            if(cntS1 == cntS2)
                return true;
        }
        return false;
    }
};