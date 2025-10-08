class Solution:
    def getIslands(self, i, j, grid, deltas): 
        island_size = 0
        stack = [(i, j)] 
        rows, cols = len(grid), len(grid[0])

        while stack: 
            i, j = stack.pop() 
            if i >= 0 and i < rows and j >= 0 and j < cols: 
                if grid[i][j] == 1: 
                    grid[i][j] = 0 
                    island_size += 1

                    stack.extend((i + di, j + dj) for di, dj in deltas)

        return island_size




    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        deltas = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        cnt = 0


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    cnt = max(cnt, self.getIslands(i, j, grid, deltas))

        return cnt
