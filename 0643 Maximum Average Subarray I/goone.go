func findMaxAverage(nums []int, k int) float64 {
    total, top := 0, len(nums)

    for i := 0; i < k; i++{
        total += nums[i]
    }

    cnt := total

    for i := k; i < top; i++{
        total += nums[i]
        total -= nums[i - k]
        if total > cnt{
            cnt = total
        }
    }
    return float64(cnt) / float64(k)
}