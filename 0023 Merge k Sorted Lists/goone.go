/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type Triplet struct{
    val int
    idx int
    node *ListNode
}

type TripletHeap []Triplet
func (h TripletHeap) Len() int {return len(h)}
func (h TripletHeap) Less(i, j int) bool {return h[i].val < h[j].val}//< min heap. > max heap
func (h TripletHeap) Swap(i, j int) {h[j], h[i] = h[i], h[j]}
func (h *TripletHeap) Push(x interface{}) {*h = append(*h, x.(Triplet))}
func (h *TripletHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n - 1]
	*h = old[0 : n - 1 ]
	return x
}

func mergeKLists(lists []*ListNode) *ListNode {
    h := &TripletHeap{}
    heap.Init(h)

    for i, list := range lists {
        if list != nil {
            heap.Push(h, Triplet{list.Val, i, list})
        }
    }

    dummy := &ListNode{}
    current := dummy

    for h.Len() > 0 {
        temp := heap.Pop(h).(Triplet)
        current.Next = temp.node
        current = current.Next
        if temp.node.Next != nil {
            heap.Push(h, Triplet{temp.node.Next.Val, temp.idx, temp.node.Next})
        }
    }
    return dummy.Next
}