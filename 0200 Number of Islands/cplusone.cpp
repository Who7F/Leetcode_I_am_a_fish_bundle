class Solution {
private:
    vector<vector<char>> grid;
    int row, col;
    vector<pair<int, int>> directions = {{0, 1},{1, 0},{0, -1},{-1, 0}};

    void getIslands(int i, int j) {
        vector<pair<int, int>> stack;
        stack.push_back({i, j});

        while(!stack.empty()){
            auto [i, j] = stack.back();
            stack.pop_back();

            if (i >= 0 && i < row && j >= 0 && j < col){
                if(grid[i][j] == '1') {
                    grid[i][j] = '0';

                    for (auto [di, dj] : directions){
                        stack.push_back({i + di, j + dj});
                    }
                }
            }
        }
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int islands = 0;
        this->grid = grid;
        row = grid.size();
        col = grid[0].size();

        for (int i = 0; i < row; i++){
            for (int j = 0; j < col; j++){
                if(this->grid[i][j] == '1') {
                    islands++;
                    getIslands(i, j);
                }
            }
        }
        
        return islands;
    }
};