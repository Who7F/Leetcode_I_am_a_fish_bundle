class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)       
        stack = []

        for i, val in enumerate(nums):
            curr_val = val
            curr_left = i

            while stack and stack[-1][0] > val:
                top_val, top_left, _ = stack.pop()
                curr_val = max(curr_val, top_val)
                curr_left = top_left 
            
            stack.append((curr_val, curr_left, i))

        res = [0] * n

        for s in stack:
            for j in range(s[1], s[2] + 1):
                res[j] = s[0]


        return res
