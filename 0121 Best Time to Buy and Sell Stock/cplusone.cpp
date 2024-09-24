class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = prices[0];
        int h = 0;
        int anc = 0;

        for(auto& i : prices){
            if(i > h){
                h = i;
                if (h - l > anc){
                    anc = h - l;
                }                
            }
            if (i < l){
                l = i;
                h = i;
            }
        }
        return anc;    
    }
};