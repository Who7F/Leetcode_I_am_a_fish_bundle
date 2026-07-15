class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = {'2', '5', '6', '9'}
        bad = {'3', '4', '7'}

        res = 0

        for i in range(1, n + 1):
            change = False

            for val in str(i):
                if val in bad:
                    break
                
                if val in good:
                    change = True

            else:
                if change:
                    res += 1
        
        return res
