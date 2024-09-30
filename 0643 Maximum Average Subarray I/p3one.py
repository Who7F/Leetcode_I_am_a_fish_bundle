class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        top = len(nums)
        total = 0
        for i in range(k):
            total += nums[i]

        anc = total
        
        for i in range(k, top):
            total += nums[i]
            total -= nums[i - k]
            anc = max(anc, total)

        return(anc / k)