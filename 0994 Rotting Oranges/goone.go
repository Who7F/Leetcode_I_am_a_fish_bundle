type pair struct {
    r, c int
}

func orangesRotting(grid [][]int) int {
    row, col  := len(grid), len(grid[0])
    que := []pair{}
    deltas := []pair{{1, 0}, {-1, 0}, {0, 1},{0, -1}}
    fresh, time := 0, 0
    

    for i := 0; i < row; i++ {
        for j := 0; j < col; j++ {
            if grid[i][j] == 2 {
                que = append(que, pair{i, j})
            } else if grid[i][j] == 1 {
                fresh++
            }
        }
    }

    for len(que) > 0 {
        size := len(que)
        for q := 0; q < size; q++ {
            node := que[0]
            que =  que[1:]
            for _, delta := range deltas {
                nr, nc := delta.r + node.r, delta.c + node.c
                if nr >= 0 && nr < row && nc >= 0 && nc < col && grid[nr][nc] == 1 {
                    grid[nr][nc] = 2
                    que = append(que, pair{nr, nc})
                    fresh--
                }
            }
        }
        if len(que) > 0 {
            time++
        }        
    }

    if fresh == 0 {
        return time
    }

    return -1
}