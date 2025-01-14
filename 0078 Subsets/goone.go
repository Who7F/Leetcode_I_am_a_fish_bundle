// Recursive
// Finds base sebset
// Stateful Design

// Number of subsets is 2^n. 2 branches at each step.
type SubsetFinder struct{
    anc [][]int
    temp []int
}

func (finder *SubsetFinder) setSub(nums []int, i int){
    if i == len(nums){
        sub_set := make([]int, len(finder.temp))
        copy(sub_set, finder.temp)
        // Adds base case (current subset to results)
        finder.anc = append(finder.anc, sub_set)
    }else{
        // Left branch (exclude current element)
        finder.setSub(nums, i + 1)
        // Right branch (include current element)
        finder.temp = append(finder.temp, nums[i])
        finder.setSub(nums, i + 1)
        finder.temp = finder.temp[:len(finder.temp) - 1]
    }
}

func subsets(nums []int) [][]int {
    finder := SubsetFinder{}
    // Start the recursive process
    finder.setSub(nums, 0)
    return finder.anc
}