import heapq
class Solution:
    def getDeltas(self, start, n, h, seen, grid):
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i, j = start

        for d in delta:
            x, y = d
            di, dj = i + x, j + y

            if 0 <= di < n and 0 <= dj < n and seen[di][dj] == 0:
                heapq.heappush(h, (grid[di][dj], di, dj))

            

    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        h = [(grid[0][0], 0, 0)]

        seen = [[0 for i in range(n)] for j in range(n)]
        res = 0

        while h:
            cost, i, j = heapq.heappop(h)

            if seen[i][j] == 1:
                continue
            
            res = max(res, cost)

            if [i, j] == [n -1, n-1]:
                return  res

            seen[i][j] = 1
            self.getDeltas([i, j], n, h, seen, grid)
            
        return -1