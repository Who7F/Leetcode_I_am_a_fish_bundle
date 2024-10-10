func checkInclusion(s1 string, s2 string) bool {
    if len(s1) > len(s2){
        return false
    }

    cntS1, cntS2 := [26]int{}, [26]int{}

    for i := 0; i < len(s1); i++{
        cntS1[s1[i] - 97]++
        cntS2[s2[i] - 97]++
    }

    if cntS1 == cntS2{
        return true
    }

    for i := len(s1); i < len(s2); i ++{
        cntS2[s2[i] - 97]++
        cntS2[s2[i - len(s1)] - 97]--
        if cntS1 == cntS2{
            return true
        } 
    }
    return false
}