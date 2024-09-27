func search(nums []int, target int) int {
    lit, big := 0, len(nums) - 1
    for lit <= big{
        mid := lit + (big - lit) / 2
        if nums[mid] == target{
            return mid
        }
        if nums[lit] <= nums[mid]{
            if nums[lit] <= target && target < nums[mid]{
                big = mid - 1
            }else{
                lit = mid + 1
            }
        }else{
            if nums[mid] < target && target <= nums[big]{
                lit = mid + 1
            }else{
                big = mid - 1
            }
        }
    }
    return -1