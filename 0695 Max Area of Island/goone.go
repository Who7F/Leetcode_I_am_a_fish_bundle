func getIslands(i int, j int, grid [][]int, deltas [][2]int) int {
    if i < 0 || i >= len(grid) || j < 0 || j >= len(grid[0]) || grid[i][j] == 0{
        return 0
    }
            
    grid[i][j] = 0
    res := 1

    for _, delta := range deltas {
        res += getIslands(i + delta[0], j + delta[1], grid, deltas) 
    }
    return res
}

func max(x int, y int) int {
    if x > y{
        return x
    }
    return y
}

func maxAreaOfIsland(grid [][]int) int {
    res := 0
    deltas := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} 

    for i := 0;  i < len(grid); i++ {
        for j := 0;  j < len(grid[i]); j++ {
            if grid[i][j] == 1{
                res = max(res, getIslands(i, j, grid, deltas))
            }
        } 
    }
    return res
}