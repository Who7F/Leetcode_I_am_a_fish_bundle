class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int anc = INT_MAX;
        int low = 0;
        int ttl = 0;

        for(int i = 0; i < nums.size(); i++){
            ttl += nums[i];
            while(ttl >= target){
                anc = min(anc, i - low + 1);
                ttl -= nums[low];
                low ++;
            }
        }

        return anc == INT_MAX ? 0 : anc;
    }
};