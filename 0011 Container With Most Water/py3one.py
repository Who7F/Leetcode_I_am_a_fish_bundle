class Solution:
    def maxArea(self, height: List[int]) -> int:
        cnt = 0
        lo = 0
        hi = len(height) - 1
        while lo < hi:

            if height[lo] > height[hi]:    
                if height[hi] * (hi-lo) > cnt:
                    cnt = height[hi] * (hi-lo)
                hi -= 1

            elif height[lo] < height[hi]:
                if height[lo] * (hi-lo) > cnt:
                    cnt = height[lo] * (hi-lo)
                lo += 1

            else:
                if height[hi] * (hi-lo) > cnt:
                    cnt = height[hi] * (hi-lo)
                hi -= 1
                lo += 1


        return cnt