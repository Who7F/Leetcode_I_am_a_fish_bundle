func mergeAlternately(word1 string, word2 string) string {
    anc := ""
    min_len := len(word1)
    if len(word1) > len(word2){
        min_len = len(word2)
    }
    for i := range min_len{
        anc += string(word1[i]) + string(word2[i]) 
    }
    anc += word1[min_len:] + word2[min_len:]

    return anc
}