class Solution:
    def findWord(self, board, word, i, j, index):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False

        if board[i][j] != word[index]:
            return False
        
        index += 1
        
        if index == len(word):
            return True

        temp = board[i][j]
        board[i][j] = "-"

        for m, n in [(0, 1),(1, 0),(0, -1),(-1, 0)]:
            if self.findWord(board, word, i + m, j + n, index):
                return True

        board[i][j] = temp

        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.findWord(board, word, i, j, 0):
                    return True
        return False
