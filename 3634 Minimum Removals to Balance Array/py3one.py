class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        res = len(nums) 

        for r in range(len(nums)):
            while nums[l] * k < nums[r] and l < r:
                l += 1

            res = min(res, len(nums) - r + l - 1)
            

        return res