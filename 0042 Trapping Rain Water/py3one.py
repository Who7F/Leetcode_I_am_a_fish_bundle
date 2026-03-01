class Solution:
    def trap(self, height: List[int]) -> int:
        cnt, lo, hi = 0, 0, len(height) - 1
        m = height[lo] if height[lo] < height[hi] else height[hi]
        
        while lo < hi:
            if height[lo] <= m:
                cnt += m - height[lo]
                lo += 1
            elif height[hi] <= m:
                cnt += m - height[hi]
                hi -= 1
            else:   
                m = height[lo] if height[lo] < height[hi] else height[hi]

        return cnt