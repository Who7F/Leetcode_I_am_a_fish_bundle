class Solution {
private:
    vector<string> res;
    void getPairs(string sol, int left, int right) {
        if (left + right == 0) {
            res.push_back(sol);
            return;
        }

        if (left > 0) {
            getPairs(sol + '(', left - 1, right + 1);
        }

        if (right > 0) {
            getPairs(sol + ')', left, right - 1);
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        res.clear();
        getPairs("", n, 0);
        return res;
    }
};