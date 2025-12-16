class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        int x = 0;
        int y = 0;
        int dx = 1;
        int dy = 0;

        vector<int> res;

        for (int i = 0; i < row * col; i++) {
            res.push_back(matrix[y][x]);
            matrix[y][x] = -101;

            if (!(0 <= x + dx && x + dx < col && 0 <= y + dy && y + dy < row) || matrix[y + dy][x + dx] == -101) {
                int temp = dx;
                dx = -dy;
                dy = temp;
            }

            x += dx;
            y += dy;

            cout << x + dx << " : ";
            cout << col << "\n";

        }

        cout << x;

        return res;  
    }
};