class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low, cnt, high = 0, 0, len(nums)  

        for h in range(high):
            if nums[h] == 0:
                cnt += 1  

            if cnt > k:  
                if nums[low] == 0:
                    cnt -= 1  
                low += 1  

        return high - low  