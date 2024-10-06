class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int len = matrix.size();
        for(int i = 0; i < len; i++)
            for(int j = 0; j < i; j++){
                int store = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = store;
            }

        for(int i = 0; i < len/2; i++)
            for(int j = 0; j < len; j++){
                int store = matrix[j][i];
                matrix[j][i] = matrix[j][len - i - 1];
                matrix[j][len - i - 1] = store;
            }
    }
};