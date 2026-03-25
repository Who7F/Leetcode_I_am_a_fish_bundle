class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        
        res = [[1] * cols for _ in range(rows)]
        mod = 12345
        
        prefix = 1
        for i in range(rows):
            for j in range(cols):
                res[i][j] = prefix 
                prefix = (prefix * grid[i][j]) % mod
        
        suffix = 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                res[i][j] = (res[i][j] * suffix) % mod
                suffix = (suffix * grid[i][j]) % mod
        
        return res
