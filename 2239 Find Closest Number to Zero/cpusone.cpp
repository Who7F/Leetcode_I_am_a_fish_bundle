class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int anc = nums[0];
        for(int i = 1; i < nums.size(); i++){
            if (abs(nums[i]) < abs(anc))
                anc = nums[i];
            if (abs(nums[i]) == abs(anc))
                anc = max(nums[i], anc);
            
        }
        return anc;
    }
};