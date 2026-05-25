class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        R = len(robot)
        F = len(factory)

        #I dislike decorators
        @lru_cache(None)
        def dfs(i, j):

            if i == R:
                return 0

            if j == F:
                return float('inf')

            pos, limit = factory[j]

            ans = dfs(i, j + 1)

            dist = 0
            for k in range(1, min(limit, R - i) + 1):
                dist += abs(robot[i + k - 1] - pos)
                ans = min(ans, dist + dfs(i + k, j + 1))

            return ans

        return dfs(0, 0)
