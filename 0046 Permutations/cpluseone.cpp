// Recursive
// Gets all the possible permutations
// Object-oriented design

class Solution {
private:
    vector<vector<int>> res;
    vector<int> temp;
    vector<bool> visited;

    void findPermuta(vector<int> nums){
        if(temp.size() == nums.size()){
            // Adds base case (current subset to results)
            res.push_back(temp);
        }else{
            for(size_t i = 0; i < nums.size(); ++i){
                if (!visited[i]){
                    visited[i] = true;
                    temp.push_back(nums[i]);
                    findPermuta(nums);
                    temp.pop_back();
                    visited[i] = false;
                }
            }
        }
    }
public:
    Solution() : res(), temp(), visited() {} 
    vector<vector<int>> permute(vector<int>& nums) {
        res.clear();
        temp.clear();
        visited.assign(nums.size(), false);
        // Start the recursive process
        findPermuta(nums);
        return res;
    }
};


