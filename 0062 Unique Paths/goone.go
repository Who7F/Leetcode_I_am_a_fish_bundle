func uniquePaths(m int, n int) int {
    grid := make([]int ,n)

    grid[0] = 1

    for i := 0; i < m; i++ {
        for j := 1; j < n; j++ {
            grid[j] += grid[j - 1]
        }
    }

    return grid[n - 1]
}