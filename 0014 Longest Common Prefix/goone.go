func min(x int, y int) int {
    if x > y {
        return y
    }
    return x
}

func longestCommonPrefix(strs []string) string {
    anc := ""

    slices.Sort(strs)

    s := min(len(strs[0]), len(strs[len(strs) - 1]))

    for i := range s {
        if strs[0][i] != strs[len(strs) - 1][i] {
            return anc
        }
        anc += string(strs[0][i])
    }
    return anc
}