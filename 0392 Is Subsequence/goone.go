func isSubsequence(s string, t string) bool {
    j, i := 0, 0
    for i < len(s) && j < len(t){
        if s[i] == t[j]{
            i += 1;
        }
        j += 1
    }
    return i == len(s) 
}