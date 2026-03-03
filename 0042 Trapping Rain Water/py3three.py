class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []

        for right in range(len(height)):

            while stack and height[stack[-1]] < height[right]:
                m = stack.pop()
                if not stack:
                    break

                left = stack[-1]

                h = min(height[right], height[left])
                res += (h - height[m]) * (right - left - 1)

            stack.append(right)


        return res