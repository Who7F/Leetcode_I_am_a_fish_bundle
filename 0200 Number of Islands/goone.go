func getIslands(i int, j int, grid [][]byte, deltas [][2]int) {
    stack := [][2]int{{i, j}}

    for len(stack) > 0{
        node := stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]

        i, j = node[0], node[1]

        if i >= 0 && i < len(grid) && j >= 0 && j < len(grid[i]) {
            if grid[i][j] == '1'{
                grid[i][j] = '0'

                for _, delta := range deltas {
                    stack = append(stack, [2]int{i + delta[0], j + delta[1]})
                }
            }
        }
    }
}

func numIslands(grid [][]byte) int {
    island := 0
    deltas := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} 

    for i := 0;  i < len(grid); i++ {
        for j := 0;  j < len(grid[i]); j++ {
            if grid[i][j] == '1'{
                island ++
                getIslands(i, j, grid, deltas) 
            }
        } 
    }
    return island
}