class Solution:
    def binarySearch(self, dp, n) -> int:
        left, right = 0, len(dp) - 1
       
        while left <= right:
            mid = (right - left)//2 + left
   
            if dp[mid] < n:
                left = mid + 1

            else:
                right = mid - 1

        dp[left] = n

            
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [nums[0]]

        for n in nums[1:]:

            if n > dp[-1]:
                dp.append(n)
            else:
                self.binarySearch(dp, n)
                
        return len(dp)