func getPairs(res *[]string, sol string, left int, right int) {
    if left + right == 0 {
        *res = append(*res, sol)
        return
    }

    if left > 0 {
        getPairs(res, sol + "(", left - 1, right + 1)
    }

    if right > 0 {
        getPairs(res, sol + ")", left, right - 1)
    }
}

func generateParenthesis(n int) []string {
    res := []string{}
    getPairs(&res, "", n, 0)
    return res
}