func isValidSudoku(board [][]byte) bool {
    seen := make(map[int]struct{})

    for i := 0; i < 9; i++ {
        for j := 0; j < 9; j++ {
            if board[i][j] != '.' {
                b := int(board[i][j])
                key := []int{
                    10 * i + b,
                    10 * j + b + 100,
                    10 * (j/3 + (i/3 * 3)) + b + 200,
                }
                for _, k := range key {
                    if _, ok := seen[k]; ok {
                        return false
                    }
                    seen[k] = struct{}{}
                }                
            }
        }
    }
    return true
}