class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<int> seen;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if (seen.contains(10 * i + int(board[i][j])) ||
                        seen.contains(10 * j + int(board[i][j]) + 100) || 
                        seen.contains(10 * (j/3 + (i/3 * 3)) + int(board[i][j]) + 200)
                        ) {
                            return false;
                    }
                    seen.insert(10 * i + int(board[i][j]));
                    seen.insert(10 * j + int(board[i][j]) + 100);
                    seen.insert(10 * (j/3 + (i/3 * 3)) + int(board[i][j]) + 200);
                }
            }
        }
        return true;
    }
};