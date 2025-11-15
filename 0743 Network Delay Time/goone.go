type Pair struct{
    time, node int
}

type PairHeap []Pair
func (h PairHeap) Len() int {return len(h)}
func (h PairHeap) Less(i, j int) bool {return h[i].time < h[j].time}//< min heap. > max heap
func (h PairHeap) Swap(i, j int) {h[j], h[i] = h[i], h[j]}
func (h *PairHeap) Push(x interface{}) {*h = append(*h, x.(Pair))}
func (h *PairHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n - 1]
	*h = old[0 : n - 1 ]
	return x
}

func networkDelayTime(times [][]int, n int, k int) int {
    graph := make(map[int][]Pair)
    for _, t := range times {
        graph[t[0]] = append(graph[t[0]], Pair{t[2], t[1]})
    }
    h := &PairHeap{}
    heap.Init(h)
    heap.Push(h, Pair{time: 0, node: k})

    m := n + 1

    seen := make([]bool, m)
    time := make([]int, m)

    for h.Len() > 0 {
        
        temp := heap.Pop(h).(Pair)

        if seen[temp.node]{
            continue
        } 

        seen[temp.node] = true
        time[temp.node] = temp.time

        for _, g := range graph[temp.node] {
            if !seen[g.node] {
                heap.Push(h, Pair{time: g.time + temp.time,  node: g.node})
            }
        } 
    }
    maxDelay := 0
    for i := 1; i < m; i++{

        if !seen[i] {
            return -1
        }

        if time[i] > maxDelay {
            maxDelay = time[i]
        }
    }

    return maxDelay
}