class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> seen;
        for (auto n : nums) {
            seen.insert(n);
        }

        return nums.size() != seen.size();
    }
};