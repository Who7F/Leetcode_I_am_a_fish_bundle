func max(x int, y int) int {
    if x > y {
        return x
    }
    return y
}

func canJump(nums []int) bool {
    maxJump := 0

    for i := 0; i < len(nums); i++ {
        if i > maxJump {
            return false
        } 
        maxJump = max(i + nums[i], maxJump)
    }
    return true
}