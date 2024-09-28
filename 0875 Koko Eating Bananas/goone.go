import (
    "math"
)

func eatsBananas(piles []int, h int, bite int) bool {
    n := 0
    for _, p := range piles{
        n += int(math.Ceil(float64(p) / float64(bite)))
    }
    return n <= h
}

func max(piles []int) int{
    maxVal := piles[0]
    for _, p := range piles{
        if p > maxVal {
            maxVal = p
        }
    }
    return maxVal
}

func minEatingSpeed(piles []int, h int) int {
    lit, big := 1, max(piles)
    for lit < big{
        bite := lit + (big - lit) / 2
        if eatsBananas(piles, h, bite){
            big = bite
        }else{
            lit = bite + 1
        }
    }
    return lit
}