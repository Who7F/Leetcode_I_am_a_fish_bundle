type IntHeap []int
func (h IntHeap) Len() int {return len(h)}
func (h IntHeap) Less(i, j int) bool {return h[i] < h[j]}//< min heap. > max heap
func (h IntHeap) Swap(i, j int) {h[j], h[i] = h[i], h[j]}
func (h *IntHeap) Push(x interface{}) {*h = append(*h, x.(int))}
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n - 1]
	*h = old[0 : n - 1 ]
	return x
}

func findKthLargest(nums []int, k int) int {
    h := &IntHeap{}
    heap.Init(h)

    for _, val := range(nums[:k]){
		heap.Push(h, val)
	}

    for _, val := range(nums[k:]){
        if val > (*h)[0] {
            heap.Push(h, val)
            heap.Pop(h)
        }
	}
    return (*h)[0]
}