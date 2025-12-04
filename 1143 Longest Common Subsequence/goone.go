func max(x int, y int) int {
    if x > y {
        return x
    }
    return y
}

func longestCommonSubsequence(text1 string, text2 string) int {
    dp := make([]int, len(text2) + 1)

    for i := 0; i < len(text1); i++ {
        prev := 0
        
        for j := 0; j < len(text2); j++ {
            temp := dp[j + 1]

            if text1[i] == text2[j] {
                dp[j + 1] = prev + 1
            } else {
                dp[j + 1] = max(dp[j + 1], dp[j])
            }
            prev = temp
        }    
    }
    return dp[len(dp) - 1]
}