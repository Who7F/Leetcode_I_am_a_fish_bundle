func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)

    for i, n := range nums {
        if idx, ok := seen[target - n]; ok {
            return []int{idx ,i}
        } else {
            seen[n] = i
        }
    }
    return nil
}