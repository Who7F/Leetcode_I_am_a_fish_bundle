
  Definition for a Node.
  type Node struct {
      Val int
      Next Node
      Random Node
  }
 

func copyRandomList(head Node) Node {
    if head == nil{
        return nil
    }

    nodeMap = make(map[Node]Node)
    h = head

    for h != nil{
        nodeMap[h] = &Node{Val h.Val}
        h = h.Next
    }

    h = head

    for h != nil{
        nodeMap[h].Next = nodeMap[h.Next]
        nodeMap[h].Random = nodeMap[h.Random]
        h = h.Next
    }

    return nodeMap[head]
}