class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> seen;

        for (auto &s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            seen[key].push_back(s);
        }
        
        vector<vector<string>> res;

        for (auto &[_, s] : seen) {
            res.push_back(s);
        } 

        return res;
    }
};