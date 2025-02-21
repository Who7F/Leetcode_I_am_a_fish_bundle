class Solution {
private:
    vector<int> sol;
    vector<vector<int>> res;

    void getSum(int target, int index, int l, vector<int>& candidates){
        if(l == target){
            res.push_back(sol);
            return;
        }

        if(l > target){
            return;
        }

        for(int i = index; i < candidates.size(); i++){
            sol.push_back(candidates[i]);
            getSum(target, i, l + candidates[i], candidates);
            sol.pop_back();
        }
    }

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        res.clear();
        sol.clear();
        getSum(target, 0,  0, candidates);
        return res;
    }
};