type pair struct {
    r, c int
}

func bfs(heights [][]int, que []pair, visited [][]bool) {
    delta := []pair{{1, 0}, {-1, 0}, {0, 1},{0, -1}}
    row, col := len(heights), len(heights[0])

    for len(que) > 0 {
        node := que[0]
        que = que[1:]
        for _, d := range delta {
            nr, nc := node.r + d.r, node.c + d.c            
            if nr >= 0 && nr < row && nc >= 0 && nc < col && !visited[nr][nc] && heights[nr][nc] >= heights[node.r][node.c] {
                visited[nr][nc] = true
                que = append(que, pair{nr, nc})
            }
                
        }
    } 
}

func pacificAtlantic(heights [][]int) [][]int {
    if len(heights) == 0 || len(heights[0]) == 0 {
        return [][]int{}
    }

    row, col := len(heights), len(heights[0])
    
    pacific := make([][]bool, row)
    atlantic := make([][]bool, row)

    for i := 0; i < row; i++ {
        pacific[i] = make([]bool, col)
        atlantic[i] = make([]bool, col)
    }

    pacQue := make([]pair, 0)
    atlQue := make([]pair, 0)

    for i := 0; i < row; i++ {
        pacQue = append(pacQue, pair{i, 0})
        atlQue = append(atlQue, pair{i, col - 1})
        pacific[i][0] = true
        atlantic[i][col - 1] = true
    }

    for j := 0; j < col; j++ {
        pacQue = append(pacQue, pair{0, j})
        atlQue = append(atlQue, pair{row - 1, j})
        pacific[0][j] = true
        atlantic[row - 1][j] = true
    }
    
    bfs(heights, pacQue, pacific)
    bfs(heights, atlQue, atlantic)

    res := [][]int{}

    for i := 0; i < row; i++{
        for j := 0; j < col; j++{
            if pacific[i][j] && atlantic[i][j]{
                res = append(res, []int{i, j})
            }
        }
    }

    return res
}