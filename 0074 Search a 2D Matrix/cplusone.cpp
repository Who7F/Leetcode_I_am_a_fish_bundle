class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int lit = 0;
        int big = m * n - 1;
        while(lit <= big){
            int mid = lit + (big - lit) / 2;
            int midVal = matrix[mid/n][mid%n];
            if(midVal == target)
                return true;
            else if(midVal < target)
                lit = mid + 1;
            else
                big = mid - 1;
        }
        return false;
    }
};