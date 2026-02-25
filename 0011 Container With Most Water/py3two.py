class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
                
        while left < right:
            width = right - left
            temp = min(height[left], height[right]) * width 
            res = max(res, temp)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1  
            

        return res