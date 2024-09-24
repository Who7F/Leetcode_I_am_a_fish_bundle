func maxProfit(prices []int) int {
    l, h, anc := prices[0], 0, 0
    for _, i := range prices{
        if i > h{
            h = i
            if h - l > anc{
                anc = h - l
            }
        }
        if i < l{
            l = i
            h = i
        }    
    }
    return anc
}