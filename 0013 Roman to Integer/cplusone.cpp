class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> numeralMap = {
            {'I', 1}, {'V', 5}, {'X', 10}, 
            {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
        };
        int anc = 0;
        for(int i = 0; i < s.size(); i++){
            if (numeralMap[s[i]] < numeralMap[s[i+1]])
                anc -= numeralMap[s[i]];
            else
                anc += numeralMap[s[i]];
        }
        return anc;
    }
};