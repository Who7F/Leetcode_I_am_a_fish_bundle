class Solution:
    def getIslands(self, i, j, grid, deltas):
        stack = [(i, j)]
        while stack:
            i, j = stack.pop()
        
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    stack.extend((i + di, j + dj) for di, dj in deltas)
                    


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        islands = 0
        deltas = [(1, 0),(-1, 0),(0, 1),(0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    self.getIslands(i, j, grid, deltas)

        return islands
