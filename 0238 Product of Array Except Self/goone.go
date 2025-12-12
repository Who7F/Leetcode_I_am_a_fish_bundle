func productExceptSelf(nums []int) []int {
    l := len(nums)
    anc := make([]int, l)

    total := 1

    for i := 0; i < l - 1; i++ {
        total *= nums[i]
        anc[i + 1] = 1 * total
    }

    total = 1
    anc[0] = 1

    for i := l - 1; i > 0; i-- {
        total *= nums[i]
        anc[i - 1] *= total
    }
    
    return anc
}