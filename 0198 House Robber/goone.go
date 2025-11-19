func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

func rob(nums []int) int {
    if len(nums) == 1 {
        return nums[0]
    }

    prev2, prev1 := nums[0], nums[1]

    for _, n := range nums[2:] {
        prev2, prev1 = max(prev2, prev1), prev2 + n
        
    }

    return max(prev2, prev1)
}