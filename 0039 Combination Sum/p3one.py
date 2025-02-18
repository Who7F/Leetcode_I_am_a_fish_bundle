# too ugly to keep

class Solution:
    def getSum(self, candidates, target, sol, res, n):
        if n == target:
            res.append(sol.copy())
        else:
            if n > target or len(candidates) == 0:
                return

            self.getSum(candidates[1:], target, sol, res, n)
    
            sol.append(candidates[0])
            self.getSum(candidates, target, sol, res, n + candidates[0])
            sol.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        res = []
        self.getSum(candidates, target, sol, res, 0)
        return res
