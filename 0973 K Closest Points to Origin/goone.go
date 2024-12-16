type Pair struct{
    dest int
    nums []int    
}

type PairHeap []Pair
func (h PairHeap) Len() int {return len(h)}
func (h PairHeap) Less(i, j int) bool {return h[i].dest > h[j].dest}//< min heap. > max heap
func (h PairHeap) Swap(i, j int) {h[j], h[i] = h[i], h[j]}
func (h *PairHeap) Push(x interface{}) {*h = append(*h, x.(Pair))}
func (h *PairHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n - 1]
	*h = old[0 : n - 1 ]
	return x
}

func kClosest(points [][]int, k int) [][]int {
    h := &PairHeap{}

    for _, p := range points {
        destance := p[0]*p[0] + p[1]*p[1]
        heap.Push(h, Pair{dest: destance, nums: p})

        if h.Len() > k {
            heap.Pop(h)
        }
    }
    result := make([][]int, 0, k)
    for h.Len() > 0 {
        result = append(result, heap.Pop(h).(Pair).nums)
    }
    return result
}