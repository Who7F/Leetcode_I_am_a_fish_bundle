func canConstruct(ransomNote string, magazine string) bool {
    seen := make(map[rune]int)

    for _, m := range magazine {
        seen[m]++
    }

    for _, r := range ransomNote {
        seen[r]--
        if seen[r] < 0 {
            return false
        }
    }

    return true
}