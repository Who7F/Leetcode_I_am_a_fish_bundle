class Solution {
private: 
    bool EatsBananas(vector<int>& piles, int h, int bite){
        int n = 0;
        for(int p : piles){
            n += (p + bite - 1) / bite;
        }
        return n <= h;
    }
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int big = *max_element(piles.begin(), piles.end());
        int lit = 1;
        while (lit < big){
            int bite = lit + (big - lit) / 2;

            if(EatsBananas(piles, h, bite)){
                big = bite;
            }else{
                lit = bite + 1;
            }
        }
        return lit;
    }
};