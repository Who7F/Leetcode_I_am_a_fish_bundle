class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> anc;

        int i = 0;

        while (i < nums.size()) {
            int start = nums[i];

            while (i < nums.size() -1  && nums[i] + 1 == nums[i + 1]) {
                i ++;
            }

            if (start == nums[i]) {
                anc.push_back(to_string(start));
            } else {
                anc.push_back(to_string(start) + "->" + to_string(nums[i]));
            }
            i ++;
        }
        return anc;
    }
};
