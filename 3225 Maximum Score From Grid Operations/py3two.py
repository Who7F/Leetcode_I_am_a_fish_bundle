class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n == 1: return 0

        HEIGHT = 0
        STATE = 1

        dp = [[0, 0] for _ in range(n + 1)]
        for j in range(1, m):
            temp = [[0, 0] for _ in range(n + 1)]
            
            for i in range(n + 1):
                prev = 0
                curr = sum(grid[k][j] for k in range(i))
                
                for k in range(n + 1):
                    if k > 0 and k <= i:
                        curr -= grid[k - 1][j]

                    if j > 0 and  k > i:
                        prev += grid[k - 1][j - 1]

                    temp[k][HEIGHT] = max(
                        temp[k][HEIGHT],
                        prev + dp[i][HEIGHT],
                        dp[i][STATE]
                    )

                    temp[k][STATE] = max(
                        temp[k][STATE],
                        curr + dp[i][STATE],
                        curr + prev + dp[i][HEIGHT]
                    )
                    
            dp = temp
        
        return max(row[STATE] for row in dp)
