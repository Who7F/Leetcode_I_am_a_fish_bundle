func isPalindrome(s string) bool {
    runes := []rune(s)
    l, r := 0, len(runes)-1

    for l < r {
        if !unicode.IsLetter(runes[l]) && !unicode.IsDigit(runes[l]) {
            l++
        } else if !unicode.IsLetter(runes[r]) && !unicode.IsDigit(runes[r]) {
            r--
        } else if unicode.ToLower(runes[l]) != unicode.ToLower(runes[r]) {
            return false
        } else {
            l++
            r--
        }
    }
    return true
}