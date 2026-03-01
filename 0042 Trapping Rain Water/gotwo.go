func trap(height []int) int {
    tail := 0
    res := 0
    sum := 0

    for i := 1; i < len(height); i++ {
        if height[i] >= height[tail] {
            res += (height[tail] * (i - tail - 1)) - sum
            sum = 0
            tail = i
        } else {
            sum += height[i]    
        }
    }

    sum = 0
    tail = 0
    fmt.Print(sum)

    for i := len(height) - 2; i >= 0; i--{
        if height[i] > height[tail] {
            res += (height[tail] * (tail - i - 1)) - sum
            sum = 0
            tail = i
        } else {
            sum += height[i]
        }
    }

    return res
}