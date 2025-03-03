class Solution:
    def getPairs(self, res, sol, left, right):
        if left + right == 0:
            res.append(sol)
            return

        if left > 0:
            self.getPairs(res, sol + '(', left - 1, right + 1)

        if right > 0:
            self.getPairs(res, sol + ')', left, right - 1)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.getPairs(res, "", n, 0)
        return res
