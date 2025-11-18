func min(x int, y int) int {
    if x > y {
        return y
    }
    return x
}

func minCostClimbingStairs(cost []int) int {
    prev2, prev1 := cost[0], cost[1]

    for _, c := range cost[2:] {
        prev2, prev1 = prev1, c + min(prev2, prev1)
    }
    return min(prev2, prev1)
}