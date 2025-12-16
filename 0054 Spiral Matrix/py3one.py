class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top = 0
        btm = len(matrix) -1 
        lft = 0
        rgh = len(matrix[0]) -1
        anc = []
        while True:
            for i in range(lft, rgh +1, +1):
                anc.append(matrix[top][i])
            if len(anc) == len(matrix) * len(matrix[0]):
                break
            top += 1
            for i in range(top, btm +1, +1):
                anc.append(matrix[i][rgh])
            if len(anc) == len(matrix) * len(matrix[0]):
                break
            rgh -= 1
            for i in range(rgh, lft -1, -1):
                anc.append(matrix[btm][i])
            if len(anc) == len(matrix) * len(matrix[0]):
                break
            btm -= 1
            for i in range(btm, top -1, -1):
                anc.append(matrix[i][lft])
            if len(anc) == len(matrix) * len(matrix[0]):
                break
            lft += 1


        return anc
        