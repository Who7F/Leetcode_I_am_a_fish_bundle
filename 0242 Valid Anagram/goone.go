func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    seen := make(map[rune]int)

    for _, i := range s{
        seen[i]++
    }

    for _, i := range t{
        if seen[i] == 0 {
            return false
        }
        seen[i]--
    }

    return true
}