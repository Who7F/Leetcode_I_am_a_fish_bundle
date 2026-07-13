class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])

        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        for j in range(m):
            temp = [[-1] * (k + 1) for _ in range(n + 1)]

            for i in range(1, n + 1):
                score = grid[j][i - 1]
                cost = 0 if score == 0 else 1

                if (i, j) == (1, 0):
                    temp[1][0] = 0
                    continue

                for z in range(cost, k + 1):
                
                    best = max(dp[i][z - cost], temp[i - 1][z - cost]) 

                    if best != -1:
                        temp[i][z] = best + score

            dp = temp


        return max(dp[n]) 
        