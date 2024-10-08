class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        anc = float('inf')
        low, ttl = 0, 0

        for i in range(len(nums)):
            ttl += nums[i]
            while ttl >= target:
                anc = min(anc, i - low + 1)
                ttl -= nums[low]
                low += 1

        return anc if anc < float('inf') else 0
