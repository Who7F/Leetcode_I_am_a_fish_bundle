func findClosestNumber(nums []int) int {
    anc := nums[0]

    abs := func (x int) int {
        if x < 0 {
            x = x * -1
        }
        return x
    }

    for _, i := range nums{
        if abs(i) < abs(anc){
            anc = i
        }
        if abs(i) == abs(anc){
            anc = max(anc, i)
        }
    }
    
    return anc
}