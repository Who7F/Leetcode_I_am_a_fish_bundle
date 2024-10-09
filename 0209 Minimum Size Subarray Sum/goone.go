import (
    "math"
)

func min(x int, y int) int{
    if x < y{
        return x
    }
    return y
}

func minSubArrayLen(target int, nums []int) int {
    low, ttl, anc := 0, 0, math.MaxInt

    for i := range nums{
        ttl += nums[i]

        for ttl >= target{
            anc = min(anc, i - low + 1)
            ttl -= nums[low]
            low ++
        }
    }
    if anc == math.MaxInt {
        return 0
    }
    return anc
}