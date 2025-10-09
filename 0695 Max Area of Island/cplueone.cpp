class Solution {
private:
    vector<vector<int>> grid;
    int row, col;
    vector<pair<int, int>> directions = {{0, 1},{1, 0},{0, -1},{-1, 0}};

    int AreaIsland(int i, int j){
        int cnt = 0;
        queue<pair<int, int>> q;
        q.push({i, j});


        while(!q.empty()){
            auto [x, y] = q.front();
            q.pop();
        
            if (x >= 0 && x < row && y >= 0 && y < col && grid[x][y] == 1){
                grid[x][y] = 0;
                cnt ++;
                for(auto [dx, dy]: directions){
                    q.push({x + dx, y + dy});
                }
            }
        }
        return cnt;
    }

public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int res = 0;
        this->grid = grid;
        row = grid.size();
        col = grid[0].size();

        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(this->grid[i][j] == 1){
                    res = max(res, AreaIsland(i, j));
                }
            }
        }
        return res;
    }
};