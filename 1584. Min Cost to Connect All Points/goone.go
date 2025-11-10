type Pair struct{
    cost, node int
}

type PairHeap []Pair
func (h PairHeap) Len() int {return len(h)}
func (h PairHeap) Less(i, j int) bool {return h[i].cost < h[j].cost}//< min heap. > max heap
func (h PairHeap) Swap(i, j int) {h[j], h[i] = h[i], h[j]}
func (h *PairHeap) Push(x interface{}) {*h = append(*h, x.(Pair))}
func (h *PairHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n - 1]
	*h = old[0 : n - 1 ]
	return x
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func minCostConnectPoints(points [][]int) int {
    n := len(points)
    if n == 0 {
        return 0
    }

    h := &PairHeap{}
    heap.Init(h)
    seen := make([]bool, n)
    
    cost := 0

    heap.Push(h, Pair{cost: 0, node: 0})

    for h.Len() > 0 {
        temp := heap.Pop(h).(Pair)
        if seen[temp.node] {
            continue
        }
        cost += temp.cost
        seen[temp.node] = true
        for nei := 0; nei < n; nei++ {
            if !seen[nei] {
                tempCost := (abs(points[temp.node][0] - points[nei][0])+abs(points[temp.node][1] - points[nei][1]))
                heap.Push(h, Pair{cost: tempCost, node: nei})
            }
        }     
    }
    return cost
}