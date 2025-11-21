class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = curr = nums[0]
        
        for n in nums[1:]:
            curr = max(n, curr + n)
            total = max(total, curr)
            
        return total