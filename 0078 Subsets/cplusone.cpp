// Recursive
// Finds base sebset
// Object-oriented design

// Number of subsets is 2^n. 2 branches at each step.
class Solution {
private:
    vector<vector<int>> anc;
    vector<int> temp;

    void getSub(vector<int>& nums, int i){
        if(i == nums.size()){
            // Adds base case (current subset to results)
            anc.push_back(temp); 
        }else{
            // Left branch (exclude current element)
            getSub(nums, i + 1);

            // Right branch (include current element)
            temp.push_back(nums[i]);
            getSub(nums, i + 1);
            temp.pop_back();
        }
    }

public:
    // Constructor initializes member variables
    Solution() : anc(), temp() {} 

    vector<vector<int>> subsets(vector<int>& nums) {
        // Start the recursive process
        getSub(nums, 0);
        return anc;
    }
};