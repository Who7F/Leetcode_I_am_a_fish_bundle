class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> seen;

        for (auto m : magazine) {
            seen[m]++;
        }

        for (auto r : ransomNote) {
            if (--seen[r] < 0) {
                return false;
            }
        }

        return true;
    }
};