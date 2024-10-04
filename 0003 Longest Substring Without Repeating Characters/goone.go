func lengthOfLongestSubstring(s string) int {
    anc, low := 0, 0
    cheekyMap := make(map[byte]int)
    for i := range s{
        if val, ok := cheekyMap[s[i]]; ok && val >= low{
            low = val + 1
        }
        cheekyMap[s[i]] = i
        if i - low + 1 > anc{
            anc = i - low + 1
        }
    }
    return anc
}