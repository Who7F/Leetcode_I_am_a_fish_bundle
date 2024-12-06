class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l//2):
            for j in range(i, l-i-1, 1):
                
                bucket = matrix[i][j]
                matrix[i][j] = matrix[l-j-1][i]
                matrix[l-j-1][i] = matrix[l-i-1][l-j-1]
                matrix[l-i-1][l-j-1] = matrix[j][l-i-1]
                matrix[j][l-i-1] = bucket
