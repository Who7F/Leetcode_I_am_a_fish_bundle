func twoSum(numbers []int, target int) []int {
    left := 0
    right := len(numbers) - 1

    for left < right{
        temp := numbers[left] + numbers[right]
        if temp < target {
            left ++
        } else if temp > target {
            right --
        } else {
            return []int{left +1, right + 1}
        }
    }
    return []int{-1, -1}
}