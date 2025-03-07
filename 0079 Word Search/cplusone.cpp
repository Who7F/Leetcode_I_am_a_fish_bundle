class Solution {
private:
    vector<vector<char>> board;
    string word;
    int row, col;

    bool findWord(int i, int j, int index){
        if (i < 0 || i >= row || j < 0 || j >= col) {
            return false;
        }

        if (board[i][j] != word[index]) {
            return false;
        }

        index ++;

        if(index == word.size()){
            return true;
        }

        vector<pair<int, int>> directions = {{0, 1},{1, 0},{0, -1},{-1, 0}};
        char temp = board[i][j];
        board[i][j] = '-';

        for (auto [dx, dy] : directions) {
            if (findWord(i + dx, j + dy, index)) {
                return true;
            }
        }

        board[i][j] = temp;
        return false;
    }


public:
    bool exist(vector<vector<char>>& b, string w) {
        board = b;
        word = w;
        row = board.size();
        col = board[0].size();
        
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (findWord(i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};