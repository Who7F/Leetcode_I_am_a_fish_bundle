func maxNumberOfBalloons(text string) int {
    word := "balloon"

    freq := make(map[rune]int)
    
    for _, t := range text {
        freq[t] ++
    }

    need := make(map[rune]int)
    
    for _, w := range word {
        need[w] ++
    }

    ans := math.MaxInt

    for c, cnt := range need {
        ans = min(ans, freq[c]/cnt)
    }

    return ans
}