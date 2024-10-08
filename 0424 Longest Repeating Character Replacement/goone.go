func max(x int, y int) int {
    if x > y{
        return x
    }
    return y
}


func characterReplacement(s string, k int) int {
    anc, low, maxCnt := 0, 0, 0
    cheekyMap := make(map[byte]int)
    for i := range s{
        cheekyMap[s[i]] ++
        maxCnt = max(maxCnt, cheekyMap[s[i]])

        if i - low + 1 - maxCnt > k{
            cheekyMap[s[low]] --
            low ++
        }
        anc = max(anc, i - low + 1)
    }
    return anc
}