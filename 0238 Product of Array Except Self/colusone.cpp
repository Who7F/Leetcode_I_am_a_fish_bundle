class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int l = nums.size();

        vector<int> anc(l, 1);

        int total = 1;

        for (int i = 0; i < l - 1; i++) {
            total *= nums[i];
            anc[i+1] *= total;
        }

        total = 1;

        for (int i = l - 1; i > 0; i--) {
            total *= nums[i];
            anc[i - 1] *= total;    
        }

        return anc;
        
    }
};
