func spiralOrder(matrix [][]int) []int {
    x, y, dx, dy := 0, 0, 1, 0
    res := []int{}
    row, col := len(matrix), len(matrix[0])

    for i := 0; i < row * col; i++ {
        res = append(res, matrix[y][x])
        matrix[y][x] = -101

        if !(0 <= x + dx && x + dx < col && 0 <= y + dy && y + dy < row) || matrix[y+dy][x+dx] == -101 {
            dx, dy = -dy, dx
        }

        x += dx
        y += dy
    }

    return res    
}