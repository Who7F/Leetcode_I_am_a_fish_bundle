class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int lit = 0;
        int big = nums.size() - 1;
        while(lit <= big){
            int anc = lit + (big - lit)/2;
            cout << anc;
            if(target > nums[anc])
                lit = anc + 1;
            else if(target < nums[anc])
                big = anc - 1;
            else
                return anc;
        }
        return lit;    
    }
};