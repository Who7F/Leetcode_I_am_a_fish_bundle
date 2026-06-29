class Solution:
    def checkLimit(self, x, y, n, m, seen):
        return x > -1 and x < n and y > -1 and y < m and not seen[x][y]

    def dfs(self, grid, n, m, seen, x, y):
        if (x, y) == (n - 1, m - 1):
            return True

        street = {1:(0, 2), 2:(1, 3), 3:(0, 3), 4:(2, 3), 5:(0, 1), 6:(1, 2)}
        delters = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        opposites = {0: 2, 1: 3, 2: 0, 3: 1}

        seen[x][y] = True

        for d in street[grid[x][y]]:
            di, dj = delters[d]
            dx, dy = x + di, y + dj

            if not self.checkLimit(dx, dy, n, m, seen):
                continue

            if opposites[d] not in street[grid[dx][dy]]:
                continue

            if self.dfs(grid, n, m, seen, dx, dy):
                return True


        return False


    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0]) 
        seen = [[False for _ in range(m)]for _ in range(n)]
        return self.dfs(grid, n, m, seen, 0, 0)
        
        return False
