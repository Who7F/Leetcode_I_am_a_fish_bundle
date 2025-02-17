// Pointer-based design,
// recursive
// Finds base sebset
func findNumber(n int, k int, res *[][]int, sol *[]int){
    if len(*sol) == k{
        // Adds base case (current subset to results)
        tmp := make([]int, len(*sol))
        copy(tmp, *sol)
        *res = append(*res, tmp)
    }else{
        // Left branch (exclude current element)
        if(n > k - len(*sol)){
            findNumber(n - 1, k, res, sol)
        }
        // Right branch (include current element)
        *sol = append(*sol, n)
        findNumber(n - 1, k, res, sol)
        *sol = (*sol)[:len(*sol) - 1]
    }
}

func combine(n int, k int) [][]int {
    res := [][]int{}
    sol := []int{}
    findNumber(n, k, &res, &sol)
    return res
}