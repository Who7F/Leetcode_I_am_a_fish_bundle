class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dirs = [(0,1), (0, -1), (1,0), (-1,0)]
        n, m = len(grid), len(grid[0])
        seen = [[False for _ in range(m)] for _ in range(n)]

        def dfs(x, y, px, py, target):
            seen[x][y] = True
            for di, dj in dirs:
                dx, dy = di + x, dj + y
                if (px, py) != (dx, dy) and dx > -1 and dx < n and dy > -1 and dy < m and target == grid[dx][dy]:
                    if seen[dx][dy] or dfs(dx, dy, x, y, grid[i][j]):
                        return True

            return False
                    

        for i in range(n):
            for j in range(m):
                if not seen[i][j]:
                    if dfs(i, j, n, m, grid[i][j]):
                        return True

        return False