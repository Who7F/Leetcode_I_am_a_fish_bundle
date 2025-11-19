class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = nums[1]

        for n in nums[2:]:
            prev2, prev1 = max(prev2, prev1), prev2 + n

        return max(prev2, prev1)