func isPerfectSquare(num int) bool {
    if 1 == num{
        return true
    }
    n := num
    lit := 0
    for lit < n{
        cnt := lit + (n - lit)/2
        if cnt*cnt == num{
            return true
        }else if cnt*cnt > num{
            n = cnt
        }else{
            lit = cnt + 1
        }
    }
    return false
}