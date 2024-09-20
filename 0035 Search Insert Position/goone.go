func searchInsert(nums []int, target int) int {
    lit := 0
    big := len(nums) - 1
    anc := -1
    for lit <= big{
        anc = lit + (big - lit) / 2
        if target > nums[anc]{
            lit = anc + 1
        }else if target < nums[anc]{
            big = anc - 1
        }else{
            return anc
        }
    }
    return lit
}