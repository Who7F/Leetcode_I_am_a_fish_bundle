class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        std::unordered_set<int> num(nums.begin(), nums.end());
        int res = 0;
        
        for(int n : num){
            if (!num.count(n - 1)){

                int length = 1;
                while(num.count(n + length)){
                    length++;
                }
                res = max(res, length);
            }
        }

    return res;
    }
};