class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int top = nums.size();
        int total = 0;

        for(int i = 0; i < k; i++)
            total += nums[i];

        int anc = total;

        for(int i = k; i < top; i++){
            total += nums[i];
            total -= nums[i - k];
            anc = max(anc,total);
        }
        return double(anc) / k;
    }
};