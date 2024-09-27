class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lit = 0;
        int big = nums.size() - 1;
        while(lit <= big){
            int mid = lit + (big - lit) / 2;
            if (nums[mid] == target)
                return mid;
            if(nums[lit] <= nums[mid]){
                if(nums[lit] <= target && target < nums[mid]){
                    big = mid - 1;
                }else{
                    lit = mid + 1;
                }
            }else{
                if(nums[mid] < target && target <= nums[big]){
                    lit = mid + 1;
                }else{
                    big = mid - 1;
                }
            }
        }
        return - 1;
    }
};