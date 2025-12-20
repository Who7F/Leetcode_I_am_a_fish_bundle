class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> seen;

        for (auto m : magazine) {
            if (seen.find(m) == seen.end()) {
                seen.insert({m, 1});
            } else {
                seen[m]++;
            }
        }

        for (auto r : ransomNote) {
            if (seen.find(r) == seen.end() || seen[r] == 0) {
                return false;
            } else {
                seen[r]--;
            }
        }

        return true;
    }
};