class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        h = 0

        while left < right:
            if height[left] < height[right]:
                h = max(h, height[left])
                res += h - height[left]
                left += 1

            else:
                h = max(h, height[right])
                res += h - height[right]
                right -= 1

        return res