class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, tmp in enumerate(temperatures):
            while stack and tmp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = idx - prev
            stack.append(idx)
   
        return res     