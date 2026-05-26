class Solution:

    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res =  float("inf")
        n = len(words)
            
        for i, w in enumerate(words):
            if w == target:
                d = abs(startIndex - i)
                res = min(res, min(d, n- d))

        return -1 if res == float("inf") else res
