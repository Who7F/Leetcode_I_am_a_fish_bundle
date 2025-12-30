class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        vector<int> count(26, 0);

        for (auto i : s) {
            count[i - 'a']++;
        }

        for (auto i : t) {
            if (count[i - 'a'] == 0) {
                return false;
            }
            count[i - 'a']--;
        }

        return true;    
    }
};