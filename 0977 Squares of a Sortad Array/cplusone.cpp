class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        vector<int> res(nums.size(), 0);

        for (int i = nums.size(); i > 0; i--) {
            if (abs(nums[left]) > abs(nums[right])) {
                res[i - 1] = nums[left] * nums[left];
                left++;
            } else {    
                res[i - 1] = nums[right] * nums[right];
                right--; 
            }
        }

        return res;
    }
};
