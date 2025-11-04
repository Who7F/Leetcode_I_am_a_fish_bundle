class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        
        int row = grid.size();
        int col = grid[0].size();
        vector<pair<int, int>> deltas = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        queue<pair<int, int>> que;
        int fresh = 0;
        int time  = 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 2) {
                    que.push({i, j});
                } else if (grid[i][j] == 1) {
                    fresh ++;
                }
            }
        }

        while (!que.empty()) {
            int queSize = que.size();
            for (int q = 0; q < queSize; q++) {
                auto [r, c] = que.front();
                que.pop();
                for (auto [dr, dc]: deltas) {
                    int nr = dr + r;
                    int nc = dc + c;
                    if (nr >= 0 && nr < row && nc >= 0 && nc < col && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        que.push({nr, nc});
                        fresh --;                     
                    }
                }
            }
            
            if (!que.empty()) {
                time ++;
            }
        }

        return (fresh == 0) ? time: -1;
    }
};