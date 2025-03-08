func findWord(board [][]byte, word string, i int, j int, index int) bool {
    if i < 0 || i >= len(board) || j < 0 || j >= len(board[0]) {
        return false
    }

    if board[i][j] != word[index] {
        return false
    }

    index++

    if index == len(word) {
        return true
    }

    temp := board[i][j]
    board[i][j] = '-'

    for _, delta := range [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} {
        dx, dy := delta[0], delta[1]
        if findWord(board, word, i + dx, j + dy, index) {
            return true
        }
    }
    
    board[i][j] = temp
    return false
}

func exist(board [][]byte, word string) bool {
    for i := 0; i < len(board); i++ {
        for j := 0; j < len(board[0]); j++ {
            if findWord(board, word, i, j, 0) {
                return true
            }
        }
    }
    return false
}



