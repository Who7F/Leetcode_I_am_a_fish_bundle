class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        anc = [0] * len(temperatures)
        stack = []
        for e, i in enumerate(temperatures):
            while stack != [] and i > stack[-1][1]:
                p = stack.pop()
                anc[p[0]] = e- p[0]
            stack.append((e, i))
   
        return anc      