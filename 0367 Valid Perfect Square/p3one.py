class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if 1 == num:
            return True
        n = num
        lit = 0
        while lit < n:
            cnt = lit + (n - lit)//2
            if cnt*cnt == num:
                return True
            elif cnt*cnt > num:
                n =cnt
            else:
                lit = cnt + 1
        return False
