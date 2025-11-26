func binarySearch(dp []int, n int) int {
    left, right := 0, len(dp) - 1

    for left <= right {
        mid := (right - left) / 2  + left

        if dp[mid] < n {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return left
}

func lengthOfLIS(nums []int) int {
    dp := []int{nums[0]}

    for _, n := range nums[1:] {
        if n > dp[len(dp) - 1] {
            dp = append(dp, n)
        } else {
            idx := binarySearch(dp, n)
            dp[idx] = n
        }
    }
    return len(dp)    
}