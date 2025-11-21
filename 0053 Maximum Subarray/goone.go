func max(x int, y int) int {
    if x > y {
        return x
    }
    return y
}

func maxSubArray(nums []int) int {
    total := nums[0]
    curr := nums[0]

    for _, n := range nums[1:] {
        curr = max(n, curr + n)
        total = max(curr, total)
    }

    return total
}