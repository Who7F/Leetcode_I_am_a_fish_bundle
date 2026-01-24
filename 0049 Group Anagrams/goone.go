func groupAnagrams(strs []string) [][]string {
    seen := make(map[string][]string)

    for _, s := range strs {
        chars := []rune(s)
        sort.Slice(chars, func(i, j int)bool {
            return chars[i] > chars[j]
        })
        key := string(chars)
        seen[key] = append(seen[key], s)
    }

    res := make([][]string, 0, len(seen))

    for _, s := range seen {
        res = append(res, s)
    }

    return res
}