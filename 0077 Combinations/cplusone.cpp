// Object-oriented design
// recursive
// Finds base sebset

class Solution {
private:
    vector<int> sol;
    vector<vector<int>> res;
    int con;

    void findNumbers(int n){
        if(sol.size() == con){
            // Adds base case (current subset to results)
            res.push_back(sol);
        }else{
            // Left branch (exclude current element)
            if(n > con - sol.size())
                findNumbers(n - 1);
            
            // Right branch (include current element)
            sol.push_back(n);
            findNumbers(n - 1);
            sol.pop_back();
        }
    }
public:
    // Constructor initializes member variables
    Solution() : sol(), res(), con(0) {} 

    vector<vector<int>> combine(int n, int k) {
        con = k; 
        sol.clear();
        res.clear();
        findNumbers(n);
        return res;
    }
};