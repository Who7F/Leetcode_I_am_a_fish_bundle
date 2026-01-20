class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cnt = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    
                    cnt.append(10 * i + int(board[i][j]))
                    cnt.append(10 * j + int(board[i][j]) + 100)
                    cnt.append(10 *(j//3 + (i//3 * 3)) + int(board[i][j]) + 200)

        
    
        return len(set(cnt)) == len(cnt)