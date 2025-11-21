class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int total = nums[0];
        int curr = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            curr = max(nums[i], curr + nums[i]);
            total = max(total, curr);
        }

        return total;       
    }
};