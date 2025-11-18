func climbStairs(n int) int {
    if n < 2 {
        return n
    }

    a, b := 0, 1

    for i := 0; i < n; i++ {
        a, b = b, a + b
    }

    return b
}