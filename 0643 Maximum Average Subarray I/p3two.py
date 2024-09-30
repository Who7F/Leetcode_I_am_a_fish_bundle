class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total, top = 0, len(nums)

        total = sum(nums[:k])

        anc = total
        
        for i in range(k, top):
            total += nums[i] - nums[i - k]
            anc = max(anc, total)

        return(anc / k)
