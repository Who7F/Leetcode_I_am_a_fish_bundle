func max (x, y int, flag bool) int {
    if (x > y && flag) || (x < y && !flag) {
        return x
    } 
    return y
}

func maxArea(height []int) int {
    left := 0
    right := len(height) - 1
    res := 0

    for left < right {
        width := right - left
        temp := max(height[left], height[right], false) * width
        res = max(res, temp, true)

        if height[left] < height[right] {
            left ++
        } else {
            right --
        }
    }
    return res
}