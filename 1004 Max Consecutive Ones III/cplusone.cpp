class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int low = 0;
        int cnt = 0;
        int high = nums.size();

        for(int h = 0; h < high; h++){
            if(nums[h] == 0)
                cnt ++;

            if(cnt > k){
                if(nums[low] == 0)
                    cnt --;
                low ++;
            }    
        }
        return high - low;        
    }
};
