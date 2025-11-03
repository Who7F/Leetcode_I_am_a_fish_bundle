class Solution:
    def bfs(self, grid, que, fresh):
        deltas = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        row = len(grid)
        col = len(grid[0])

        time = 0

        while que:
            size = len(que)

            for _ in range(size):    
                x, y = que.popleft()
                for dx, dy in deltas:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                        que.append([nx, ny])
                        fresh -= 1
                        grid[nx][ny] = 2
            if que:
                time += 1
                
        
        return time if fresh == 0 else -1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        que = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        return self.bfs(grid, que, fresh)
