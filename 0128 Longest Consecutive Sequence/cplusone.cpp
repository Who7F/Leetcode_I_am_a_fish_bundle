class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        std::unordered_set<int> num(nums.begin(), nums.end());
        int res = 0;
        
        for(int n : num){
            if (num.find(n - 1) == num.end()){

                int length = 1;
                while(num.find(n + length) != num.end()){
                    length++;
                }
                res = max(res, length);
            }
        }

    return res;
    }
};
