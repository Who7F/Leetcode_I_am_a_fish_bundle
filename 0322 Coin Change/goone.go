func min (x int, y int) int {
    if x > y {
        return y
    }
    return x
}


func coinChange(coins []int, amount int) int {
    dp := make([]int, amount + 1)

    for i := 1; i < amount + 1; i++ {
        dp[i] = amount + 1

        for _, c := range coins {
            if i >= c {
                dp[i] = min(dp[i], dp[i - c] + 1)
            }
        }
    }

    if dp[amount] != amount + 1 {
        return dp[amount]
    } 

    return -1
}