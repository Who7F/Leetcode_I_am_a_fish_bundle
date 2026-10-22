class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        m = max(lights)
        res = 0
        for a in arrivalTime:
            curr = a % period

            if curr >= m:
                res = max(res, period - curr)

        return res