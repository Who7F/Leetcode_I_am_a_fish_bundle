func threeSum(nums []int) [][]int {
    slices.Sort(nums)
    res := [][]int{}
    n := len(nums)

    for i := 0; i < n - 2; i++ {
        if nums[i] > 0 {
            break
        }

        if i > 0 && nums[i] == nums[i - 1] {
            continue;
        }

        left := i + 1
        right := n - 1

        for left < right {

            if nums[i] + nums[left] + nums[right] == 0 {
                
                res = append(res, []int{nums[i], nums[left], nums[right]})

                left ++
                right --

                for left < right && nums[left] == nums[left - 1] {
                    left ++
                }

                for left < right && nums[right] == nums[right + 1] {
                    right --
                }
            } else if nums[i] + nums[left] + nums[right] < 0 {
                left ++
            } else {
                right --
            }
        }
    }
    return res
}