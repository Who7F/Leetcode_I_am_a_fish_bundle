type IntHeap []int
func (h IntHeap) Len() int {return len(h)}
func (h IntHeap) Less(i, j int) bool {return h[i] > h[j]}//< min heap. > max heap
func (h IntHeap) Swap(i, j int) {h[j], h[i] = h[i], h[j]}
func (h *IntHeap) Push(x interface{}) {*h = append(*h, x.(int))}
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n - 1]
	*h = old[0 : n - 1 ]
	return x
}

func lastStoneWeight(stones []int) int {
    h := &IntHeap{}
    heap.Init(h)
	for _, val := range(stones){
		heap.Push(h, val)
	}
	for h.Len() > 1{
		x := heap.Pop(h).(int)
		y := heap.Pop(h).(int)

		
		if x != y {
			heap.Push(h, (x - y))
		}
	}

	if h.Len() == 0{
		return 0
	} else{
		return heap.Pop(h).(int)
	}
}