func numJewelsInStones(jewels string, stones string) int {
    cnt := 0

    for _, j := range jewels {
        for _, s := range stones {
            if j == s {
                cnt++
            }
        }
    }

    return cnt
}
