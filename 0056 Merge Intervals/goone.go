func merge(intervals [][]int) [][]int {
    sort.Slice(intervals, func(x, y int) bool {
        return intervals[x][0] < intervals[y][0]
    })
    
    anc := [][]int{}
    n := 0

    anc = append(anc, intervals[0])

    for _, i := range intervals {
        if anc[n][1] >= i[0] {
            if anc[n][1] < i[1] {
                anc[n][1] = i[1]
            }
        } else {
            anc = append(anc, i)
            n++
        }
    }

    return anc    
}