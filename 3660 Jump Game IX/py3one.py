class Solution:
    def maxValue(self, A: List[int]) -> List[int]:
        n = len(A)
        pst = A[:]
        
        for i in range(n - 2, -1, -1):
            pst[i] = min(pst[i], pst[i + 1])

        res = []
        m = 0
        for i, x in enumerate(A):
            m = max(m, x)
            if i == n - 1 or m <= pst[i + 1]:
                res.extend([m] * (i + 1 - len(res)))
                m = 0

        return res
