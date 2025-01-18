// recursive
// Gets all the possible permutations

func findPermuta(nums []int, res *[][]int, index int){
    if index == len(nums){
        sub_set := make([]int, len(nums))
        copy(sub_set, nums)
        // Adds base case (current subset to results)
        *res = append(*res, sub_set)
    }else{
        for i := index; i < len(nums); i++{
            nums[index], nums[i] = nums[i], nums[index]
            findPermuta(nums, res, index + 1)
            nums[index], nums[i] = nums[i], nums[index]
        }

    }   
}

func permute(nums []int) [][]int {
    res := [][]int{}
    // Start the recursive process
    findPermuta(nums, &res, 0)
    return res
}