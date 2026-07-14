class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        ttl = 0
        tmp  = 0

        for i, val in enumerate(nums):
            ttl += val
            tmp += i * val

        res = tmp
        
        for i in range(1, n):
            tmp = tmp + ttl - (n * nums[n - i])
            res = max(res, tmp)

        return res
