class Solution {
private:
    vector<string> res;
    void getCobinations(string digits, string letter_map[], string sol, int index) {
        
        if (index == digits.size()) {
            res.push_back(sol);
        } else {

            int target = digits[index] - '0';

            for(int i = 0; i < letter_map[target].size(); i++) {

                sol.push_back(letter_map[target][i]);
                getCobinations(digits, letter_map, sol, index + 1);
                sol.pop_back();
            }
        }
    }
  

public:
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0){
            return res;
        }
        
        string letter_map[10] = {"",    "",    "abc",  "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        getCobinations(digits, letter_map, "", 0);
        return res;
    }
};