func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func trap(height []int) int {
    left := 0
    right := len(height) - 1
    res := 0
    h := 0

    for left < right {
        if height[left] < height[right] {
            h = max(height[left], h)
            res += h - height[left]
            left++
        } else {
            h = max(height[right], h)
            res += h - height[right]
            right--
        }
    }
    return res
}