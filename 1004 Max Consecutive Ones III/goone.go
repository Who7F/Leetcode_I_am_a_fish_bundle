func longestOnes(nums []int, k int) int {
    low, cnt, high := 0, 0, len(nums)

    for h := 0; h < high; h++{
        if nums[h] == 0{
            cnt ++
        }
        if cnt > k{
            if nums[low] == 0{
                cnt --
            }
            low ++
        }
    }
    return high - low
}