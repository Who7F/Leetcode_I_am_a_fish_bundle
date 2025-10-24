class Solution {
private:
    vector<pair<int, int>> bfs(vector<vector<int>>& heights, queue<pair<int, int>>& que) {
        int row = heights.size(),  col = heights[0].size();
        vector<pair<int, int>> res;
        vector<pair<int, int>> delta = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        vector<vector<bool>> visited(row, vector<bool>(col, false));

        while(!que.empty()){
            auto [r, c] = que.front();
            que.pop();

            if (visited[r][c]) continue;
            visited[r][c] = true;
            res.push_back({r, c});

            for (auto [dr, dc] : delta) {
                int nr = r + dr, nc = c + dc;
                if(nr >= 0 && nr < row && nc >= 0 && nc < col && !visited[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                    que.push({nr, nc});
                }
            }

        }
        return res;
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty() || heights[0].empty()) return {};
   
        queue<pair<int, int>> pacific;
        queue<pair<int, int>> atlantic;
        int row = heights.size(),  col = heights[0].size();

        for(int i = 0; i < row; i++){
            pacific.push({i, 0});
            atlantic.push({i, col - 1});
        }

        for(int j = 0; j < col; j++){
            pacific.push({0, j});
            atlantic.push({row - 1, j});
        }

        vector<pair<int, int>> pacSeen;
        vector<pair<int, int>> atlSeen;

        pacSeen = bfs(heights, pacific);
        atlSeen = bfs(heights, atlantic);

        set<pair<int,int>> pacSet(pacSeen.begin(), pacSeen.end());
        set<pair<int,int>> atlSet(atlSeen.begin(), atlSeen.end());

        vector<vector<int>> res;
    
        for (auto& cell : pacSet) {
            if (atlSet.count(cell)) {
                res.push_back({cell.first, cell.second});
                
            }
        }

        return res;
    }
};