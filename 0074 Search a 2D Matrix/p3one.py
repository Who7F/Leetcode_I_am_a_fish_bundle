class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])  
        lit, big = 0, m * n - 1
        while lit <= big:
            mid = lit + (big -lit) // 2
            row, col = divmod(mid, n)
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                lit = mid + 1
            else:
                big = mid - 1

        return False
