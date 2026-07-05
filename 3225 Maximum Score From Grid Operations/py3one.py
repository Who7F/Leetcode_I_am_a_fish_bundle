class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n == 1: return 0

        dp_pri = [0] * (n + 1)
        dp_sec = [0] * (n + 1)
        for j in range(1, m):
            temp_pri = [0] * (n + 1)
            temp_sec = [0] * (n + 1)
            for i in range(n + 1):
                prev = 0
                curr = sum(grid[k][j] for k in range(i))
                
                for k in range(n + 1):
                    if k > 0 and k <= i:
                        curr -= grid[k - 1][j]

                    if j > 0 and  k > i:
                        prev += grid[k - 1][j - 1]

                    temp_pri[k] = max(temp_pri[k], prev + dp_pri[i], dp_sec[i])
                    temp_sec[k] = max(temp_sec[k], curr + dp_sec[i], curr + prev + dp_pri[i])

            dp_pri, dp_sec = temp_pri, temp_sec

        return max(dp_sec)
