func setDum(res *[][]int, sol []int, candidates []int, target int, l int, index int) {
    if l == target{
        tmp := make([]int, len(sol))
        copy(tmp, sol)
        *res = append(*res, tmp)
        return
    }

    if l > target {
        return
    }

    for i := index; i < len(candidates); i++ {
        sol = append(sol, candidates[i])
        setDum(res, sol, candidates, target, l + candidates[i], i)
        sol = (sol)[:len(sol) - 1]
    }
    
}

func combinationSum(candidates []int, target int) [][]int {
    res := [][]int{}
    sol := []int{}
    setDum(&res, sol, candidates, target, 0 , 0)
    return res
}