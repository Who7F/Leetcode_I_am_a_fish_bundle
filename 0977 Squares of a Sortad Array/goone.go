func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func sortedSquares(nums []int) []int {
    res := make([]int, len(nums))
    left := 0
    right := len(nums) - 1

    for i := len(nums); i > 0; i-- {
        if abs(nums[left]) > abs(nums[right]) {
            res[i -1] = nums[left] * nums[left]
            left++
        } else {
            res[i -1] = nums[right] * nums[right] 
            right--
        }
    }

    return res
}