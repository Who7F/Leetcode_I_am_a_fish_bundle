func romanToInt(s string) int {
    numeralMap := map[string]int{
        "I": 1, 
        "V": 5, 
        "X": 10, 
        "L": 50, 
        "C": 100, 
        "D": 500, 
        "M": 1000,
    }
    length := len(s)
    anc := 0
    fmt.Printf(string(s[0]))
    for i := 0; i < length - 1; i++{
        if numeralMap[string(s[i])] < numeralMap[string(s[i+1])]{
            anc -= numeralMap[string(s[i])]
        }else{
            anc += numeralMap[string(s[i])]
        }
    }
    anc += numeralMap[string(s[length-1])]
    return anc
}