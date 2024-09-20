# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lit = 0
        while lit < n:
            anc = lit + (n - lit)//2
            print(lit, n, anc)
            if isBadVersion(anc): 
                n = anc
            else:
                lit = anc + 1
            
        return n 
