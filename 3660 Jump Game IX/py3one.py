class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sfx = nums[:]
        
        for i in range(n - 2, -1, -1):
            sfx[i] = min(sfx[i], sfx[i + 1])

        res = []
        m = 0
        for i, x in enumerate(nums):
            m = max(m, x)
            if i == n - 1 or m <= sfx[i + 1]:
                res.extend([m] * (i + 1 - len(res)))
                m = 0


        return res
