func findMin(nums []int) int {
    lit, big := 0, len(nums) - 1
    for lit < big{
        mid := lit + (big - lit) / 2
        if nums[mid] > nums[big]{
            lit = mid + 1
        }else{
            big = mid
        }
    }
    return nums[lit]
}