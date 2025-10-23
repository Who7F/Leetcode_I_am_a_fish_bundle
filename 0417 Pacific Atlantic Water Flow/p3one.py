class Solution:
    def bfs(self, que, heights):
        seen = set(que)
        delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        row, col = len(heights), len(heights[0])

        while que:
            i, j = que.popleft()      
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if ni < row and nj < col and ni >= 0 and nj >= 0 and (ni, nj) not in seen:
                    if heights[ni][nj] >= heights[i][j]:
                        seen.add((ni, nj))
                        que.append((ni, nj))
                          
        return seen

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        pacific = deque()
        atlantic = deque()
        row, col = len(heights), len(heights[0])
        res = []

        for i in range(row):
            pacific.append((i, 0))
            atlantic.append((i, col - 1))

        for j in range(col):
            pacific.append((0, j))
            atlantic.append((row - 1, j))

        p_set = self.bfs(pacific, heights)
        a_set = self.bfs(atlantic, heights)

        for h in p_set:
            if h in a_set:
                res.append(h)

        return res
        