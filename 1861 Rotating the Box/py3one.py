class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        n = len(boxGrid)
        m = len(boxGrid[0])

        res = [["."]*n for _ in range(m)]

        for i in range(n):
            pointer = m - 1
            
            for j in range(m - 1, -1, -1):
                val = boxGrid[i][j]
                if val == '*':
                   res[j][n - 1 - i] = '*'
                   pointer = j - 1
                elif val == '#':
                    res[pointer][n - 1 - i] = '#'
                    pointer -= 1
        
        return res
