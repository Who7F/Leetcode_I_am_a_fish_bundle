class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string anc = "";

        sort(strs.begin(), strs.end());

        int len = min(strs[0].size(), strs[strs.size() - 1].size());

        for (int i = 0; i < len; i++) {
            if (strs[0][i] != strs[strs.size() - 1][i]) {
                return anc;
            }
            anc += strs[0][i];
        }
        return anc;
    }
};