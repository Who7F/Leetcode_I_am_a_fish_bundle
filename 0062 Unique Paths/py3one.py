class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[0] * (n+1) for _ in range(m+1)]

        grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                grid[i + 1][j] += grid[i][j]
                grid[i][j + 1] += grid[i][j]

        return grid[m-1][n-1]
