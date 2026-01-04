func maxNumberOfBalloons(text string) int {
    t := make(map[rune]int)
    b := "balloon"
    n := 0

    for _, c := range text {
        t[c] ++
    }

    for {
        for _, c := range b {
            t[c]-- 
            if t[c] <0 {
                return n
            }
        }
        n++
    }
    return -1 //error
}