class Solution {
public:
    int findMin(vector<int>& nums) {
        int lit = 0;
        int big = nums.size() - 1;
        
        while(lit < big){
            int mid = lit + (big - lit) / 2;
            if (nums[mid] > nums[big])
                lit = mid + 1;
            else 
                big = mid;
        }
        return nums[lit];
    }
};