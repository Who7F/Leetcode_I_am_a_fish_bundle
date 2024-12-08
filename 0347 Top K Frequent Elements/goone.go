type Pair struct{
    freq int
    num int
}

type PairHeap []Pair
func (h PairHeap) Len() int {return len(h)}
func (h PairHeap) Less(i, j int) bool {return h[i].freq < h[j].freq}//< min heap. > max heap
func (h PairHeap) Swap(i, j int) {h[j], h[i] = h[i], h[j]}
func (h *PairHeap) Push(x interface{}) {*h = append(*h, x.(Pair))}
func (h *PairHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n - 1]
	*h = old[0 : n - 1 ]
	return x
}

func topKFrequent(nums []int, k int) []int {
    freqMap := make(map[int]int)
    for _, num := range nums {
        freqMap[num]++
    }

    h := &PairHeap{}
    heap.Init(h)

    for num, freq := range freqMap {
        heap.Push(h, Pair{freq, num})
        if h.Len() > k {
            heap.Pop(h)
        }
    }

    result := make([]int, 0, k)
    for h.Len() > 0 {
        result = append(result, heap.Pop(h).(Pair).num)
    }
    
    return result
}