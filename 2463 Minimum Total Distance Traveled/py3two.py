class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        n = len(robot)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
 
        for pos, limit in factory:
            ndp = dp[:] 

            for i, _ in enumerate(robot):
                dist = 0

                for k in range(1, min(limit, n - i) + 1):
                    dist += abs(robot[i + k - 1] - pos)

                    ndp[i + k] = min(ndp[i + k], dp[i] + dist)

            dp = ndp

        return dp[n]
