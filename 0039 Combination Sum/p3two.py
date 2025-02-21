# Slower, but doesn't look like garbage
class Solution:
    def getSum(self, candidates, target, index, sol, res):
        if sum(sol) == target:
            res.append(sol.copy())
            return
        

        if sum(sol) > target:
            return
        

        for i in range(index, len(candidates)):
            sol.append(candidates[i])
            self.getSum(candidates, target, i, sol, res)
            sol.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.getSum(candidates, target, 0, [], res, )
        return res
