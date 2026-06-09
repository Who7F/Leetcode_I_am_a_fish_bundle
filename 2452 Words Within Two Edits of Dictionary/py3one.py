class Solution:
    def getDustance(self, q, d):
        cnt = 0
        for i, _ in enumerate(q):
            if q[i] != d[i]:
                cnt += 1
            
            if cnt > 2:
                return False
            
        return True

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for q in queries:
            for d in dictionary:
                if self.getDustance(q, d):
                    res.append(q)
                    break
        
        return res